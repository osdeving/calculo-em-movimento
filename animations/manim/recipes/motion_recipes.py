from __future__ import annotations

from manim import MoveAlongPath, Mobject, TracedPath, smooth


HIGHLIGHT = "#67d5e7"


def make_motion_trail(
    mobject: Mobject,
    color: str = HIGHLIGHT,
    stroke_width: float = 4,
    dissipating_time: float | None = None,
) -> TracedPath:
    """Cria um rastro para objetos que precisam deixar memoria do caminho."""

    kwargs = {
        "stroke_color": color,
        "stroke_width": stroke_width,
    }
    if dissipating_time is not None:
        kwargs["dissipating_time"] = dissipating_time
    return TracedPath(mobject.get_center, **kwargs)


def travel_along_path(
    mobject: Mobject,
    path: Mobject,
    run_time: float = 2.2,
    rate_func=smooth,
) -> MoveAlongPath:
    """Move um objeto por uma curva, trilha ou eixo desenhado."""

    return MoveAlongPath(mobject, path, run_time=run_time, rate_func=rate_func)


def move_with_trail(
    mobject: Mobject,
    path: Mobject,
    color: str = HIGHLIGHT,
    stroke_width: float = 4,
    run_time: float = 2.2,
    rate_func=smooth,
) -> tuple[TracedPath, MoveAlongPath]:
    """Atalho para obter rastro e animacao no mesmo ponto."""

    trail = make_motion_trail(mobject, color=color, stroke_width=stroke_width)
    animation = travel_along_path(mobject, path, run_time=run_time, rate_func=rate_func)
    return trail, animation
