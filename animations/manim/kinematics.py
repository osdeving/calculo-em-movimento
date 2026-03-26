from __future__ import annotations

from manim import (
    Axes,
    Arrow,
    Circle,
    Create,
    DashedLine,
    Dot,
    DOWN,
    DoubleArrow,
    FadeIn,
    FadeOut,
    Indicate,
    LEFT,
    Line,
    Polygon,
    RIGHT,
    RoundedRectangle,
    Scene,
    Text,
    Transform,
    UP,
    VGroup,
    ValueTracker,
    always_redraw,
    linear,
    smooth,
)


PAPER = "#f6f1e6"
INK = "#2a2926"
MUTED = "#665f56"
ACCENT = "#8b5e34"
ACCENT_SOFT = "#d8c1a2"
CAR_RED = "#c8623b"
CAR_DARK = "#7e3c27"
HIGHLIGHT = "#1f7a8c"
SOFT_BLUE = "#d6eef2"


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
        fill_color="#fffaf2",
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
        fill_color="#fffaf2",
        fill_opacity=0.94,
    )
    label.move_to(card.get_center())
    return VGroup(card, label)


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
    wheel_left = Circle(radius=0.15, stroke_color=INK, stroke_width=3, fill_color=INK, fill_opacity=1)
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


def make_graph_axes(center, label: str, y_range: list[float]) -> tuple[VGroup, Axes]:
    axes = Axes(
        x_range=[0, 3.2, 1],
        y_range=y_range,
        x_length=3.15,
        y_length=1.35,
        tips=False,
        axis_config={"color": ACCENT, "stroke_width": 3, "include_ticks": False},
    ).move_to(center)
    title = Text(label, font="DejaVu Sans", font_size=20, color=INK).next_to(axes, UP, buff=0.05)
    t_label = Text("t", font="DejaVu Sans", font_size=18, color=MUTED).next_to(axes, RIGHT, buff=0.08)
    return VGroup(axes, title, t_label), axes


class AverageVelocityPostsScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text(
            "Velocidade media entre dois postes",
            font="DejaVu Serif",
            font_size=34,
            color=INK,
        ).to_edge(UP).shift(DOWN * 0.25)

        track, axis_point = make_track(left_edge=5.8, right_edge=5.5, y=1.15, max_value=80)
        axis, ticks, labels, axis_label = track

        post_a_point = axis_point(30)
        post_b_point = axis_point(66)
        post_a = Line(post_a_point + DOWN * 0.04, post_a_point + UP * 1.65, color=MUTED, stroke_width=5)
        post_b = Line(post_b_point + DOWN * 0.04, post_b_point + UP * 1.65, color=MUTED, stroke_width=5)
        post_a_label = Text("30 m", font="DejaVu Sans", font_size=22, color=INK).next_to(post_a, UP, buff=0.12)
        post_b_label = Text("66 m", font="DejaVu Sans", font_size=22, color=INK).next_to(post_b, UP, buff=0.12)

        start_marker = Line(post_a_point + DOWN * 0.25, post_a_point + UP * 0.52, color=HIGHLIGHT, stroke_width=5)
        end_marker = Line(post_b_point + DOWN * 0.25, post_b_point + UP * 0.52, color=HIGHLIGHT, stroke_width=5)
        car = make_car(0.78).move_to(post_a_point + UP * 0.44)

        start_box = make_info_box("t = 2 s", "x = 30 m", font_size=24).to_corner(UP + LEFT).shift(DOWN * 0.95 + RIGHT * 0.42)
        end_box = make_info_box("t = 5 s", "x = 66 m", font_size=24).move_to(start_box)

        delta_arrow = DoubleArrow(
            post_a_point + DOWN * 0.78,
            post_b_point + DOWN * 0.78,
            buff=0,
            stroke_width=5,
            tip_length=0.18,
            color=ACCENT,
        )
        delta_t = make_badge("Delta t = 3 s", font_size=22).move_to(delta_arrow.get_center() + UP * 0.34)
        delta_x = Text("Delta x = 36 m", font="DejaVu Sans", font_size=26, color=ACCENT).move_to(
            delta_arrow.get_center() + DOWN * 0.42
        )

        formula_box = make_info_box(
            "Delta x = 66 - 30 = 36 m",
            "Delta t = 5 - 2 = 3 s",
            "v_med = 36 / 3 = 12 m/s",
            font_size=23,
            highlight_last=True,
        ).to_corner(UP + RIGHT).shift(DOWN * 0.78 + LEFT * 0.32)

        self.play(FadeIn(title, shift=DOWN * 0.1))
        self.play(Create(axis), FadeIn(axis_label, shift=UP * 0.08))
        self.play(FadeIn(ticks, shift=UP * 0.06), FadeIn(labels, shift=UP * 0.06))
        self.play(Create(post_a), Create(post_b), FadeIn(post_a_label), FadeIn(post_b_label))
        self.play(FadeIn(start_marker), FadeIn(car, shift=LEFT * 0.12), FadeIn(start_box, shift=UP * 0.16))
        self.wait(0.2)
        self.play(
            car.animate.move_to(post_b_point + UP * 0.44),
            Transform(start_box, end_box),
            run_time=2.4,
            rate_func=linear,
        )
        self.play(FadeIn(end_marker))
        self.play(FadeOut(axis_label, shift=DOWN * 0.06))
        self.play(Create(delta_arrow), FadeIn(delta_t, shift=DOWN * 0.05), FadeIn(delta_x, shift=UP * 0.05))
        self.play(FadeIn(formula_box, shift=LEFT * 0.18))
        self.play(Indicate(formula_box[1][-1], scale_factor=1.04, color=HIGHLIGHT))
        self.wait(1.0)


class UniformMotionGraphsScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("MU: mesmos passos no mesmo tempo", font="DejaVu Serif", font_size=29, color=INK).to_edge(UP).shift(DOWN * 0.22)

        track, axis_point = make_track(left_edge=5.8, right_edge=0.4, y=1.25, max_value=60)
        axis, ticks, labels, axis_label = track

        positions = [8, 20, 32, 44]
        time_labels = VGroup()
        for index, value in enumerate(positions):
            marker = Line(axis_point(value) + DOWN * 0.18, axis_point(value) + UP * 0.42, color=HIGHLIGHT, stroke_width=4)
            tag = Text(f"t = {index} s", font="DejaVu Sans", font_size=18, color=INK).next_to(marker, UP, buff=0.08)
            time_labels.add(VGroup(marker, tag))

        car = make_car(0.62).move_to(axis_point(positions[0]) + UP * 0.44)
        trail = VGroup()
        equal_box = make_info_box(
            "No MU:",
            "a cada segundo, o",
            "deslocamento repete",
            "o mesmo padrao.",
            font_size=21,
        ).move_to(LEFT * 3.35 + UP * 1.5)

        x_panel_group, x_axes = make_graph_axes(RIGHT * 3.55 + UP * 1.5, "x(t)", [0, 5.8, 1])
        v_panel_group, v_axes = make_graph_axes(RIGHT * 3.55 + DOWN * 0.15, "v(t)", [0, 4.2, 1])
        a_panel_group, a_axes = make_graph_axes(RIGHT * 3.55 + DOWN * 1.8, "a(t)", [-0.6, 1.2, 1])

        x_line = x_axes.plot(lambda t: 1.0 + 1.05 * t, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
        v_line = v_axes.plot(lambda t: 2.5, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
        a_line = a_axes.plot(lambda t: 0, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(Create(axis), FadeIn(axis_label), FadeIn(ticks), FadeIn(labels))
        self.play(FadeIn(equal_box, shift=RIGHT * 0.12))
        self.play(FadeIn(time_labels[0]), FadeIn(car, shift=LEFT * 0.08))

        for index, value in enumerate(positions[1:], start=1):
            ghost = car.copy().set_opacity(0.26)
            trail.add(ghost)
            self.play(
                car.animate.move_to(axis_point(value) + UP * 0.44),
                FadeIn(ghost),
                FadeIn(time_labels[index]),
                run_time=0.78,
                rate_func=linear,
            )

        self.play(FadeIn(trail))
        self.play(FadeIn(x_panel_group), Create(x_line))
        self.play(FadeIn(v_panel_group), Create(v_line))
        self.play(FadeIn(a_panel_group), Create(a_line))
        self.play(Indicate(x_line, color=HIGHLIGHT), Indicate(v_line, color=HIGHLIGHT))
        self.wait(1.0)


class AcceleratedMotionGraphsScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("MUV: passos cada vez maiores", font="DejaVu Serif", font_size=30, color=INK).to_edge(UP).shift(DOWN * 0.22)

        track, axis_point = make_track(left_edge=5.8, right_edge=0.4, y=1.25, max_value=70)
        axis, ticks, labels, axis_label = track

        positions = [6, 15, 29, 50]
        car = make_car(0.62).move_to(axis_point(positions[0]) + UP * 0.44)
        time_labels = VGroup()
        for index, value in enumerate(positions):
            marker = Line(axis_point(value) + DOWN * 0.18, axis_point(value) + UP * 0.42, color=HIGHLIGHT, stroke_width=4)
            tag = Text(f"t = {index} s", font="DejaVu Sans", font_size=18, color=INK).next_to(marker, UP, buff=0.08)
            time_labels.add(VGroup(marker, tag))

        growing_box = make_info_box(
            "No MUV:",
            "o espacamento cresce",
            "porque a velocidade",
            "aumenta a cada passo.",
            font_size=21,
        ).move_to(LEFT * 3.35 + UP * 1.5)

        gap_1 = make_badge("+9 m", font_size=20).move_to((axis_point(positions[0]) + axis_point(positions[1])) / 2 + DOWN * 0.64)
        gap_2 = make_badge("+14 m", font_size=20).move_to((axis_point(positions[1]) + axis_point(positions[2])) / 2 + DOWN * 0.73)
        gap_3 = make_badge("+21 m", font_size=20).move_to((axis_point(positions[2]) + axis_point(positions[3])) / 2 + DOWN * 0.64)

        x_panel_group, x_axes = make_graph_axes(RIGHT * 3.55 + UP * 1.5, "x(t)", [0, 7.0, 1])
        v_panel_group, v_axes = make_graph_axes(RIGHT * 3.55 + DOWN * 0.15, "v(t)", [0, 6.0, 1])
        a_panel_group, a_axes = make_graph_axes(RIGHT * 3.55 + DOWN * 1.8, "a(t)", [0, 3.2, 1])

        x_curve = x_axes.plot(lambda t: 0.45 * t * t + 0.5 * t + 0.8, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
        v_line = v_axes.plot(lambda t: 1.2 + 1.25 * t, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
        a_line = a_axes.plot(lambda t: 1.8, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(Create(axis), FadeIn(axis_label), FadeIn(ticks), FadeIn(labels))
        self.play(FadeIn(growing_box, shift=RIGHT * 0.12))
        self.play(FadeIn(time_labels[0]), FadeIn(car, shift=LEFT * 0.08))

        for index, value in enumerate(positions[1:], start=1):
            self.play(
                car.animate.move_to(axis_point(value) + UP * 0.44),
                FadeIn(time_labels[index]),
                run_time=0.78,
                rate_func=linear,
            )

        self.play(FadeIn(gap_1), FadeIn(gap_2), FadeIn(gap_3))
        self.play(FadeIn(x_panel_group), Create(x_curve))
        self.play(FadeIn(v_panel_group), Create(v_line))
        self.play(FadeIn(a_panel_group), Create(a_line))
        self.play(Indicate(x_curve, color=HIGHLIGHT), Indicate(v_line, color=HIGHLIGHT))
        self.wait(1.0)


class SecantToTangentScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("Da secante para a tangente", font="DejaVu Serif", font_size=32, color=INK).to_edge(UP).shift(DOWN * 0.18)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 18, 4],
            x_length=8.9,
            y_length=4.4,
            tips=False,
            axis_config={"color": ACCENT, "stroke_width": 3},
        ).move_to(DOWN * 0.55)
        t_label = Text("t", font="DejaVu Sans", font_size=20, color=MUTED).next_to(axes, RIGHT, buff=0.1)
        x_label = Text("x(t)", font="DejaVu Sans", font_size=20, color=MUTED).next_to(axes, UP + LEFT, buff=0.15)

        def f(t: float) -> float:
            return 0.55 * t * t + 0.7 * t + 1.0

        def f_prime(t: float) -> float:
            return 1.1 * t + 0.7

        curve = axes.plot(f, x_range=[0.2, 5.5], color=HIGHLIGHT, stroke_width=5)
        t0 = 2.0
        h = ValueTracker(2.0)

        dot_a = always_redraw(lambda: Dot(axes.c2p(t0, f(t0)), radius=0.075, color=CAR_RED))
        dot_b = always_redraw(lambda: Dot(axes.c2p(t0 + h.get_value(), f(t0 + h.get_value())), radius=0.075, color=ACCENT))
        secant = always_redraw(lambda: Line(dot_a.get_center(), dot_b.get_center(), color=ACCENT, stroke_width=4))
        v_line_a = always_redraw(lambda: DashedLine(dot_a.get_center(), axes.c2p(t0, 0), dash_length=0.1, color=MUTED, stroke_width=2))
        v_line_b = always_redraw(lambda: DashedLine(dot_b.get_center(), axes.c2p(t0 + h.get_value(), 0), dash_length=0.1, color=MUTED, stroke_width=2))
        point_label_a = always_redraw(lambda: Text("A", font="DejaVu Sans", font_size=20, color=CAR_RED).next_to(dot_a, UP, buff=0.08))
        point_label_b = always_redraw(lambda: Text("B", font="DejaVu Sans", font_size=20, color=ACCENT).next_to(dot_b, UP, buff=0.08))

        delta_box = always_redraw(
            lambda: make_info_box(
                "Intervalo observado",
                f"Delta t = {h.get_value():.2f} s",
                font_size=22,
                highlight_last=True,
            ).to_corner(UP + RIGHT).shift(DOWN * 0.82 + LEFT * 0.35)
        )

        tangent = axes.plot(
            lambda x: f(t0) + f_prime(t0) * (x - t0),
            x_range=[t0 - 1.05, t0 + 1.05],
            color=HIGHLIGHT,
            stroke_width=5,
        )
        final_box = make_info_box(
            "Quando Delta t encolhe,",
            "a secante se aproxima",
            "da tangente.",
            "Essa inclinacao local",
            "representa v(t).",
            font_size=21,
            highlight_last=True,
        ).to_corner(UP + LEFT).shift(DOWN * 0.95 + RIGHT * 0.4)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(Create(axes), FadeIn(t_label), FadeIn(x_label))
        self.play(Create(curve))
        self.play(FadeIn(dot_a), FadeIn(dot_b), Create(v_line_a), Create(v_line_b), Create(secant))
        self.play(FadeIn(point_label_a), FadeIn(point_label_b), FadeIn(delta_box))
        self.play(h.animate.set_value(1.0), run_time=1.4, rate_func=smooth)
        self.play(h.animate.set_value(0.35), run_time=1.4, rate_func=smooth)
        self.play(h.animate.set_value(0.12), run_time=1.3, rate_func=smooth)
        self.play(Create(tangent), FadeIn(final_box, shift=RIGHT * 0.12))
        self.play(Indicate(tangent, color=HIGHLIGHT))
        self.wait(1.0)
