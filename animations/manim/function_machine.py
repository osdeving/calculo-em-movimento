from __future__ import annotations

import sys
from pathlib import Path

from manim import (
    Arrow,
    Create,
    FadeIn,
    Flash,
    Indicate,
    Line,
    Scene,
    Text,
    Transform,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    VGroup,
    ValueTracker,
    smooth,
)


THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from book_motion import (  # noqa: E402
    ACCENT,
    HIGHLIGHT,
    INK,
    MUTED,
    PAPER,
    make_badge,
    make_car,
    make_function_machine,
    make_signal_chip,
    make_stopwatch,
    make_track,
)


class PositionFunctionMachineScene(Scene):
    def construct(self) -> None:
        self.camera.background_color = PAPER

        title = Text(
            "Em x(t), o tempo entra e a posicao sai",
            font="DejaVu Serif",
            font_size=30,
            color=INK,
        ).to_edge(UP).shift(DOWN * 0.18)

        time_tracker = ValueTracker(0)
        stopwatch = make_stopwatch(time_tracker, max_time=4.0, scale_factor=0.92).to_corner(UP + LEFT).shift(RIGHT * 0.58 + DOWN * 0.66)

        machine = make_function_machine("x(t)", "exemplo: x(t) = 2t^2 + 4t", scale_factor=1.0).move_to(UP * 0.9 + RIGHT * 0.25)
        input_arrow = Arrow(machine.get_left() + LEFT * 1.8, machine.get_left() + LEFT * 0.12, buff=0, stroke_width=5, tip_length=0.18, color=ACCENT)
        output_arrow = Arrow(machine.get_right() + RIGHT * 0.12, machine.get_right() + RIGHT * 1.8, buff=0, stroke_width=5, tip_length=0.18, color=HIGHLIGHT)
        input_label = Text("tempo", font="DejaVu Sans", font_size=22, color=MUTED).next_to(input_arrow, UP, buff=0.1)
        output_label = Text("posicao", font="DejaVu Sans", font_size=22, color=MUTED).next_to(output_arrow, UP, buff=0.1)

        track, axis_point = make_track(left_edge=5.9, right_edge=5.4, y=3.1, max_value=50, tick_step=10)
        axis, ticks, labels, axis_label = track

        car = make_car(0.72).move_to(axis_point(0) + UP * 0.42)
        initial_marker = Line(axis_point(0) + DOWN * 0.18, axis_point(0) + UP * 0.48, color=ACCENT, stroke_width=4)
        initial_badge = make_badge("x(0) = 0 m", font_size=18, color=ACCENT).move_to(axis_point(0) + UP * 1.0)

        samples = [
            {"time": 1, "position": 6},
            {"time": 2, "position": 16},
            {"time": 4, "position": 48},
        ]

        stored_badges = VGroup(initial_badge)
        stored_markers = VGroup(initial_marker)

        self.play(FadeIn(title, shift=DOWN * 0.08))
        self.play(FadeIn(stopwatch, shift=RIGHT * 0.1))
        self.play(FadeIn(machine, shift=UP * 0.08), Create(input_arrow), Create(output_arrow))
        self.play(FadeIn(input_label, shift=UP * 0.08), FadeIn(output_label, shift=UP * 0.08))
        self.play(Create(axis), FadeIn(axis_label, shift=UP * 0.08))
        self.play(FadeIn(ticks, shift=UP * 0.06), FadeIn(labels, shift=UP * 0.06))
        self.play(FadeIn(car, shift=LEFT * 0.08), Create(initial_marker), FadeIn(initial_badge, shift=UP * 0.08))

        for sample in samples:
            time_value = sample["time"]
            position_value = sample["position"]

            input_chip = make_signal_chip(f"t = {time_value} s", color=ACCENT).move_to(input_arrow.get_start() + RIGHT * 0.28)
            output_chip = make_signal_chip(f"x({time_value}) = {position_value} m", color=HIGHLIGHT).move_to(output_arrow.get_end() + LEFT * 0.12)
            marker = Line(axis_point(position_value) + DOWN * 0.18, axis_point(position_value) + UP * 0.48, color=HIGHLIGHT, stroke_width=4)
            badge = make_badge(f"x({time_value}) = {position_value} m", font_size=18, color=HIGHLIGHT).move_to(axis_point(position_value) + UP * 1.0)

            self.play(FadeIn(input_chip, shift=RIGHT * 0.12))
            self.play(
                time_tracker.animate.set_value(time_value),
                input_chip.animate.move_to(machine.get_center() + LEFT * 0.55),
                run_time=0.9,
                rate_func=smooth,
            )
            self.play(
                Indicate(machine, color=HIGHLIGHT),
                Flash(machine.get_center(), color=HIGHLIGHT, line_length=0.18),
                run_time=0.55,
            )
            self.play(Transform(input_chip, output_chip), run_time=0.45)
            self.play(
                Transform(input_chip, badge),
                Create(marker),
                car.animate.move_to(axis_point(position_value) + UP * 0.42),
                run_time=1.0,
                rate_func=smooth,
            )

            stored_badges.add(input_chip)
            stored_markers.add(marker)

        closing = make_badge("tempo entra, x(t) devolve uma posicao", font_size=18, color=INK).move_to(DOWN * 1.25)

        self.play(FadeIn(closing, shift=UP * 0.08))
        self.wait(1.0)
