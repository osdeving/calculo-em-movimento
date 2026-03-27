from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TEMP_MEDIA_DIR = REPO_ROOT / ".tmp" / "manim"

SCENES = [
    {
        "source": REPO_ROOT / "animations" / "manim" / "calculus_showcase.py",
        "scene": "KinematicsTimeSweepScene",
        "output_stem": "kinematics_time_sweep",
        "target": REPO_ROOT / "content" / "media" / "manim" / "kinematics_time_sweep.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
        "dependencies": [
            REPO_ROOT / "animations" / "manim" / "book_motion.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "composition_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "highlight_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "motion_recipes.py",
        ],
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "calculus_showcase.py",
        "scene": "CalculusTriptychScene",
        "output_stem": "calculus_triptych",
        "target": REPO_ROOT / "content" / "media" / "manim" / "calculus_triptych.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
        "dependencies": [
            REPO_ROOT / "animations" / "manim" / "book_motion.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "composition_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "highlight_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "tracker_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "transform_recipes.py",
        ],
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "calculus_showcase.py",
        "scene": "GeneralCurveDashboardScene",
        "output_stem": "general_curve_dashboard",
        "target": REPO_ROOT / "content" / "media" / "manim" / "general_curve_dashboard.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
        "dependencies": [
            REPO_ROOT / "animations" / "manim" / "book_motion.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "composition_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "highlight_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "tracker_recipes.py",
        ],
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "calculus_showcase.py",
        "scene": "IntegralUnitsScene",
        "output_stem": "integral_units_bridge",
        "target": REPO_ROOT / "content" / "media" / "manim" / "integral_units_bridge.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
        "dependencies": [
            REPO_ROOT / "animations" / "manim" / "book_motion.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "composition_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "highlight_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "transform_recipes.py",
        ],
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "calculus_showcase.py",
        "scene": "FundamentalCycleScene",
        "output_stem": "fundamental_cycle_dashboard",
        "target": REPO_ROOT / "content" / "media" / "manim" / "fundamental_cycle_dashboard.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
        "dependencies": [
            REPO_ROOT / "animations" / "manim" / "book_motion.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "composition_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "highlight_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "tracker_recipes.py",
        ],
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "calculus_showcase.py",
        "scene": "VelocityGraphOperationsScene",
        "output_stem": "velocity_graph_operations",
        "target": REPO_ROOT / "content" / "media" / "manim" / "velocity_graph_operations.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
        "dependencies": [
            REPO_ROOT / "animations" / "manim" / "book_motion.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "composition_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "highlight_recipes.py",
            REPO_ROOT / "animations" / "manim" / "recipes" / "tracker_recipes.py",
        ],
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "function_machine.py",
        "scene": "PositionFunctionMachineScene",
        "output_stem": "position_function_machine",
        "target": REPO_ROOT / "content" / "media" / "manim" / "position_function_machine.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
        "dependencies": [REPO_ROOT / "animations" / "manim" / "book_motion.py"],
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "AverageVelocityPostsScene",
        "output_stem": "average_velocity_posts",
        "target": REPO_ROOT / "content" / "media" / "manim" / "average_velocity_posts.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "UniformMotionGraphsScene",
        "output_stem": "mu_graphs_overview",
        "target": REPO_ROOT / "content" / "media" / "manim" / "mu_graphs_overview.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "AcceleratedMotionGraphsScene",
        "output_stem": "muv_graphs_overview",
        "target": REPO_ROOT / "content" / "media" / "manim" / "muv_graphs_overview.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "SecantToTangentScene",
        "output_stem": "secant_to_tangent",
        "target": REPO_ROOT / "content" / "media" / "manim" / "secant_to_tangent.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "DerivativeRulesScene",
        "output_stem": "derivative_rules_overview",
        "target": REPO_ROOT / "content" / "media" / "manim" / "derivative_rules_overview.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "IntegralAccumulationScene",
        "output_stem": "integral_accumulation_overview",
        "target": REPO_ROOT / "content" / "media" / "manim" / "integral_accumulation_overview.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "SignedAreaScene",
        "output_stem": "signed_area_overview",
        "target": REPO_ROOT / "content" / "media" / "manim" / "signed_area_overview.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "UniformAreaRectangleScene",
        "output_stem": "mu_area_rectangle",
        "target": REPO_ROOT / "content" / "media" / "manim" / "mu_area_rectangle.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "AcceleratedAreaDecompositionScene",
        "output_stem": "muv_area_decomposition",
        "target": REPO_ROOT / "content" / "media" / "manim" / "muv_area_decomposition.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "AverageVelocityAreaScene",
        "output_stem": "muv_average_velocity",
        "target": REPO_ROOT / "content" / "media" / "manim" / "muv_average_velocity.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "FormalIntegralBridgeScene",
        "output_stem": "integral_formal_bridge",
        "target": REPO_ROOT / "content" / "media" / "manim" / "integral_formal_bridge.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "UniformDerivativeBridgeScene",
        "output_stem": "mu_derivative_bridge",
        "target": REPO_ROOT / "content" / "media" / "manim" / "mu_derivative_bridge.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "AcceleratedDerivativeCascadeScene",
        "output_stem": "muv_derivative_cascade",
        "target": REPO_ROOT / "content" / "media" / "manim" / "muv_derivative_cascade.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "FundamentalTheoremKinematicsScene",
        "output_stem": "fundamental_theorem_kinematics",
        "target": REPO_ROOT / "content" / "media" / "manim" / "fundamental_theorem_kinematics.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "FormulaMapOverviewScene",
        "output_stem": "formula_map_overview",
        "target": REPO_ROOT / "content" / "media" / "manim" / "formula_map_overview.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "TrafficLightLaunchScene",
        "output_stem": "traffic_light_launch_example",
        "target": REPO_ROOT / "content" / "media" / "manim" / "traffic_light_launch_example.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
    {
        "source": REPO_ROOT / "animations" / "manim" / "kinematics.py",
        "scene": "EngineeringGraphReadingScene",
        "output_stem": "engineering_graph_reading",
        "target": REPO_ROOT / "content" / "media" / "manim" / "engineering_graph_reading.mp4",
        "format": "mp4",
        "quality": "l",
        "renderer": "cairo",
    },
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


def render_scene(scene: dict[str, object]) -> bool:
    dependencies = [scene["source"], *scene.get("dependencies", [])]
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
