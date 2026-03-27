---
name: livro-manim-movimento
description: Aplica tecnicas de movimento e trilha do Manim como MoveAlongPath e TracedPath. Use quando a trajetoria, o rastro ou a leitura do percurso importarem didaticamente.
---

# Livro: Manim movimento

## Leia primeiro

- [../../../docs/ai/pipelines/usar-tecnica-manim.md](../../../docs/ai/pipelines/usar-tecnica-manim.md)
- [../../../animations/manim/recipes/motion_recipes.py](../../../animations/manim/recipes/motion_recipes.py)

## Receitas principais

- `make_motion_trail`: rastro independente
- `travel_along_path`: deslocamento por curva ou eixo
- `move_with_trail`: atalho com movimento e memoria do caminho

## Regras rapidas

- use `MoveAlongPath` quando a forma da trajetoria precisa ser vista
- use `TracedPath` quando o observador precisa lembrar onde o objeto passou
- controle `run_time` com cuidado para o rastro conseguir ser lido

## Fechamento

```bash
python3 -m py_compile animations/manim/*.py animations/manim/recipes/*.py scripts/render_manim_assets.py
```

