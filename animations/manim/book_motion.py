from __future__ import annotations

from manim import (
    Axes,
    Arrow,
    Circle,
    DOWN,
    LEFT,
    Line,
    Polygon,
    RIGHT,
    RoundedRectangle,
    TAU,
    Text,
    UP,
    VGroup,
    ValueTracker,
    always_redraw,
    rotate_vector,
)


PAPER = "#05070d"
INK = "#f4ead8"
MUTED = "#c5b79f"
ACCENT = "#d89a45"
ACCENT_SOFT = "#6c4b23"
CARD_FILL = "#101722"
CARD_FILL_ALT = "#16202d"
CAR_RED = "#d96f48"
CAR_DARK = "#8d452d"
CAR_WHEEL = "#0d1118"
HIGHLIGHT = "#67d5e7"
SOFT_BLUE = "#18394d"
NEGATIVE = "#e07a6b"
NEGATIVE_SOFT = "#5d2520"


def make_info_box(
    *lines: str,
    font_size: int = 28,
    highlight_last: bool = False,
    highlight_color: str = HIGHLIGHT,
) -> VGroup:
    texts = []
    for index, line in enumerate(lines):
        is_highlight = highlight_last and index == len(lines) - 1
        texts.append(
            Text(
                line,
                font="DejaVu Sans",
                font_size=font_size,
                color=highlight_color if is_highlight else INK,
                weight="BOLD" if is_highlight else "NORMAL",
            )
        )

    content = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
    card = RoundedRectangle(
        corner_radius=0.18,
        height=content.height + 0.42,
        width=content.width + 0.56,
        stroke_color=ACCENT_SOFT,
        stroke_width=2,
        fill_color=CARD_FILL,
        fill_opacity=1,
    )
    content.move_to(card.get_center())
    return VGroup(card, content)


def make_badge(text: str, font_size: int = 22, color: str = ACCENT) -> VGroup:
    label = Text(text, font="DejaVu Sans", font_size=font_size, color=color, weight="BOLD")
    card = RoundedRectangle(
        corner_radius=0.16,
        height=label.height + 0.22,
        width=label.width + 0.34,
        stroke_color=ACCENT_SOFT,
        stroke_width=2,
        fill_color=CARD_FILL_ALT,
        fill_opacity=0.94,
    )
    label.move_to(card.get_center())
    return VGroup(card, label)


def make_signal_chip(
    text: str,
    font_size: int = 22,
    color: str = HIGHLIGHT,
    fill_color: str = CARD_FILL_ALT,
) -> VGroup:
    label = Text(text, font="DejaVu Sans", font_size=font_size, color=color, weight="BOLD")
    chip = RoundedRectangle(
        corner_radius=0.18,
        height=label.height + 0.26,
        width=label.width + 0.42,
        stroke_color=color,
        stroke_width=2.4,
        fill_color=fill_color,
        fill_opacity=1,
    )
    label.move_to(chip.get_center())
    return VGroup(chip, label)


def make_car(scale_factor: float = 1.0) -> VGroup:
    body = RoundedRectangle(
        corner_radius=0.14,
        width=1.55,
        height=0.42,
        stroke_color=CAR_DARK,
        stroke_width=3,
        fill_color=CAR_RED,
        fill_opacity=1,
    )
    cabin = RoundedRectangle(
        corner_radius=0.12,
        width=0.72,
        height=0.32,
        stroke_color=CAR_DARK,
        stroke_width=3,
        fill_color="#f0d7c5",
        fill_opacity=1,
    ).move_to(body.get_center() + UP * 0.26 + LEFT * 0.18)
    windshield = Polygon(
        cabin.get_corner(UP + LEFT),
        cabin.get_corner(UP + RIGHT) + DOWN * 0.04,
        cabin.get_corner(DOWN + RIGHT),
        cabin.get_corner(DOWN + LEFT),
        stroke_width=0,
        fill_color=SOFT_BLUE,
        fill_opacity=0.95,
    )
    wheel_left = Circle(radius=0.15, stroke_color=CAR_WHEEL, stroke_width=3, fill_color=CAR_WHEEL, fill_opacity=1)
    wheel_right = wheel_left.copy()
    wheel_left.move_to(body.get_bottom() + LEFT * 0.42 + DOWN * 0.02)
    wheel_right.move_to(body.get_bottom() + RIGHT * 0.42 + DOWN * 0.02)
    return VGroup(body, cabin, windshield, wheel_left, wheel_right).scale(scale_factor)


def make_track(
    left_edge: float,
    right_edge: float,
    y: float,
    max_value: float,
    tick_step: int = 10,
) -> tuple[VGroup, callable]:
    axis_start = LEFT * abs(left_edge) + DOWN * abs(y)
    axis_end = RIGHT * right_edge + DOWN * abs(y)
    axis = Arrow(axis_start, axis_end, buff=0, stroke_width=5, tip_length=0.22, color=ACCENT)

    ticks = VGroup()
    labels = VGroup()
    for value in range(0, int(max_value) + 1, tick_step):
        point = axis_start + (axis_end - axis_start) * (value / max_value)
        tick = Line(point + DOWN * 0.1, point + UP * 0.1, color=ACCENT, stroke_width=3)
        label = Text(str(value), font="DejaVu Sans", font_size=18, color=MUTED).next_to(tick, DOWN, buff=0.1)
        ticks.add(tick)
        labels.add(label)

    axis_label = Text("eixo S (m)", font="DejaVu Sans", font_size=22, color=MUTED).next_to(axis, DOWN, buff=0.4)

    def axis_point(value: float):
        return axis_start + (axis_end - axis_start) * (value / max_value)

    return VGroup(axis, ticks, labels, axis_label), axis_point


def make_stopwatch(
    time_tracker: ValueTracker,
    max_time: float = 4.0,
    scale_factor: float = 1.0,
) -> VGroup:
    shell = Circle(radius=0.82, stroke_color=ACCENT, stroke_width=4, fill_color=CARD_FILL, fill_opacity=1)
    face = Circle(radius=0.68, stroke_color=ACCENT_SOFT, stroke_width=2, fill_color=CARD_FILL_ALT, fill_opacity=1)
    crown = RoundedRectangle(
        corner_radius=0.08,
        width=0.36,
        height=0.18,
        stroke_color=ACCENT,
        stroke_width=3,
        fill_color=CARD_FILL_ALT,
        fill_opacity=1,
    ).next_to(shell, UP, buff=-0.02)
    button = RoundedRectangle(
        corner_radius=0.05,
        width=0.16,
        height=0.12,
        stroke_color=ACCENT,
        stroke_width=2,
        fill_color=CARD_FILL_ALT,
        fill_opacity=1,
    ).next_to(crown, RIGHT, buff=0.05).shift(UP * 0.03)

    ticks = VGroup()
    for step in range(12):
        tick = Line(UP * 0.5, UP * 0.62, color=MUTED, stroke_width=2).rotate(-step * TAU / 12)
        ticks.add(tick)
    ticks.move_to(face.get_center())

    hand = always_redraw(
        lambda: Line(
            face.get_center(),
            face.get_center() + rotate_vector(UP * 0.48, -TAU * time_tracker.get_value() / max_time),
            color=HIGHLIGHT,
            stroke_width=4,
        )
    )
    center_dot = Circle(radius=0.055, stroke_width=0, fill_color=HIGHLIGHT, fill_opacity=1).move_to(face.get_center())
    readout = always_redraw(
        lambda: Text(
            f"t = {int(round(time_tracker.get_value()))} s",
            font="DejaVu Sans",
            font_size=22,
            color=INK,
            weight="BOLD",
        ).next_to(shell, DOWN, buff=0.18)
    )

    return VGroup(shell, face, ticks, hand, center_dot, crown, button, readout).scale(scale_factor)


def make_function_machine(
    label: str = "x(t)",
    subtitle: str = "tempo -> posicao",
    scale_factor: float = 1.0,
) -> VGroup:
    shell = RoundedRectangle(
        corner_radius=0.24,
        width=3.55,
        height=2.35,
        stroke_color=ACCENT,
        stroke_width=3.2,
        fill_color=CARD_FILL_ALT,
        fill_opacity=1,
    )
    screen = RoundedRectangle(
        corner_radius=0.16,
        width=2.2,
        height=0.82,
        stroke_color=ACCENT_SOFT,
        stroke_width=2.2,
        fill_color=CARD_FILL,
        fill_opacity=1,
    ).move_to(shell.get_center() + UP * 0.42)
    label_text = Text(label, font="DejaVu Sans", font_size=34, color=INK, weight="BOLD").move_to(screen.get_center())
    subtitle_text = Text(subtitle, font="DejaVu Sans", font_size=18, color=MUTED).move_to(shell.get_center() + DOWN * 0.55)

    input_port = RoundedRectangle(
        corner_radius=0.05,
        width=0.26,
        height=0.5,
        stroke_color=ACCENT,
        stroke_width=2,
        fill_color=CARD_FILL,
        fill_opacity=1,
    ).next_to(shell, LEFT, buff=-0.02)
    output_port = input_port.copy().next_to(shell, RIGHT, buff=-0.02)

    lights = VGroup(
        Circle(radius=0.06, stroke_width=0, fill_color="#72c48d", fill_opacity=1),
        Circle(radius=0.06, stroke_width=0, fill_color="#f0c05a", fill_opacity=1),
        Circle(radius=0.06, stroke_width=0, fill_color="#d86d5a", fill_opacity=1),
    ).arrange(RIGHT, buff=0.14).move_to(shell.get_center() + DOWN * 0.12 + LEFT * 0.86)

    core_outer = Circle(radius=0.18, stroke_color=HIGHLIGHT, stroke_width=2.4, fill_color=CARD_FILL, fill_opacity=1)
    core_inner = Circle(radius=0.05, stroke_width=0, fill_color=HIGHLIGHT, fill_opacity=1)
    spokes = VGroup(
        Line(UP * 0.14, DOWN * 0.14, color=HIGHLIGHT, stroke_width=2),
        Line(LEFT * 0.14, RIGHT * 0.14, color=HIGHLIGHT, stroke_width=2),
        Line(UP * 0.1 + LEFT * 0.1, DOWN * 0.1 + RIGHT * 0.1, color=HIGHLIGHT, stroke_width=2),
        Line(UP * 0.1 + RIGHT * 0.1, DOWN * 0.1 + LEFT * 0.1, color=HIGHLIGHT, stroke_width=2),
    )
    core = VGroup(core_outer, spokes, core_inner).move_to(shell.get_center() + DOWN * 0.12 + RIGHT * 0.92)

    machine = VGroup(shell, screen, label_text, subtitle_text, input_port, output_port, lights, core)
    return machine.scale(scale_factor)
