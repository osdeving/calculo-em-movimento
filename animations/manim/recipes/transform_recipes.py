from __future__ import annotations

from manim import FadeTransform, Mobject, PI, TransformFromCopy, TransformMatchingShapes


def morph_by_shape(
    source: Mobject,
    target: Mobject,
    path_arc: float = PI / 7,
    run_time: float = 1.0,
) -> TransformMatchingShapes:
    """Transicao que preserva a ideia visual entre formas parecidas."""

    return TransformMatchingShapes(source, target, path_arc=path_arc, run_time=run_time)


def duplicate_into(
    source: Mobject,
    target: Mobject,
    path_arc: float = PI / 10,
    run_time: float = 0.9,
) -> TransformFromCopy:
    """Copia uma ideia visual de um lugar para outro."""

    return TransformFromCopy(source, target, path_arc=path_arc, run_time=run_time)


def soft_swap(source: Mobject, target: Mobject, run_time: float = 0.8) -> FadeTransform:
    """Troca suave quando a continuação conceitual importa mais que o matching."""

    return FadeTransform(source, target, run_time=run_time)

