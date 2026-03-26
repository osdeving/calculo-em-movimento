from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TEMP_MEDIA_DIR = REPO_ROOT / ".tmp" / "manim"

SCENES = [
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "AverageVelocityPostsScene",
        "output_stem": "average_velocity_posts",
        "target": REPO_ROOT / "content" / "media" / "manim" / "average_velocity_posts.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    }
]


def latest_mtime(paths: list[Path]) -> float:
    return max(path.stat().st_mtime for path in paths if path.exists())


def is_up_to_date(target: Path, dependencies: list[Path]) -> bool:
    return target.exists() and target.stat().st_mtime >= latest_mtime(dependencies)


def find_rendered_file(output_stem: str, extension: str) -> Path:
    matches = sorted(
        TEMP_MEDIA_DIR.rglob(f"{output_stem}.{extension}"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    if not matches:
        raise FileNotFoundError(f"Manim render output not found for {output_stem}.{extension}")
    return matches[0]


def copy_if_changed(source: Path, target: Path) -> bool:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and source.read_bytes() == target.read_bytes():
        print(f"manim unchanged: {target.relative_to(REPO_ROOT)}")
        return False
    shutil.copy2(source, target)
    print(f"manim updated:   {target.relative_to(REPO_ROOT)}")
    return True


def render_scene(scene: dict[str, Path | str]) -> bool:
    dependencies = [Path(__file__), scene["source"]]
    target = scene["target"]
    if is_up_to_date(target, dependencies):
        print(f"manim up-to-date: {target.relative_to(REPO_ROOT)}")
        return False

    command = [
        "manim",
        "--renderer",
        str(scene["renderer"]),
        "-q",
        str(scene["quality"]),
        "--format",
        str(scene["format"]),
        "--media_dir",
        str(TEMP_MEDIA_DIR),
        "-o",
        str(scene["output_stem"]),
        str(scene["source"]),
        str(scene["scene"]),
    ]
    print("$ " + " ".join(command))
    subprocess.run(command, cwd=REPO_ROOT, check=True)

    rendered = find_rendered_file(str(scene["output_stem"]), str(scene["format"]))
    return copy_if_changed(rendered, target)


def main() -> int:
    changed = False
    for scene in SCENES:
        changed = render_scene(scene) or changed
    if not changed:
        print("All Manim assets are up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
