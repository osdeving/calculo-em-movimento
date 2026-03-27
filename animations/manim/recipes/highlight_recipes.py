from __future__ import annotations

from manim import Circumscribe, Flash, Indicate, Mobject


HIGHLIGHT = "#67d5e7"
ACCENT = "#d89a45"


def outline_focus(
    mobject: Mobject,
    color: str = HIGHLIGHT,
    stroke_width: float = 5,
    fade_out: bool = True,
    run_time: float = 1.0,
) -> Circumscribe:
    """Contorna um elemento para concentrar a atencao nele."""

    return Circumscribe(
        mobject,
        color=color,
        stroke_width=stroke_width,
        fade_out=fade_out,
        run_time=run_time,
    )


def pulse_focus(
    mobject: Mobject,
    color: str = ACCENT,
    scale_factor: float = 1.06,
    run_time: float = 0.75,
) -> Indicate:
    """Pulso rapido para destacar uma palavra, ponto ou marcador."""

    return Indicate(
        mobject,
        color=color,
        scale_factor=scale_factor,
        run_time=run_time,
    )


def spark_point(
    mobject: Mobject,
    color: str = HIGHLIGHT,
    line_length: float = 0.18,
    run_time: float = 0.7,
) -> Flash:
    """Explosao curta para sinalizar um valor importante."""

    return Flash(
        mobject.get_center(),
        color=color,
        line_length=line_length,
        run_time=run_time,
    )

