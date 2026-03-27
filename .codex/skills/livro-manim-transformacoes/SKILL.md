---
name: livro-manim-transformacoes
description: Aplica tecnicas de transformacao do Manim como TransformMatchingShapes e TransformFromCopy. Use quando um objeto, formula ou label precisa virar outro com continuidade visual.
---

# Livro: Manim transformacoes

## Leia primeiro

- [../../../docs/ai/pipelines/usar-tecnica-manim.md](../../../docs/ai/pipelines/usar-tecnica-manim.md)
- [../../../animations/manim/recipes/transform_recipes.py](../../../animations/manim/recipes/transform_recipes.py)

## Receitas principais

- `morph_by_shape`: forma antiga vira a nova por matching visual
- `duplicate_into`: uma copia sai de um lugar e se encaixa em outro
- `soft_swap`: troca suave quando o matching completo nao ajuda

## Regras rapidas

- prefira `TransformMatchingShapes` para texto, formula curta e cards parecidos
- prefira `TransformFromCopy` quando a copia precisa deixar claro de onde a ideia veio
- use `FadeTransform` quando o ganho didatico vier da continuidade geral e nao do matching letra a letra

## Fechamento

```bash
python3 -m py_compile animations/manim/*.py animations/manim/recipes/*.py scripts/render_manim_assets.py
```

