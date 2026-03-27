from __future__ import annotations

import sys
from pathlib import Path

from manim import (
    Axes,
    Create,
    DashedLine,
    Dot,
    DOWN,
    FadeIn,
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


THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from book_motion import (  # noqa: E402
    ACCENT,
    ACCENT_SOFT,
    CARD_FILL,
    CARD_FILL_ALT,
    HIGHLIGHT,
    INK,
    MUTED,
    NEGATIVE,
    NEGATIVE_SOFT,
    PAPER,
    SOFT_BLUE,
    make_badge,
    make_car,
    make_track,
)
from recipes.composition_recipes import (  # noqa: E402
    chained_sequence,
    layered_parallel,
    staggered_reveal,
)
from recipes.highlight_recipes import outline_focus, pulse_focus, spark_point  # noqa: E402
from recipes.motion_recipes import make_motion_trail  # noqa: E402
from recipes.tracker_recipes import make_tangent_probe, make_tracked_text  # noqa: E402
from recipes.transform_recipes import duplicate_into  # noqa: E402


X_COLOR = ACCENT
V_COLOR = HIGHLIGHT
A_COLOR = NEGATIVE


def make_axes_panel(
    title: str,
    center,
    x_range: list[float],
    y_range: list[float],
    x_length: float = 3.2,
    y_length: float = 1.95,
    title_color: str = INK,
) -> tuple[VGroup, Axes]:
    frame = RoundedRectangle(
        corner_radius=0.2,
        width=x_length + 0.9,
        height=y_length + 1.0,
        stroke_color=ACCENT_SOFT,
        stroke_width=2.4,
        fill_color=CARD_FILL,
        fill_opacity=1,
    ).move_to(center)
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        tips=False,
        axis_config={"color": ACCENT, "stroke_width": 2.6, "include_ticks": False},
    ).move_to(frame.get_center() + DOWN * 0.12)
    title_text = Text(title, font="DejaVu Sans", font_size=20, color=title_color, weight="BOLD")
    title_text.move_to(frame.get_top() + DOWN * 0.24)
    x_label = Text("t", font="DejaVu Sans", font_size=16, color=MUTED).next_to(axes, RIGHT, buff=0.08)
    return VGroup(frame, axes, title_text, x_label), axes


def make_cursor_line(axes: Axes, x_value: float, y_value: float, color: str = MUTED) -> DashedLine:
    return DashedLine(
        axes.c2p(x_value, 0),
        axes.c2p(x_value, y_value),
        color=color,
        dash_length=0.09,
        stroke_width=2.2,
    )


def make_rectangles(
    axes: Axes,
    func,
    x_start: float,
    x_end: float,
    count: int,
    sample: str = "mid",
    positive_fill: str = ACCENT_SOFT,
    positive_stroke: str = ACCENT,
    negative_fill: str = NEGATIVE_SOFT,
    negative_stroke: str = NEGATIVE,
    fill_opacity: float = 0.32,
    stroke_width: float = 1.8,
) -> VGroup:
    if x_end <= x_start:
        return VGroup()

    dx = (x_end - x_start) / count
    sample_offset = {"left": 0.0, "mid": 0.5, "right": 1.0}[sample]
    rectangles = VGroup()

    for index in range(count):
        left = x_start + index * dx
        right = left + dx
        probe = left + sample_offset * dx
        height = func(probe)
        fill_color = positive_fill if height >= 0 else negative_fill
        stroke_color = positive_stroke if height >= 0 else negative_stroke
        rectangles.add(
            Polygon(
                axes.c2p(left, 0),
                axes.c2p(right, 0),
                axes.c2p(right, height),
                axes.c2p(left, height),
                fill_color=fill_color,
                fill_opacity=fill_opacity,
                stroke_color=stroke_color,
                stroke_width=stroke_width,
            )
        )
    return rectangles


def current_time(alpha: float, duration: float = 5.0) -> float:
    return duration * alpha


def general_velocity(t: float) -> float:
    return 0.18 * (t - 0.6) * (t - 2.5) * (t - 4.4)


def general_velocity_prime(t: float) -> float:
    return 0.18 * ((t - 2.5) * (t - 4.4) + (t - 0.6) * (t - 4.4) + (t - 0.6) * (t - 2.5))


def general_velocity_area(t: float) -> float:
    return 0.18 * (0.25 * t**4 - 2.5 * t**3 + 7.57 * t**2 - 6.6 * t)


def theorem_velocity(t: float) -> float:
    return 0.44 * t + 0.3


def theorem_position(t: float) -> float:
    return 0.22 * t * t + 0.3 * t + 0.9


def theorem_displacement_from_one(t: float) -> float:
    return 0.22 * (t * t - 1.0) + 0.3 * (t - 1.0)


def engineering_velocity(t: float) -> float:
    return 1.0 + 0.55 * t - 0.08 * t * t


def engineering_acceleration(t: float) -> float:
    return 0.55 - 0.16 * t


def engineering_displacement(t: float) -> float:
    return t + 0.275 * t * t - (0.08 / 3.0) * t**3


class KinematicsTimeSweepScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text(
            "O mesmo instante aparece em tres retratos",
            font="DejaVu Serif",
            font_size=28,
            color=INK,
        ).to_edge(UP).shift(DOWN * 0.22)

        tracker = ValueTracker(0.0)

        def x_func(t: float) -> float:
            return 2.0 + 4.0 * t + 1.2 * t * t

        def v_func(t: float) -> float:
            return 4.0 + 2.4 * t

        def a_func(_: float) -> float:
            return 2.4

        x_panel, x_axes = make_axes_panel("x(t)", LEFT * 4.2 + UP * 1.45, [0, 4, 1], [0, 40, 10], title_color=X_COLOR)
        v_panel, v_axes = make_axes_panel("v(t)", UP * 1.45, [0, 4, 1], [0, 15, 5], title_color=V_COLOR)
        a_panel, a_axes = make_axes_panel("a(t)", RIGHT * 4.2 + UP * 1.45, [0, 4, 1], [0, 4, 1], title_color=A_COLOR)

        x_curve = x_axes.plot(x_func, x_range=[0, 4], color=X_COLOR, stroke_width=4.5)
        v_curve = v_axes.plot(v_func, x_range=[0, 4], color=V_COLOR, stroke_width=4.5)
        a_curve = a_axes.plot(a_func, x_range=[0, 4], color=A_COLOR, stroke_width=4.5)

        x_probe = always_redraw(lambda: Dot(x_axes.c2p(tracker.get_value(), x_func(tracker.get_value())), radius=0.07, color=X_COLOR))
        v_probe = always_redraw(lambda: Dot(v_axes.c2p(tracker.get_value(), v_func(tracker.get_value())), radius=0.07, color=V_COLOR))
        a_probe = always_redraw(lambda: Dot(a_axes.c2p(tracker.get_value(), a_func(tracker.get_value())), radius=0.07, color=A_COLOR))

        x_cursor = always_redraw(lambda: make_cursor_line(x_axes, tracker.get_value(), x_func(tracker.get_value())))
        v_cursor = always_redraw(lambda: make_cursor_line(v_axes, tracker.get_value(), v_func(tracker.get_value())))
        a_cursor = always_redraw(lambda: make_cursor_line(a_axes, tracker.get_value(), a_func(tracker.get_value())))

        time_badge = always_redraw(
            lambda: make_badge(
                f"t = {tracker.get_value():.1f} s",
                font_size=20,
                color=INK,
            ).move_to(UP * 2.9)
        )
        x_badge = always_redraw(
            lambda: make_badge(
                f"x = {x_func(tracker.get_value()):.1f} m",
                font_size=17,
                color=X_COLOR,
            ).move_to(x_panel.get_bottom() + DOWN * 0.36)
        )
        v_badge = always_redraw(
            lambda: make_badge(
                f"v = {v_func(tracker.get_value()):.1f} m/s",
                font_size=17,
                color=V_COLOR,
            ).move_to(v_panel.get_bottom() + DOWN * 0.36)
        )
        a_badge = always_redraw(
            lambda: make_badge(
                f"a = {a_func(tracker.get_value()):.1f} m/s^2",
                font_size=17,
                color=A_COLOR,
            ).move_to(a_panel.get_bottom() + DOWN * 0.36)
        )

        track_group, axis_point = make_track(left_edge=5.7, right_edge=5.5, y=3.18, max_value=40, tick_step=10)
        axis, ticks, labels, axis_label = track_group
        car_shape = make_car(0.66)
        car = always_redraw(lambda: car_shape.copy().move_to(axis_point(x_func(tracker.get_value())) + UP * 0.42))
        trail = make_motion_trail(car, color=V_COLOR, stroke_width=3)

        closing = make_badge("um mesmo t produz tres pontos e um estado do movimento", font_size=18, color=INK).move_to(DOWN * 1.18)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.8)
        self.play(staggered_reveal(x_panel, v_panel, a_panel, lag_ratio=0.14, run_time=1.6))
        self.play(
            layered_parallel(Create(x_curve), Create(v_curve), Create(a_curve), run_time=1.4),
        )
        self.play(FadeIn(time_badge, shift=UP * 0.08), FadeIn(x_badge), FadeIn(v_badge), FadeIn(a_badge), run_time=0.8)
        self.play(Create(axis), FadeIn(ticks), FadeIn(labels), FadeIn(axis_label), run_time=1.0)
        self.add(trail)
        self.play(FadeIn(car, shift=LEFT * 0.1), FadeIn(x_probe), FadeIn(v_probe), FadeIn(a_probe), FadeIn(x_cursor), FadeIn(v_cursor), FadeIn(a_cursor), run_time=0.9)
        self.play(chained_sequence(outline_focus(x_panel[0]), outline_focus(v_panel[0]), outline_focus(a_panel[0]), run_time=2.6))
        self.play(tracker.animate.set_value(4.0), run_time=7.2, rate_func=linear)
        self.play(FadeIn(closing, shift=UP * 0.08), run_time=0.8)
        self.play(pulse_focus(x_probe), pulse_focus(v_probe), pulse_focus(a_probe), run_time=0.8)
        self.wait(1.0)


class CalculusTriptychScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text(
            "Limite, derivada e integral em um mesmo palco",
            font="DejaVu Serif",
            font_size=28,
            color=INK,
        ).to_edge(UP).shift(DOWN * 0.22)

        def base_func(t: float) -> float:
            return 0.18 * t * t + 0.24 * t + 0.7

        left_panel, left_axes = make_axes_panel("limite", LEFT * 4.35 + UP * 0.65, [0, 4.5, 1], [0, 5.5, 1], x_length=2.8, y_length=1.9)
        mid_panel, mid_axes = make_axes_panel("derivada", UP * 0.65, [0, 4.5, 1], [0, 5.5, 1], x_length=2.8, y_length=1.9)
        right_panel, right_axes = make_axes_panel("integral", RIGHT * 4.35 + UP * 0.65, [0, 4.5, 1], [0, 5.5, 1], x_length=2.8, y_length=1.9)

        left_curve = left_axes.plot(base_func, x_range=[0, 4.2], color=V_COLOR, stroke_width=4.4)
        mid_curve = mid_axes.plot(base_func, x_range=[0, 4.2], color=V_COLOR, stroke_width=4.4)
        right_curve = right_axes.plot(base_func, x_range=[0, 4.2], color=V_COLOR, stroke_width=4.4)

        h_tracker = ValueTracker(1.25)
        left_t0 = 1.8
        left_point_a = always_redraw(lambda: Dot(left_axes.c2p(left_t0, base_func(left_t0)), radius=0.07, color=X_COLOR))
        left_point_b = always_redraw(
            lambda: Dot(
                left_axes.c2p(left_t0 + h_tracker.get_value(), base_func(left_t0 + h_tracker.get_value())),
                radius=0.07,
                color=HIGHLIGHT,
            )
        )
        secant = always_redraw(
            lambda: Line(
                left_axes.c2p(left_t0, base_func(left_t0)),
                left_axes.c2p(left_t0 + h_tracker.get_value(), base_func(left_t0 + h_tracker.get_value())),
                color=INK,
                stroke_width=3.2,
            )
        )
        limit_badge = make_badge("Delta t -> 0", font_size=17, color=X_COLOR).move_to(left_panel.get_bottom() + DOWN * 0.34)

        alpha_tracker = ValueTracker(0.45)
        tangent_probe = make_tangent_probe(mid_curve, alpha_tracker, point_color=X_COLOR, tangent_color=INK, line_length=2.2)
        derivative_badge = make_badge("df/dt", font_size=17, color=V_COLOR).move_to(mid_panel.get_bottom() + DOWN * 0.34)

        rect4 = make_rectangles(right_axes, base_func, 0.0, 4.0, 4)
        rect8 = make_rectangles(right_axes, base_func, 0.0, 4.0, 8)
        rect16 = make_rectangles(right_axes, base_func, 0.0, 4.0, 16)
        integral_badge = make_badge("int f(t) dt", font_size=17, color=A_COLOR).move_to(right_panel.get_bottom() + DOWN * 0.34)
        closing = make_badge("limite aproxima, derivada mede, integral acumula", font_size=18, color=INK).move_to(DOWN * 2.48)

        self.play(FadeIn(title, shift=DOWN * 0.08), run_time=0.8)
        self.play(staggered_reveal(left_panel, mid_panel, right_panel, lag_ratio=0.14, run_time=1.6))
        self.play(layered_parallel(Create(left_curve), Create(mid_curve), Create(right_curve), run_time=1.35))

        self.play(FadeIn(left_point_a), FadeIn(left_point_b), FadeIn(secant), FadeIn(limit_badge), run_time=0.8)
        self.play(outline_focus(left_panel[0]), run_time=0.9)
        self.play(h_tracker.animate.set_value(0.18), run_time=2.2, rate_func=smooth)
        self.play(spark_point(left_point_a), pulse_focus(left_point_b), run_time=0.8)

        self.play(duplicate_into(limit_badge, derivative_badge), FadeIn(tangent_probe), run_time=0.95)
        self.play(outline_focus(mid_panel[0]), run_time=0.8)
        self.play(alpha_tracker.animate.set_value(0.72), run_time=2.0, rate_func=smooth)
        self.play(pulse_focus(tangent_probe[0]), run_time=0.75)

        self.play(duplicate_into(derivative_badge, integral_badge), FadeIn(rect4), run_time=0.95)
        self.play(outline_focus(right_panel[0]), run_time=0.8)
        self.play(Transform(rect4, rect8), run_time=1.0)
        self.play(Transform(rect4, rect16), run_time=1.0)
        self.play(FadeIn(closing, shift=UP * 0.08), run_time=0.8)
        self.wait(1.0)


class GeneralCurveDashboardScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text(
            "Em uma curva qualquer, ainda lemos valor, inclinacao e area",
            font="DejaVu Serif",
            font_size=27,
            color=INK,
        ).to_edge(UP).shift(DOWN * 0.2)

        panel, axes = make_axes_panel(
            "v(t) geral",
            LEFT * 1.8 + UP * 0.4,
            [0, 5, 1],
            [-1.6, 1.6, 0.8],
            x_length=6.1,
            y_length=3.3,
            title_color=V_COLOR,
        )
        curve = axes.plot(general_velocity, x_range=[0, 5], color=V_COLOR, stroke_width=4.8)

        alpha_tracker = ValueTracker(0.18)
        point_and_tangent = make_tangent_probe(curve, alpha_tracker, point_color=X_COLOR, tangent_color=INK, line_length=2.8)
        point = point_and_tangent[1]
        tangent = point_and_tangent[0]
        cursor = always_redraw(
            lambda: make_cursor_line(
                axes,
                current_time(alpha_tracker.get_value()),
                general_velocity(current_time(alpha_tracker.get_value())),
            )
        )
        rectangles = always_redraw(
            lambda: make_rectangles(
                axes,
                general_velocity,
                0.0,
                current_time(alpha_tracker.get_value()),
                22,
                sample="mid",
            )
        )

        dashboard = RoundedRectangle(
            corner_radius=0.2,
            width=4.15,
            height=3.4,
            stroke_color=ACCENT_SOFT,
            stroke_width=2.4,
            fill_color=CARD_FILL_ALT,
            fill_opacity=1,
        ).move_to(RIGHT * 4.35 + UP * 0.1)
        dashboard_title = Text("painel local", font="DejaVu Sans", font_size=22, color=INK, weight="BOLD").move_to(
            dashboard.get_top() + DOWN * 0.3
        )
        time_text = make_tracked_text(
            "t = ",
            alpha_tracker,
            formatter=lambda alpha: f"{current_time(alpha):.2f} s",
            font_size=22,
        ).move_to(dashboard.get_center() + UP * 0.72)
        value_text = make_tracked_text(
            "v(t) = ",
            alpha_tracker,
            formatter=lambda alpha: f"{general_velocity(current_time(alpha)):.2f}",
            font_size=22,
            color=V_COLOR,
        ).move_to(dashboard.get_center() + UP * 0.22)
        slope_text = make_tracked_text(
            "dv/dt = ",
            alpha_tracker,
            formatter=lambda alpha: f"{general_velocity_prime(current_time(alpha)):.2f}",
            font_size=22,
            color=X_COLOR,
        ).move_to(dashboard.get_center() + DOWN * 0.3)
        area_text = make_tracked_text(
            "A(0,t) = ",
            alpha_tracker,
            formatter=lambda alpha: f"{general_velocity_area(current_time(alpha)):.2f}",
            font_size=22,
            color=A_COLOR,
        ).move_to(dashboard.get_center() + DOWN * 0.82)

        area_badge = make_badge("area assinada = deslocamento", font_size=18, color=A_COLOR).move_to(DOWN * 2.72)

        self.play(FadeIn(title, shift=DOWN * 0.08), run_time=0.8)
        self.play(FadeIn(panel, shift=UP * 0.06), FadeIn(dashboard, shift=UP * 0.06), run_time=1.0)
        self.play(Create(curve), FadeIn(dashboard_title), run_time=1.0)
        self.play(FadeIn(time_text), FadeIn(value_text), FadeIn(slope_text), FadeIn(area_text), run_time=0.8)
        self.play(FadeIn(rectangles), FadeIn(cursor), FadeIn(point), FadeIn(tangent), run_time=0.8)
        self.play(alpha_tracker.animate.set_value(0.94), run_time=8.2, rate_func=linear)
        self.play(FadeIn(area_badge, shift=UP * 0.08), run_time=0.8)
        self.play(chained_sequence(outline_focus(dashboard), outline_focus(tangent), outline_focus(area_badge), run_time=2.4))
        self.wait(1.0)


class IntegralUnitsScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text(
            "A area muda de significado conforme o eixo vertical",
            font="DejaVu Serif",
            font_size=28,
            color=INK,
        ).to_edge(UP).shift(DOWN * 0.2)

        left_panel, left_axes = make_axes_panel("v x t", LEFT * 4.2 + UP * 0.6, [0, 4, 1], [0, 4, 1], title_color=V_COLOR)
        right_panel, right_axes = make_axes_panel("a x t", RIGHT * 4.2 + UP * 0.6, [0, 4, 1], [0, 2.5, 0.5], title_color=A_COLOR)

        v_line = left_axes.plot(lambda t: 3.0, x_range=[0, 3.2], color=V_COLOR, stroke_width=4.4)
        a_line = right_axes.plot(lambda t: 1.6, x_range=[0, 3.2], color=A_COLOR, stroke_width=4.4)

        v_rect = make_rectangles(left_axes, lambda _t: 3.0, 0.0, 3.2, 1, sample="left", positive_fill=SOFT_BLUE, positive_stroke=V_COLOR, fill_opacity=0.42, stroke_width=2.4)
        a_rect = make_rectangles(right_axes, lambda _t: 1.6, 0.0, 3.2, 1, sample="left", positive_fill=NEGATIVE_SOFT, positive_stroke=A_COLOR, fill_opacity=0.42, stroke_width=2.4)

        v_units = make_badge("(m/s) x s = m", font_size=18, color=V_COLOR).move_to(left_panel.get_bottom() + DOWN * 0.36)
        a_units = make_badge("(m/s^2) x s = m/s", font_size=18, color=A_COLOR).move_to(right_panel.get_bottom() + DOWN * 0.36)
        v_result = make_badge("resultado: deslocamento", font_size=18, color=V_COLOR).move_to(DOWN * 2.38 + LEFT * 3.1)
        a_result = make_badge("resultado: Delta v", font_size=18, color=A_COLOR).move_to(DOWN * 2.38 + RIGHT * 3.1)
        closing = make_badge("a geometria e a unidade fisica contam a mesma historia", font_size=18, color=INK).move_to(DOWN * 3.05)

        self.play(FadeIn(title, shift=DOWN * 0.08), run_time=0.8)
        self.play(staggered_reveal(left_panel, right_panel, lag_ratio=0.16, run_time=1.4))
        self.play(layered_parallel(Create(v_line), Create(a_line), run_time=1.1))
        self.play(FadeIn(v_rect), FadeIn(a_rect), run_time=0.8)
        self.play(FadeIn(v_units), FadeIn(a_units), run_time=0.7)
        self.play(outline_focus(v_rect), outline_focus(a_rect), run_time=0.9)
        self.play(duplicate_into(v_rect, v_result), duplicate_into(a_rect, a_result), run_time=0.95)
        self.play(FadeIn(v_result), FadeIn(a_result), run_time=0.6)
        self.play(FadeIn(closing, shift=UP * 0.08), run_time=0.8)
        self.wait(1.0)


class FundamentalCycleScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text(
            "Taxa local e acumulo global fecham um ciclo",
            font="DejaVu Serif",
            font_size=28,
            color=INK,
        ).to_edge(UP).shift(DOWN * 0.2)

        x_panel, x_axes = make_axes_panel("x(t)", LEFT * 4.15 + UP * 0.45, [0, 4.5, 1], [0, 6, 1], x_length=3.05, y_length=2.15, title_color=X_COLOR)
        v_panel, v_axes = make_axes_panel("v(t)", RIGHT * 0.25 + UP * 0.95, [0, 4.5, 1], [0, 2.5, 0.5], x_length=3.45, y_length=2.1, title_color=V_COLOR)
        flow_box = RoundedRectangle(
            corner_radius=0.2,
            width=3.9,
            height=2.45,
            stroke_color=ACCENT_SOFT,
            stroke_width=2.2,
            fill_color=CARD_FILL_ALT,
            fill_opacity=1,
        ).move_to(RIGHT * 4.55 + DOWN * 1.55)
        flow_title = Text("fechamento", font="DejaVu Sans", font_size=22, color=INK, weight="BOLD").move_to(flow_box.get_top() + DOWN * 0.3)

        x_curve = x_axes.plot(theorem_position, x_range=[0, 4.2], color=X_COLOR, stroke_width=4.6)
        v_curve = v_axes.plot(theorem_velocity, x_range=[0, 4.2], color=V_COLOR, stroke_width=4.6)

        alpha_tracker = ValueTracker(0.3)
        tangent_probe = make_tangent_probe(x_curve, alpha_tracker, point_color=X_COLOR, tangent_color=INK, line_length=2.55)
        t_display = make_tracked_text(
            "t = ",
            alpha_tracker,
            formatter=lambda alpha: f"{current_time(alpha, 4.2):.2f} s",
            font_size=21,
        ).move_to(flow_box.get_center() + UP * 0.52)
        v_display = make_tracked_text(
            "dx/dt = ",
            alpha_tracker,
            formatter=lambda alpha: f"{theorem_velocity(current_time(alpha, 4.2)):.2f}",
            font_size=21,
            color=V_COLOR,
        ).move_to(flow_box.get_center() + UP * 0.02)
        area_display = make_tracked_text(
            "int_1^t v(t)dt = ",
            alpha_tracker,
            formatter=lambda alpha: f"{theorem_displacement_from_one(max(current_time(alpha, 4.2), 1.0)):.2f}",
            font_size=21,
            color=A_COLOR,
        ).move_to(flow_box.get_center() + DOWN * 0.48)

        v_point = always_redraw(
            lambda: Dot(
                v_axes.c2p(current_time(alpha_tracker.get_value(), 4.2), theorem_velocity(current_time(alpha_tracker.get_value(), 4.2))),
                radius=0.07,
                color=V_COLOR,
            )
        )
        v_cursor = always_redraw(
            lambda: make_cursor_line(
                v_axes,
                current_time(alpha_tracker.get_value(), 4.2),
                theorem_velocity(current_time(alpha_tracker.get_value(), 4.2)),
            )
        )
        v_area = always_redraw(
            lambda: make_rectangles(
                v_axes,
                theorem_velocity,
                1.0,
                max(current_time(alpha_tracker.get_value(), 4.2), 1.0),
                16,
                sample="mid",
                positive_fill=SOFT_BLUE,
                positive_stroke=V_COLOR,
                fill_opacity=0.36,
            )
        )

        derive_chip = make_badge("derivar: inclinacao -> velocidade", font_size=18, color=V_COLOR).move_to(DOWN * 2.05 + LEFT * 3.35)
        integrate_chip = make_badge("integrar: area -> Delta x", font_size=18, color=A_COLOR).move_to(DOWN * 2.05 + RIGHT * 0.25)
        closing = make_badge("o que a derivada mede agora, a integral recompõe no intervalo", font_size=18, color=INK).move_to(DOWN * 2.78)

        self.play(FadeIn(title, shift=DOWN * 0.08), run_time=0.8)
        self.play(FadeIn(x_panel), FadeIn(v_panel), FadeIn(flow_box), FadeIn(flow_title), run_time=1.0)
        self.play(Create(x_curve), Create(v_curve), run_time=1.2)
        self.play(FadeIn(tangent_probe), FadeIn(v_point), FadeIn(v_cursor), FadeIn(t_display), FadeIn(v_display), FadeIn(area_display), run_time=0.9)
        self.play(outline_focus(tangent_probe[0]), FadeIn(derive_chip), run_time=0.8)
        self.play(alpha_tracker.animate.set_value(0.88), run_time=3.6, rate_func=linear)
        self.play(FadeIn(v_area), FadeIn(integrate_chip), run_time=0.8)
        self.play(outline_focus(v_area), run_time=0.8)
        self.play(FadeIn(closing, shift=UP * 0.08), run_time=0.8)
        self.wait(1.0)


class VelocityGraphOperationsScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text(
            "Um unico grafico v x t responde varias perguntas",
            font="DejaVu Serif",
            font_size=28,
            color=INK,
        ).to_edge(UP).shift(DOWN * 0.2)

        panel, axes = make_axes_panel(
            "grafico operacional de v(t)",
            LEFT * 2.25 + UP * 0.4,
            [0, 5, 1],
            [0, 2.8, 0.5],
            x_length=6.0,
            y_length=3.25,
            title_color=V_COLOR,
        )
        graph = axes.plot(engineering_velocity, x_range=[0, 5], color=V_COLOR, stroke_width=4.8)

        alpha_tracker = ValueTracker(0.16)
        t_value = lambda: current_time(alpha_tracker.get_value())
        point = always_redraw(lambda: Dot(axes.c2p(t_value(), engineering_velocity(t_value())), radius=0.075, color=V_COLOR))
        tangent_probe = make_tangent_probe(graph, alpha_tracker, point_color=V_COLOR, tangent_color=INK, line_length=2.6)
        cursor = always_redraw(lambda: make_cursor_line(axes, t_value(), engineering_velocity(t_value())))
        area = always_redraw(
            lambda: make_rectangles(
                axes,
                engineering_velocity,
                0.0,
                t_value(),
                20,
                sample="mid",
                positive_fill=SOFT_BLUE,
                positive_stroke=V_COLOR,
                fill_opacity=0.34,
            )
        )

        card = RoundedRectangle(
            corner_radius=0.2,
            width=4.35,
            height=4.15,
            stroke_color=ACCENT_SOFT,
            stroke_width=2.3,
            fill_color=CARD_FILL_ALT,
            fill_opacity=1,
        ).move_to(RIGHT * 4.45 + UP * 0.2)
        card_title = Text("perguntas operacionais", font="DejaVu Sans", font_size=22, color=INK, weight="BOLD").move_to(
            card.get_top() + DOWN * 0.3
        )
        q1 = Text("valor do grafico?", font="DejaVu Sans", font_size=20, color=MUTED).move_to(card.get_center() + UP * 1.0)
        q2 = Text("inclinacao local?", font="DejaVu Sans", font_size=20, color=MUTED).move_to(card.get_center() + UP * 0.3)
        q3 = Text("area ate agora?", font="DejaVu Sans", font_size=20, color=MUTED).move_to(card.get_center() + DOWN * 0.4)
        q4 = Text("leitura fisica?", font="DejaVu Sans", font_size=20, color=MUTED).move_to(card.get_center() + DOWN * 1.1)

        a1 = make_tracked_text("", alpha_tracker, formatter=lambda alpha: f"v = {engineering_velocity(current_time(alpha)):.2f} m/s", font_size=19, color=V_COLOR).next_to(q1, DOWN, buff=0.08)
        a2 = make_tracked_text("", alpha_tracker, formatter=lambda alpha: f"a = {engineering_acceleration(current_time(alpha)):.2f} m/s^2", font_size=19, color=X_COLOR).next_to(q2, DOWN, buff=0.08)
        a3 = make_tracked_text("", alpha_tracker, formatter=lambda alpha: f"Delta x = {engineering_displacement(current_time(alpha)):.2f} m", font_size=19, color=A_COLOR).next_to(q3, DOWN, buff=0.08)
        a4 = Text("velocidade, aceleracao e deslocamento", font="DejaVu Sans", font_size=18, color=INK).next_to(q4, DOWN, buff=0.08)

        footer = make_badge("em engenharia, um grafico bom ja responde metade do problema", font_size=18, color=INK).move_to(DOWN * 2.9)

        self.play(FadeIn(title, shift=DOWN * 0.08), run_time=0.8)
        self.play(FadeIn(panel), FadeIn(card), FadeIn(card_title), run_time=1.0)
        self.play(Create(graph), run_time=1.0)
        self.play(staggered_reveal(q1, q2, q3, q4, lag_ratio=0.12, run_time=1.2))
        self.play(FadeIn(a1), FadeIn(a2), FadeIn(a3), FadeIn(a4), FadeIn(area), FadeIn(cursor), FadeIn(point), FadeIn(tangent_probe[0]), run_time=0.9)
        self.play(chained_sequence(outline_focus(q1), outline_focus(q2), outline_focus(q3), run_time=2.3))
        self.play(alpha_tracker.animate.set_value(0.92), run_time=6.8, rate_func=linear)
        self.play(FadeIn(footer, shift=UP * 0.08), run_time=0.8)
        self.wait(1.0)
