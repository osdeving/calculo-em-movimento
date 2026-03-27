from __future__ import annotations

from collections.abc import Callable

from manim import Dot, TangentLine, Text, VGroup, ValueTracker, always_redraw


HIGHLIGHT = "#67d5e7"
INK = "#f4ead8"


def make_tracked_text(
    prefix: str,
    tracker: ValueTracker,
    formatter: Callable[[float], str] | None = None,
    font_size: int = 28,
    color: str = INK,
) -> Text:
    """Texto vivo para relogios, badges numericos e leituras de eixo."""

    format_value = formatter or (lambda value: f"{value:.2f}")
    return always_redraw(
        lambda: Text(
            f"{prefix}{format_value(tracker.get_value())}",
            font="DejaVu Sans",
            font_size=font_size,
            color=color,
            weight="BOLD",
        )
    )


def make_tangent_probe(
    graph,
    alpha_tracker: ValueTracker,
    point_color: str = HIGHLIGHT,
    tangent_color: str = INK,
    line_length: float = 2.6,
) -> VGroup:
    """Ponto e tangente guiados por tracker para cenas de derivada."""

    point = always_redraw(
        lambda: Dot(
            graph.point_from_proportion(alpha_tracker.get_value()),
            radius=0.075,
            color=point_color,
        )
    )
    tangent = always_redraw(
        lambda: TangentLine(
            graph,
            alpha=alpha_tracker.get_value(),
            length=line_length,
            color=tangent_color,
            stroke_width=4,
        )
    )
    return VGroup(tangent, point)

