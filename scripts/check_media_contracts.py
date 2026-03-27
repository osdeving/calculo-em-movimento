from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = REPO_ROOT / "content"
REFERENCE_ROOT = CONTENT_ROOT / "references"
RENDER_MANIM_ASSETS_PATH = REPO_ROOT / "scripts" / "render_manim_assets.py"

FIGURE_RE = re.compile(r"<figure\b.*?</figure>", re.IGNORECASE | re.DOTALL)
FIGCAPTION_RE = re.compile(r"<figcaption>(.*?)</figcaption>", re.IGNORECASE | re.DOTALL)
SOURCE_RE = re.compile(r'<source[^>]+src="([^"]+)"', re.IGNORECASE)
IMG_TAG_RE = re.compile(r'<img[^>]+src="([^"]+)"', re.IGNORECASE)
MARKDOWN_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def clean_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text, flags=re.UNICODE)
    return text.strip()


def load_scene_targets() -> set[str]:
    spec = importlib.util.spec_from_file_location("render_manim_assets_module", RENDER_MANIM_ASSETS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Não foi possível carregar scripts/render_manim_assets.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    scenes = getattr(module, "SCENES", [])
    return {
        Path(scene["target"]).resolve().relative_to(CONTENT_ROOT).as_posix()
        for scene in scenes
    }


def iter_content_markdown() -> list[Path]:
    paths: list[Path] = []
    for path in sorted(CONTENT_ROOT.rglob("*.md")):
        if path.name == "SUMMARY.md":
            continue
        if path.parent == REFERENCE_ROOT:
            continue
        paths.append(path)
    return paths


def resolve_content_path(source_path: Path, raw_path: str) -> Path:
    return (source_path.parent / raw_path).resolve()


def main() -> int:
    errors: list[str] = []
    scene_targets = load_scene_targets()
    referenced_manim_videos: set[str] = set()

    for path in iter_content_markdown():
        text = path.read_text(encoding="utf-8")

        for block_match in FIGURE_RE.finditer(text):
            block = block_match.group(0)
            is_video = "<video" in block.lower()
            has_img = "<img" in block.lower()
            caption_match = FIGCAPTION_RE.search(block)
            caption = clean_text(caption_match.group(1)) if caption_match else ""

            if (is_video or has_img) and not caption:
                errors.append(f"{path.relative_to(REPO_ROOT)}: figura/vídeo sem figcaption.")

            asset_match = SOURCE_RE.search(block) or IMG_TAG_RE.search(block)
            if asset_match:
                raw_asset_path = asset_match.group(1).strip()
                resolved = resolve_content_path(path, raw_asset_path)
                if not resolved.exists():
                    errors.append(
                        f"{path.relative_to(REPO_ROOT)}: asset referenciado não existe: {raw_asset_path}"
                    )
                if raw_asset_path.startswith("media/manim/"):
                    referenced_manim_videos.add(raw_asset_path)

        for line_number, line in enumerate(text.splitlines(), start=1):
            image_match = MARKDOWN_IMAGE_RE.search(line)
            if not image_match:
                continue

            alt_text = image_match.group(1).strip()
            asset_path = image_match.group(2).strip()
            resolved = resolve_content_path(path, asset_path)

            if not alt_text:
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}:{line_number}: imagem Markdown sem texto alternativo."
                )
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}:{line_number}: imagem referenciada não existe: {asset_path}"
                )

        for video_path in referenced_manim_videos:
            if video_path not in scene_targets:
                errors.append(
                    f"Vídeo referenciado no conteúdo não está registrado em scripts/render_manim_assets.py: {video_path}"
                )

    for target in sorted(scene_targets):
        if not (CONTENT_ROOT / target).exists():
            errors.append(f"Target registrado no pipeline Manim não existe no repositório: {target}")

    if errors:
        print("Falhas de contrato de mídia encontradas:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Contratos de mídia verificados com sucesso.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
