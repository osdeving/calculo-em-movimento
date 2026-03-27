from __future__ import annotations

from manim import Animation, AnimationGroup, FadeIn, LaggedStart, Mobject, Succession, UP


DEFAULT_SHIFT = UP * 0.18


def staggered_reveal(
    *mobjects: Mobject,
    shift=DEFAULT_SHIFT,
    lag_ratio: float = 0.18,
    run_time: float = 1.6,
) -> LaggedStart:
    """Entrada em cascata no estilo LaggedStart."""

    return LaggedStart(
        *(FadeIn(mobject, shift=shift) for mobject in mobjects),
        lag_ratio=lag_ratio,
        run_time=run_time,
    )


def layered_parallel(
    *animations: Animation,
    lag_ratio: float = 0.0,
    run_time: float | None = None,
) -> AnimationGroup:
    """Agrupa animacoes paralelas com controle de atraso."""

    kwargs: dict[str, float] = {"lag_ratio": lag_ratio}
    if run_time is not None:
        kwargs["run_time"] = run_time
    return AnimationGroup(*animations, **kwargs)


def chained_sequence(*animations: Animation, run_time: float | None = None) -> Succession:
    """Encadeia etapas que devem ocorrer em serie."""

    kwargs: dict[str, float] = {}
    if run_time is not None:
        kwargs["run_time"] = run_time
    return Succession(*animations, **kwargs)

