from __future__ import annotations

from manim import (
    Arrow,
    Circle,
    Create,
    DOWN,
    DoubleArrow,
    FadeIn,
    Indicate,
    LEFT,
    Line,
    ORIGIN,
    PI,
    Polygon,
    RIGHT,
    RoundedRectangle,
    Scene,
    Text,
    UP,
    VGroup,
    Write,
    linear,
)


PAPER = "#f6f1e6"
INK = "#2a2926"
MUTED = "#665f56"
ACCENT = "#8b5e34"
ACCENT_SOFT = "#d8c1a2"
CAR_RED = "#c8623b"
CAR_DARK = "#7e3c27"
HIGHLIGHT = "#1f7a8c"


def make_info_box(*lines: str, highlight_last: bool = False) -> VGroup:
    texts = []
    for index, line in enumerate(lines):
        color = HIGHLIGHT if highlight_last and index == len(lines) - 1 else INK
        weight = "BOLD" if highlight_last and index == len(lines) - 1 else "NORMAL"
        texts.append(Text(line, font="DejaVu Sans", font_size=28, color=color, weight=weight))

    content = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
    card = RoundedRectangle(
        corner_radius=0.18,
        height=content.height + 0.45,
        width=content.width + 0.6,
        stroke_color=ACCENT_SOFT,
        stroke_width=2,
        fill_color="#fffaf2",
        fill_opacity=1,
    )
    content.move_to(card.get_center())
    return VGroup(card, content)


def make_car() -> VGroup:
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
        fill_color="#d6eef2",
        fill_opacity=0.95,
    )
    wheel_left = Circle(radius=0.15, stroke_color=INK, stroke_width=3, fill_color=INK, fill_opacity=1)
    wheel_right = wheel_left.copy()
    wheel_left.move_to(body.get_bottom() + LEFT * 0.42 + DOWN * 0.02)
    wheel_right.move_to(body.get_bottom() + RIGHT * 0.42 + DOWN * 0.02)
    return VGroup(body, cabin, windshield, wheel_left, wheel_right)


class AverageVelocityPostsScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text(
            "Velocidade media entre dois postes",
            font="DejaVu Serif",
            font_size=34,
            color=INK,
        ).to_edge(UP).shift(DOWN * 0.25)

        axis_start = LEFT * 5.5 + DOWN * 0.85
        axis_end = RIGHT * 5.5 + DOWN * 0.85
        axis = Arrow(axis_start, axis_end, buff=0, stroke_width=6, tip_length=0.24, color=ACCENT)
        axis_label = Text("eixo S (m)", font="DejaVu Sans", font_size=24, color=MUTED).next_to(axis, DOWN, buff=0.45)

        def axis_point(value: float):
            return axis_start + (axis_end - axis_start) * (value / 80.0)

        ticks = VGroup()
        labels = VGroup()
        for value in range(0, 81, 10):
            point = axis_point(value)
            tick = Line(point + DOWN * 0.12, point + UP * 0.12, color=ACCENT, stroke_width=3)
            label = Text(str(value), font="DejaVu Sans", font_size=20, color=MUTED).next_to(tick, DOWN, buff=0.14)
            ticks.add(tick)
            labels.add(label)

        post_a_point = axis_point(30)
        post_b_point = axis_point(66)
        post_a = Line(post_a_point + DOWN * 0.04, post_a_point + UP * 1.75, color=MUTED, stroke_width=5)
        post_b = Line(post_b_point + DOWN * 0.04, post_b_point + UP * 1.75, color=MUTED, stroke_width=5)
        post_a_label = Text("30 m", font="DejaVu Sans", font_size=22, color=INK).next_to(post_a, UP, buff=0.15)
        post_b_label = Text("66 m", font="DejaVu Sans", font_size=22, color=INK).next_to(post_b, UP, buff=0.15)

        start_marker = Line(post_a_point + DOWN * 0.25, post_a_point + UP * 0.55, color=HIGHLIGHT, stroke_width=5)
        end_marker = Line(post_b_point + DOWN * 0.25, post_b_point + UP * 0.55, color=HIGHLIGHT, stroke_width=5)

        car = make_car().scale(0.88).move_to(post_a_point + UP * 0.55)

        start_box = make_info_box("t = 2 s", "x = 30 m").to_corner(UP + LEFT).shift(DOWN * 0.95 + RIGHT * 0.45)
        end_box = make_info_box("t = 5 s", "x = 66 m").move_to(start_box)

        delta_arrow = DoubleArrow(
            post_a_point + DOWN * 0.62,
            post_b_point + DOWN * 0.62,
            buff=0,
            stroke_width=5,
            tip_length=0.18,
            color=ACCENT,
        )
        delta_x = Text("Delta x = 36 m", font="DejaVu Sans", font_size=26, color=ACCENT).next_to(delta_arrow, DOWN, buff=0.16)
        delta_t = Text("Delta t = 3 s", font="DejaVu Sans", font_size=26, color=ACCENT).next_to(delta_arrow, UP, buff=0.12)

        formula_box = make_info_box(
            "Delta x = 66 - 30 = 36 m",
            "Delta t = 5 - 2 = 3 s",
            "v_med = 36 / 3 = 12 m/s",
            highlight_last=True,
        ).to_corner(UP + RIGHT).shift(DOWN * 1.05 + LEFT * 0.4)

        statement = Text(
            "O carro avanca 36 m em 3 s.",
            font="DejaVu Sans",
            font_size=28,
            color=INK,
        ).next_to(delta_arrow, DOWN, buff=0.7)

        self.play(FadeIn(title, shift=DOWN * 0.1))
        self.play(Create(axis), FadeIn(axis_label, shift=UP * 0.1))
        self.play(FadeIn(ticks, shift=UP * 0.08), FadeIn(labels, shift=UP * 0.08))
        self.play(Create(post_a), Create(post_b), FadeIn(post_a_label), FadeIn(post_b_label))
        self.play(FadeIn(start_marker), FadeIn(car, shift=LEFT * 0.18), FadeIn(start_box, shift=UP * 0.18))
        self.wait(0.2)
        self.play(
            car.animate.move_to(post_b_point + UP * 0.55),
            start_box.animate.become(end_box),
            run_time=2.6,
            rate_func=linear,
        )
        self.play(FadeIn(end_marker))
        self.play(Create(delta_arrow), FadeIn(delta_t, shift=DOWN * 0.08), FadeIn(delta_x, shift=UP * 0.08))
        self.play(FadeIn(formula_box, shift=LEFT * 0.2))
        self.play(Write(statement))
        self.play(Indicate(formula_box[1][-1], scale_factor=1.04, color=HIGHLIGHT))
        self.wait(1.0)
