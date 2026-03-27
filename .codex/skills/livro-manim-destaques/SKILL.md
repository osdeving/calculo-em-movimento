---
name: livro-manim-destaques
description: Aplica tecnicas de destaque visual do Manim como Circumscribe, Indicate e Flash. Use quando a tarefa pedir guiar o olhar para um ponto, termo, regiao ou etiqueta sem redesenhar a cena inteira.
---

# Livro: Manim destaques

## Leia primeiro

- [../../../docs/ai/pipelines/usar-tecnica-manim.md](../../../docs/ai/pipelines/usar-tecnica-manim.md)
- [../../../animations/manim/recipes/highlight_recipes.py](../../../animations/manim/recipes/highlight_recipes.py)

## Receitas principais

- `outline_focus`: contorno que abraça o elemento
- `pulse_focus`: pulso curto de destaque
- `spark_point`: flash pontual

## Regras rapidas

- `Circumscribe` serve melhor para caixas, formulas, retas e areas
- `Indicate` funciona melhor em texto curto, labels e pontos
- `Flash` e bom como confirmacao de resultado ou chegada em um valor-chave

## Fechamento

```bash
python3 -m py_compile animations/manim/*.py animations/manim/recipes/*.py scripts/render_manim_assets.py
```

