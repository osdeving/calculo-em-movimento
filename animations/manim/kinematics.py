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
    Rectangle,
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


def make_traffic_light(scale_factor: float = 1.0) -> VGroup:
    housing = RoundedRectangle(
        corner_radius=0.12,
        width=0.62,
        height=1.72,
        stroke_color=INK,
        stroke_width=3,
        fill_color=MUTED,
        fill_opacity=1,
    )
    red = Circle(radius=0.12, stroke_width=0, fill_color="#d44f3a", fill_opacity=1).move_to(housing.get_top() + DOWN * 0.34)
    yellow = Circle(radius=0.12, stroke_width=0, fill_color="#e2b44d", fill_opacity=1).move_to(housing.get_center())
    green = Circle(radius=0.12, stroke_width=0, fill_color="#4f9d63", fill_opacity=1).move_to(housing.get_bottom() + UP * 0.34)
    pole = Line(housing.get_bottom(), housing.get_bottom() + DOWN * 1.1, color=INK, stroke_width=5)
    return VGroup(housing, red, yellow, green, pole).scale(scale_factor)


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


def make_stage_axes(
    center,
    y_label_text: str,
    y_range: list[float],
    x_range: list[float] | None = None,
    x_length: float = 4.6,
    y_length: float = 2.7,
) -> tuple[VGroup, Axes]:
    axes = Axes(
        x_range=x_range or [0, 4.2, 1],
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        tips=False,
        axis_config={"color": ACCENT, "stroke_width": 3},
    ).move_to(center)
    x_label = Text("t", font="DejaVu Sans", font_size=20, color=MUTED).next_to(axes, RIGHT, buff=0.08)
    y_label = Text(y_label_text, font="DejaVu Sans", font_size=20, color=MUTED).next_to(axes, UP + LEFT, buff=0.1)
    return VGroup(axes, x_label, y_label), axes


def make_axis_polygon(
    axes: Axes,
    points: list[tuple[float, float]],
    fill_color: str = ACCENT_SOFT,
    fill_opacity: float = 0.35,
    stroke_color: str = ACCENT,
    stroke_width: float = 3,
) -> Polygon:
    return Polygon(
        *[axes.c2p(x, y) for x, y in points],
        fill_color=fill_color,
        fill_opacity=fill_opacity,
        stroke_color=stroke_color,
        stroke_width=stroke_width,
    )


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


class DerivativeRulesScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("Derivada: o formato ja entrega a resposta", font="DejaVu Serif", font_size=30, color=INK).to_edge(UP).shift(DOWN * 0.2)
        subtitle = Text(
            "Constante vira zero, reta vira constante, parabola vira reta.",
            font="DejaVu Sans",
            font_size=20,
            color=MUTED,
        ).next_to(title, DOWN, buff=0.12)

        centers = [LEFT * 4.4 + DOWN * 0.15, DOWN * 0.15, RIGHT * 4.4 + DOWN * 0.15]
        panels = VGroup()
        curves = VGroup()
        cards = VGroup()

        specs = [
            ("x(t)", [0, 3.6, 1], lambda t: 2.2, "v(t) = 0"),
            ("x(t)", [0, 4.6, 1], lambda t: 0.9 + 0.8 * t, "v(t) = constante"),
            ("x(t)", [0, 6.6, 1], lambda t: 0.45 * t * t + 0.5, "v(t) = reta"),
        ]

        for center, (label, y_range, func, card_text) in zip(centers, specs):
            panel, axes = make_stage_axes(center, label, y_range, x_length=2.6, y_length=1.8)
            graph = axes.plot(func, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
            card = make_info_box(card_text, font_size=22, highlight_last=True).scale(0.86).next_to(panel, DOWN, buff=0.35)
            panels.add(panel)
            curves.add(graph)
            cards.add(card)

        self.play(FadeIn(title, shift=DOWN * 0.08), FadeIn(subtitle, shift=DOWN * 0.08))
        for panel, graph, card in zip(panels, curves, cards):
            self.play(FadeIn(panel), Create(graph))
            self.play(FadeIn(card, shift=UP * 0.08))
        self.play(Indicate(curves[1], color=HIGHLIGHT), Indicate(cards[1][1][0], color=HIGHLIGHT))
        self.play(Indicate(curves[2], color=HIGHLIGHT), Indicate(cards[2][1][0], color=HIGHLIGHT))
        self.wait(1.0)


class IntegralAccumulationScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("Integral: somar pequenas contribuicoes", font="DejaVu Serif", font_size=31, color=INK).to_edge(UP).shift(DOWN * 0.2)

        axes_group, axes = make_stage_axes(LEFT * 1.6 + DOWN * 0.2, "v(t)", [0, 5.5, 1], x_length=6.2, y_length=3.1)
        curve = axes.plot(lambda t: 1.0 + 0.7 * t, x_range=[0, 4], color=HIGHLIGHT, stroke_width=5)

        dx = 0.55
        rects = VGroup()
        for index in range(7):
            x0 = index * dx
            height = 1.0 + 0.7 * x0
            width = axes.c2p(x0 + dx, 0)[0] - axes.c2p(x0, 0)[0]
            rect = Rectangle(
                width=width,
                height=axes.c2p(0, height)[1] - axes.c2p(0, 0)[1],
                stroke_color=ACCENT,
                stroke_width=2,
                fill_color=ACCENT_SOFT,
                fill_opacity=0.35,
            )
            rect.move_to((axes.c2p(x0, 0) + axes.c2p(x0 + dx, height)) / 2)
            rects.add(rect)

        message = make_info_box(
            "Acumular no tempo =",
            "somar muitas pequenas",
            "contribuicoes de area.",
            "No fim, aparece Delta x.",
            font_size=22,
            highlight_last=True,
        ).to_corner(UP + RIGHT).shift(DOWN * 1.0 + LEFT * 0.4)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(FadeIn(axes_group))
        self.play(Create(curve))
        self.play(FadeIn(rects))
        self.play(FadeIn(message, shift=LEFT * 0.1))
        self.play(Indicate(rects, color=HIGHLIGHT))
        self.wait(1.0)


class UniformAreaRectangleScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("MU: a area do retangulo explica a formula", font="DejaVu Serif", font_size=30, color=INK).to_edge(UP).shift(DOWN * 0.2)

        axes_group, axes = make_stage_axes(DOWN * 0.15, "v(t)", [0, 4.6, 1], x_length=6.3, y_length=3.2)
        v_line = axes.plot(lambda t: 3.0, x_range=[0, 4], color=HIGHLIGHT, stroke_width=5)
        area = make_axis_polygon(axes, [(0, 0), (4, 0), (4, 3), (0, 3)])

        base_badge = make_badge("base = t", font_size=22).move_to(axes.c2p(2.0, -0.55))
        height_badge = make_badge("altura = v", font_size=22).move_to(axes.c2p(-0.45, 1.55))
        formula = make_info_box(
            "Delta x = area",
            "Delta x = v * t",
            "x = x0 + vt",
            font_size=22,
            highlight_last=True,
        ).to_corner(UP + RIGHT).shift(DOWN * 0.95 + LEFT * 0.45)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(FadeIn(axes_group))
        self.play(Create(v_line))
        self.play(FadeIn(area))
        self.play(FadeIn(base_badge), FadeIn(height_badge))
        self.play(FadeIn(formula, shift=LEFT * 0.1))
        self.play(Indicate(formula[1][-1], color=HIGHLIGHT))
        self.wait(1.0)


class AcceleratedAreaDecompositionScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("MUV: o trapezio se divide em duas partes", font="DejaVu Serif", font_size=30, color=INK).to_edge(UP).shift(DOWN * 0.2)

        axes_group, axes = make_stage_axes(DOWN * 0.12, "v(t)", [0, 5.8, 1], x_length=6.3, y_length=3.2)
        v_line = axes.plot(lambda t: 1.2 + 0.8 * t, x_range=[0, 4], color=HIGHLIGHT, stroke_width=5)
        rect = make_axis_polygon(axes, [(0, 0), (4, 0), (4, 1.2), (0, 1.2)])
        tri = make_axis_polygon(
            axes,
            [(0, 1.2), (4, 1.2), (4, 4.4)],
            fill_color=SOFT_BLUE,
            stroke_color=HIGHLIGHT,
            fill_opacity=0.45,
        )

        v0_tag = make_badge("v0", font_size=20).move_to(axes.c2p(-0.25, 1.2))
        top_tag = make_badge("v0 + at", font_size=20).move_to(axes.c2p(4.35, 4.4))
        formula = make_info_box(
            "A1 = v0 * t",
            "A2 = (1/2) * a * t^2",
            "x = x0 + A1 + A2",
            font_size=22,
            highlight_last=True,
        ).to_corner(UP + RIGHT).shift(DOWN * 0.92 + LEFT * 0.42)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(FadeIn(axes_group))
        self.play(Create(v_line))
        self.play(FadeIn(v0_tag), FadeIn(top_tag))
        self.play(FadeIn(rect))
        self.play(FadeIn(tri))
        self.play(FadeIn(formula, shift=LEFT * 0.1))
        self.play(Indicate(tri, color=HIGHLIGHT), Indicate(formula[1][-1], color=HIGHLIGHT))
        self.wait(1.0)


class AverageVelocityAreaScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("MUV: o trapezio vira um retangulo medio", font="DejaVu Serif", font_size=30, color=INK).to_edge(UP).shift(DOWN * 0.2)

        left_group, left_axes = make_stage_axes(LEFT * 3.2 + DOWN * 0.15, "v(t)", [0, 5.8, 1], x_length=4.2, y_length=2.8)
        right_group, right_axes = make_stage_axes(RIGHT * 3.2 + DOWN * 0.15, "v(t)", [0, 5.8, 1], x_length=4.2, y_length=2.8)

        trap = make_axis_polygon(left_axes, [(0, 0), (4, 0), (4, 4.4), (0, 1.2)])
        top_line = left_axes.plot(lambda t: 1.2 + 0.8 * t, x_range=[0, 4], color=HIGHLIGHT, stroke_width=5)
        rect = make_axis_polygon(
            right_axes,
            [(0, 0), (4, 0), (4, 2.8), (0, 2.8)],
            fill_color=SOFT_BLUE,
            stroke_color=HIGHLIGHT,
            fill_opacity=0.45,
        )

        avg_line = right_axes.plot(lambda t: 2.8, x_range=[0, 4], color=HIGHLIGHT, stroke_width=5)
        left_tag = make_badge("mesma base t", font_size=20).move_to(left_axes.c2p(2.0, -0.52))
        right_tag = make_badge("altura = v_med", font_size=20).move_to(right_axes.c2p(2.0, 3.5))
        formula = make_info_box(
            "Mesma area total",
            "Delta x = v_med * t",
            "v_med = (v0 + v) / 2",
            font_size=22,
            highlight_last=True,
        ).to_edge(DOWN).shift(UP * 0.72)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(FadeIn(left_group), FadeIn(right_group))
        self.play(FadeIn(trap), Create(top_line))
        self.play(FadeIn(rect), Create(avg_line))
        self.play(FadeIn(left_tag), FadeIn(right_tag))
        self.play(FadeIn(formula, shift=UP * 0.08))
        self.play(Indicate(rect, color=HIGHLIGHT), Indicate(formula[1][-1], color=HIGHLIGHT))
        self.wait(1.0)


class FormalIntegralBridgeScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("Integral formal: mesma ideia, notacao mais compacta", font="DejaVu Serif", font_size=29, color=INK).to_edge(UP).shift(DOWN * 0.2)

        top_group, top_axes = make_stage_axes(LEFT * 3.0 + DOWN * 0.1, "v(t)", [0, 5.6, 1], x_length=4.4, y_length=2.8)
        bottom_group, bottom_axes = make_stage_axes(RIGHT * 3.0 + DOWN * 0.1, "a(t)", [0, 3.6, 1], x_length=4.4, y_length=2.8)

        v_curve = top_axes.plot(lambda t: 1.0 + 0.9 * t, x_range=[0, 4], color=HIGHLIGHT, stroke_width=5)
        v_area = make_axis_polygon(top_axes, [(0, 0), (4, 0), (4, 4.6), (0, 1.0)])
        a_line = bottom_axes.plot(lambda t: 2.0, x_range=[0, 4], color=HIGHLIGHT, stroke_width=5)
        a_area = make_axis_polygon(
            bottom_axes,
            [(0, 0), (4, 0), (4, 2.0), (0, 2.0)],
            fill_color=SOFT_BLUE,
            stroke_color=HIGHLIGHT,
            fill_opacity=0.45,
        )

        top_box = make_info_box(
            "Acumular v(t) no intervalo",
            "produz Delta x.",
            font_size=21,
            highlight_last=True,
        ).next_to(top_group, DOWN, buff=0.38)
        bottom_box = make_info_box(
            "Acumular a(t) no intervalo",
            "produz Delta v.",
            font_size=21,
            highlight_last=True,
        ).next_to(bottom_group, DOWN, buff=0.38)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(FadeIn(top_group), FadeIn(bottom_group))
        self.play(Create(v_curve), Create(a_line))
        self.play(FadeIn(v_area), FadeIn(a_area))
        self.play(FadeIn(top_box, shift=UP * 0.08), FadeIn(bottom_box, shift=UP * 0.08))
        self.play(Indicate(v_area, color=HIGHLIGHT), Indicate(a_area, color=HIGHLIGHT))
        self.wait(1.0)


class UniformDerivativeBridgeScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("MU: derivar a reta devolve sua inclinacao", font="DejaVu Serif", font_size=30, color=INK).to_edge(UP).shift(DOWN * 0.2)

        left_group, left_axes = make_stage_axes(LEFT * 3.2 + DOWN * 0.15, "x(t)", [0, 5.8, 1], x_length=4.2, y_length=2.8)
        right_group, right_axes = make_stage_axes(RIGHT * 3.2 + DOWN * 0.15, "v(t)", [0, 4.8, 1], x_length=4.2, y_length=2.8)

        x_line = left_axes.plot(lambda t: 1.0 + 0.95 * t, x_range=[0, 4], color=HIGHLIGHT, stroke_width=5)
        v_line = right_axes.plot(lambda t: 0.95, x_range=[0, 4], color=HIGHLIGHT, stroke_width=5)
        bridge = Arrow(LEFT * 1.0, RIGHT * 1.0, buff=0.1, color=ACCENT, stroke_width=4).move_to(UP * 0.1)
        bridge_label = Text("derivar", font="DejaVu Sans", font_size=22, color=ACCENT).next_to(bridge, UP, buff=0.08)
        left_box = make_info_box("x(t) e reta", "inclinacao = v", font_size=22, highlight_last=True).next_to(left_group, DOWN, buff=0.35)
        right_box = make_info_box("v(t) fica constante", "mesma inclinacao em todo ponto", font_size=20, highlight_last=True).next_to(right_group, DOWN, buff=0.35)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(FadeIn(left_group), Create(x_line))
        self.play(FadeIn(left_box, shift=UP * 0.08))
        self.play(Create(bridge), FadeIn(bridge_label, shift=DOWN * 0.05))
        self.play(FadeIn(right_group), Create(v_line))
        self.play(FadeIn(right_box, shift=UP * 0.08))
        self.play(Indicate(x_line, color=HIGHLIGHT), Indicate(v_line, color=HIGHLIGHT))
        self.wait(1.0)


class AcceleratedDerivativeCascadeScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("MUV: a derivada cria uma cascata", font="DejaVu Serif", font_size=30, color=INK).to_edge(UP).shift(DOWN * 0.2)

        centers = [LEFT * 4.4 + DOWN * 0.1, DOWN * 0.1, RIGHT * 4.4 + DOWN * 0.1]
        panels = VGroup()
        curves = VGroup()
        boxes = VGroup()

        specs = [
            ("x(t)", [0, 6.4, 1], lambda t: 0.38 * t * t + 0.6 * t + 0.8, "quadratica"),
            ("v(t)", [0, 5.2, 1], lambda t: 0.6 + 0.76 * t, "linear"),
            ("a(t)", [0, 2.4, 1], lambda t: 0.76, "constante"),
        ]

        for center, (label, y_range, func, kind) in zip(centers, specs):
            panel, axes = make_stage_axes(center, label, y_range, x_length=2.6, y_length=1.8)
            graph = axes.plot(func, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
            box = make_badge(kind, font_size=20).next_to(panel, DOWN, buff=0.32)
            panels.add(panel)
            curves.add(graph)
            boxes.add(box)

        arrow_1 = Arrow(LEFT * 2.6 + UP * 0.1, LEFT * 1.6 + UP * 0.1, buff=0.08, color=ACCENT, stroke_width=4)
        arrow_2 = Arrow(RIGHT * 1.6 + UP * 0.1, RIGHT * 2.6 + UP * 0.1, buff=0.08, color=ACCENT, stroke_width=4)
        label_1 = Text("derivar", font="DejaVu Sans", font_size=20, color=ACCENT).next_to(arrow_1, UP, buff=0.06)
        label_2 = Text("derivar", font="DejaVu Sans", font_size=20, color=ACCENT).next_to(arrow_2, UP, buff=0.06)
        footer = make_info_box("x(t) -> v(t) -> a(t)", "cada derivada simplifica um nivel", font_size=21, highlight_last=True).to_edge(DOWN).shift(UP * 0.72)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        for panel, graph, box in zip(panels, curves, boxes):
            self.play(FadeIn(panel), Create(graph), FadeIn(box, shift=UP * 0.06))
        self.play(Create(arrow_1), FadeIn(label_1), Create(arrow_2), FadeIn(label_2))
        self.play(FadeIn(footer, shift=UP * 0.08))
        self.play(Indicate(curves[0], color=HIGHLIGHT), Indicate(curves[1], color=HIGHLIGHT), Indicate(curves[2], color=HIGHLIGHT))
        self.wait(1.0)


class FundamentalTheoremKinematicsScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("Derivar mede taxa, integrar recompõe acumulos", font="DejaVu Serif", font_size=29, color=INK).to_edge(UP).shift(DOWN * 0.2)

        x_card = make_info_box("x(t)", "posicao", font_size=26, highlight_last=True).move_to(LEFT * 4.2 + UP * 0.2)
        v_card = make_info_box("v(t)", "velocidade", font_size=26, highlight_last=True).move_to(UP * 0.2)
        a_card = make_info_box("a(t)", "aceleracao", font_size=26, highlight_last=True).move_to(RIGHT * 4.2 + UP * 0.2)

        dv_arrow = Arrow(x_card.get_right() + RIGHT * 0.12, v_card.get_left() + LEFT * 0.12, buff=0.08, color=ACCENT, stroke_width=4)
        da_arrow = Arrow(v_card.get_right() + RIGHT * 0.12, a_card.get_left() + LEFT * 0.12, buff=0.08, color=ACCENT, stroke_width=4)
        int_v_arrow = Arrow(a_card.get_bottom() + DOWN * 0.72, v_card.get_bottom() + DOWN * 0.72, buff=0.08, color=HIGHLIGHT, stroke_width=4)
        int_x_arrow = Arrow(v_card.get_bottom() + DOWN * 0.72, x_card.get_bottom() + DOWN * 0.72, buff=0.08, color=HIGHLIGHT, stroke_width=4)

        dv_label = Text("derivar", font="DejaVu Sans", font_size=20, color=ACCENT).next_to(dv_arrow, UP, buff=0.06)
        da_label = Text("derivar", font="DejaVu Sans", font_size=20, color=ACCENT).next_to(da_arrow, UP, buff=0.06)
        int_v_label = Text("integrar / acumular", font="DejaVu Sans", font_size=18, color=HIGHLIGHT).next_to(int_v_arrow, DOWN, buff=0.08)
        int_x_label = Text("integrar / acumular", font="DejaVu Sans", font_size=18, color=HIGHLIGHT).next_to(int_x_arrow, DOWN, buff=0.08)

        bottom_box = make_info_box(
            "As setas de cima leem inclinacao.",
            "As setas de baixo recompõem area e acumulo.",
            font_size=21,
            highlight_last=True,
        ).to_edge(DOWN).shift(UP * 0.78)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(FadeIn(x_card), FadeIn(v_card), FadeIn(a_card))
        self.play(Create(dv_arrow), FadeIn(dv_label), Create(da_arrow), FadeIn(da_label))
        self.play(Create(int_v_arrow), FadeIn(int_v_label), Create(int_x_arrow), FadeIn(int_x_label))
        self.play(FadeIn(bottom_box, shift=UP * 0.08))
        self.play(Indicate(v_card[1][1], color=HIGHLIGHT), Indicate(a_card[1][1], color=HIGHLIGHT))
        self.wait(1.0)


class FormulaMapOverviewScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("MU e MUV como mapa de formulas e graficos", font="DejaVu Serif", font_size=29, color=INK).to_edge(UP).shift(DOWN * 0.2)

        mu_card = make_info_box(
            "MU",
            "x = x0 + vt",
            "v = constante",
            font_size=24,
            highlight_last=True,
        ).move_to(LEFT * 3.4 + DOWN * 0.1)
        muv_card = make_info_box(
            "MUV",
            "v = v0 + at",
            "x = x0 + v0 t + (1/2) a t^2",
            font_size=21,
            highlight_last=True,
        ).move_to(RIGHT * 3.4 + DOWN * 0.1)

        mu_panel, mu_axes = make_stage_axes(LEFT * 3.4 + DOWN * 2.0, "x(t)", [0, 4.8, 1], x_length=3.2, y_length=1.8)
        muv_panel, muv_axes = make_stage_axes(RIGHT * 3.4 + DOWN * 2.0, "x(t)", [0, 6.0, 1], x_length=3.2, y_length=1.8)
        mu_graph = mu_axes.plot(lambda t: 0.9 + 0.8 * t, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
        muv_graph = muv_axes.plot(lambda t: 0.45 * t * t + 0.5, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
        footer = make_info_box(
            "MU = reta e velocidade fixa.",
            "MUV = curvatura na posicao e reta na velocidade.",
            font_size=20,
            highlight_last=True,
        ).to_edge(DOWN).shift(UP * 0.62)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(FadeIn(mu_card, shift=UP * 0.08), FadeIn(muv_card, shift=UP * 0.08))
        self.play(FadeIn(mu_panel), Create(mu_graph), FadeIn(muv_panel), Create(muv_graph))
        self.play(FadeIn(footer, shift=UP * 0.08))
        self.play(Indicate(mu_graph, color=HIGHLIGHT), Indicate(muv_graph, color=HIGHLIGHT))
        self.wait(1.0)


class TrafficLightLaunchScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("Exemplo: carro saindo do semaforo", font="DejaVu Serif", font_size=31, color=INK).to_edge(UP).shift(DOWN * 0.2)

        track, axis_point = make_track(left_edge=5.6, right_edge=5.2, y=1.2, max_value=80)
        axis, ticks, labels, axis_label = track
        traffic_light = make_traffic_light(0.78).move_to(axis_point(2) + UP * 1.25 + LEFT * 0.9)

        positions = [0, 13, 36, 69]
        car = make_car(0.68).move_to(axis_point(positions[0]) + UP * 0.44)
        markers = VGroup()
        gap_tags = VGroup()
        for index, value in enumerate(positions):
            marker = Line(axis_point(value) + DOWN * 0.2, axis_point(value) + UP * 0.46, color=HIGHLIGHT, stroke_width=4)
            tag = Text(f"t = {2*index} s", font="DejaVu Sans", font_size=18, color=INK).next_to(marker, UP, buff=0.08)
            markers.add(VGroup(marker, tag))
        for left, right, label in zip(positions, positions[1:], ["+13 m", "+23 m", "+33 m"]):
            gap_tags.add(make_badge(label, font_size=20).move_to((axis_point(left) + axis_point(right)) / 2 + DOWN * 0.65))

        info = make_info_box(
            "v0 = 4 m/s",
            "a = 2.5 m/s^2",
            "apos 6 s: v = 19 m/s",
            "Delta x = 69 m",
            font_size=22,
            highlight_last=True,
        ).to_corner(UP + RIGHT).shift(DOWN * 0.95 + LEFT * 0.45)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(Create(axis), FadeIn(axis_label), FadeIn(ticks), FadeIn(labels))
        self.play(FadeIn(traffic_light, shift=DOWN * 0.1))
        self.play(FadeIn(markers[0]), FadeIn(car, shift=LEFT * 0.08), FadeIn(info, shift=LEFT * 0.1))
        for index, value in enumerate(positions[1:], start=1):
            self.play(
                car.animate.move_to(axis_point(value) + UP * 0.44),
                FadeIn(markers[index]),
                FadeIn(gap_tags[index - 1]),
                run_time=0.85,
                rate_func=linear,
            )
        self.play(Indicate(info[1][-1], color=HIGHLIGHT), Indicate(gap_tags[-1], color=HIGHLIGHT))
        self.wait(1.0)


class EngineeringGraphReadingScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text("Leitura de engenharia: valor, inclinacao e area", font="DejaVu Serif", font_size=29, color=INK).to_edge(UP).shift(DOWN * 0.2)

        x_group, x_axes = make_stage_axes(LEFT * 4.1 + DOWN * 0.2, "x(t)", [0, 5.6, 1], x_length=2.8, y_length=2.0)
        v_group, v_axes = make_stage_axes(DOWN * 0.2, "v(t)", [0, 5.6, 1], x_length=2.8, y_length=2.0)
        a_group, a_axes = make_stage_axes(RIGHT * 4.1 + DOWN * 0.2, "a(t)", [0, 3.2, 1], x_length=2.8, y_length=2.0)

        x_graph = x_axes.plot(lambda t: 0.8 + 0.9 * t, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
        v_graph = v_axes.plot(lambda t: 1.2 + 0.8 * t, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
        v_area = make_axis_polygon(v_axes, [(0, 0), (3, 0), (3, 3.6), (0, 1.2)], fill_color=ACCENT_SOFT, fill_opacity=0.3)
        a_graph = a_axes.plot(lambda t: 1.5, x_range=[0, 3], color=HIGHLIGHT, stroke_width=5)
        a_area = make_axis_polygon(a_axes, [(0, 0), (3, 0), (3, 1.5), (0, 1.5)], fill_color=SOFT_BLUE, fill_opacity=0.35, stroke_color=HIGHLIGHT)

        x_box = make_info_box("no x(t):", "inclinacao = velocidade", font_size=18, highlight_last=True).next_to(x_group, DOWN, buff=0.3)
        v_box = make_info_box("no v(t):", "valor = velocidade", "area = Delta x", font_size=18, highlight_last=True).next_to(v_group, DOWN, buff=0.3)
        a_box = make_info_box("no a(t):", "valor = aceleracao", "area = Delta v", font_size=18, highlight_last=True).next_to(a_group, DOWN, buff=0.3)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(FadeIn(x_group), Create(x_graph))
        self.play(FadeIn(v_group), Create(v_graph), FadeIn(v_area))
        self.play(FadeIn(a_group), Create(a_graph), FadeIn(a_area))
        self.play(FadeIn(x_box, shift=UP * 0.06), FadeIn(v_box, shift=UP * 0.06), FadeIn(a_box, shift=UP * 0.06))
        self.play(Indicate(v_area, color=HIGHLIGHT), Indicate(a_area, color=HIGHLIGHT))
        self.wait(1.0)
