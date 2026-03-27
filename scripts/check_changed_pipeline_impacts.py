from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RENDER_MANIM_ASSETS_PATH = REPO_ROOT / "scripts" / "render_manim_assets.py"
GENERATED_ASSETS_SCRIPT = "scripts/generate_scene_assets.py"
MANIM_PIPELINE_SCRIPT = "scripts/render_manim_assets.py"


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def load_scenes() -> list[dict[str, object]]:
    spec = importlib.util.spec_from_file_location("render_manim_assets_module", RENDER_MANIM_ASSETS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Não foi possível carregar scripts/render_manim_assets.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return list(getattr(module, "SCENES", []))


def changed_files_from_worktree() -> set[str]:
    changed: set[str] = set()
    output = run_git("status", "--porcelain")
    for line in output.splitlines():
        if not line:
            continue
        raw_path = line[3:]
        if " -> " in raw_path:
            raw_path = raw_path.split(" -> ", 1)[1]
        changed.add(raw_path)
    return changed


def changed_files_from_ref(base_ref: str) -> set[str]:
    output = run_git("diff", "--name-only", "--diff-filter=ACMRTUXB", f"{base_ref}...HEAD")
    return {line.strip() for line in output.splitlines() if line.strip()}


def relative_repo_path(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def main() -> int:
    parser = argparse.ArgumentParser(description="Verifica se mudanças em pipelines vieram acompanhadas dos artefatos esperados.")
    parser.add_argument("--base-ref", help="Ref ou commit base para comparação. Se omitido, usa alterações locais do worktree.")
    args = parser.parse_args()

    changed_files = changed_files_from_ref(args.base_ref) if args.base_ref else changed_files_from_worktree()
    if not changed_files:
        print("Nenhuma mudança detectada para checar impactos de pipeline.")
        return 0

    errors: list[str] = []
    scenes = load_scenes()
    changed_media = {path for path in changed_files if path.startswith("content/media/manim/")}
    changed_assets = {path for path in changed_files if path.startswith("content/assets/")}

    if MANIM_PIPELINE_SCRIPT in changed_files and not changed_media:
        errors.append(
            "scripts/render_manim_assets.py mudou, mas nenhum arquivo em content/media/manim/ foi atualizado."
        )

    for scene in scenes:
        source_path = relative_repo_path(Path(scene["source"]))
        dependency_paths = [relative_repo_path(Path(dep)) for dep in scene.get("dependencies", [])]
        target_path = relative_repo_path(Path(scene["target"]))
        watched_paths = {source_path, *dependency_paths}

        if watched_paths & changed_files and target_path not in changed_files:
            scene_name = str(scene["scene"])
            errors.append(
                f"{scene_name} teve fonte/dependência alterada ({', '.join(sorted(watched_paths & changed_files))}), "
                f"mas o artefato {target_path} não mudou."
            )

    if GENERATED_ASSETS_SCRIPT in changed_files and not changed_assets:
        errors.append(
            "scripts/generate_scene_assets.py mudou, mas nenhum arquivo em content/assets/ foi atualizado."
        )

    if errors:
        print("Falhas de impacto de pipeline encontradas:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Impactos de pipeline verificados com sucesso.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
