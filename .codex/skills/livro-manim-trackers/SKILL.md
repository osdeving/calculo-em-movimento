---
name: livro-manim-trackers
description: Aplica tecnicas de ValueTracker e always_redraw para cenas vivas. Use quando a animacao precisar reagir continuamente a um valor, como tempo, posicao, tangente ou area.
---

# Livro: Manim trackers

## Leia primeiro

- [../../../docs/ai/pipelines/usar-tecnica-manim.md](../../../docs/ai/pipelines/usar-tecnica-manim.md)
- [../../../animations/manim/recipes/tracker_recipes.py](../../../animations/manim/recipes/tracker_recipes.py)

## Receitas principais

- `make_tracked_text`: texto vivo para relogios, badges e leituras
- `make_tangent_probe`: ponto e tangente movidos por tracker

## Regras rapidas

- `ValueTracker` e o eixo de controle da cena; mantenha um tracker por ideia principal
- `always_redraw` deve cuidar apenas do que realmente precisa ser recalculado
- se a cena ficar pesada, reduza a quantidade de objetos vivos antes de mexer no tema visual

## Fechamento

```bash
python3 -m py_compile animations/manim/*.py animations/manim/recipes/*.py scripts/render_manim_assets.py
```
