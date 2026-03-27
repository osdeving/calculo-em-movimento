---
name: livro-manim-composicao
description: Aplica tecnicas de composicao do Manim como LaggedStart, Succession e AnimationGroup. Use quando a tarefa pedir cascata, escalonamento, montagem em etapas ou sincronizacao entre varias entradas.
---

# Livro: Manim composicao

## Leia primeiro

- [../../../docs/ai/pipelines/usar-tecnica-manim.md](../../../docs/ai/pipelines/usar-tecnica-manim.md)
- [../../../animations/manim/recipes/composition_recipes.py](../../../animations/manim/recipes/composition_recipes.py)

## Receitas principais

- `staggered_reveal`: entrada em cascata
- `layered_parallel`: acoes paralelas com atraso controlado
- `chained_sequence`: etapas em serie

## Regras rapidas

- use `LaggedStart` para apresentar listas, badges e paines
- use `Succession` quando uma etapa precisa terminar antes da proxima nascer
- use `AnimationGroup` quando os eventos devem coexistir e só variar no ritmo

## Fechamento

```bash
python3 -m py_compile animations/manim/*.py animations/manim/recipes/*.py scripts/render_manim_assets.py
```

