# Galeria local de tecnicas Manim

Este diretorio reune receitas curadas a partir da documentacao oficial do Manim para acelerar a criacao de animacoes do livro.

Nao e uma copia literal da `Example Gallery`. Sao adaptacoes pequenas, ja pensadas para o estilo visual deste projeto e para os tipos de cena que aparecem em calculo e cinematica.

## Fontes oficiais

- Example Gallery: https://docs.manim.community/en/stable/examples.html
- `LaggedStart`: https://docs.manim.community/en/stable/reference/manim.animation.composition.LaggedStart.html
- `Succession`: https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html
- `AnimationGroup`: https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html
- `TransformFromCopy`: https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformFromCopy.html
- `TransformMatchingShapes`: https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html
- `Circumscribe`: https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html
- `MoveAlongPath`: https://docs.manim.community/en/stable/reference/manim.animation.movement.MoveAlongPath.html
- `TracedPath`: https://docs.manim.community/en/stable/reference/manim.animation.changing.TracedPath.html
- `ValueTracker`: https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html
- `always_redraw`: https://docs.manim.community/en/stable/reference/manim.animation.updaters.mobject_update_utils.html

## Mapa rapido

- `composition_recipes.py`: cascata, escalonamento, sincronizacao e montagem de blocos.
- `transform_recipes.py`: morphing entre textos, copias que viram outra coisa, trocas suaves.
- `highlight_recipes.py`: contorno, pulso e sinais de destaque.
- `motion_recipes.py`: movimento em trilha, rastro e leitura de percurso.
- `tracker_recipes.py`: elementos vivos dirigidos por `ValueTracker` e `always_redraw`.

## Como usar

1. Escolha a familia da tecnica.
2. Copie a receita minima e adapte ao contexto da cena.
3. Se o visual se repetir em mais de uma cena, promova os componentes para `animations/manim/book_motion.py`.
4. Se a tecnica virar uma nova cena do livro, registre a renderizacao em `scripts/render_manim_assets.py`.
5. Se virar video embutido em capitulo, use `<figure>`, `<video>` e `<figcaption>` no Markdown.

## Quando escolher cada familia

- Composicao: quando o problema e o ritmo da entrada, nao o desenho.
- Transformacoes: quando um objeto precisa virar outro sem perder continuidade conceitual.
- Destaques: quando um elemento ja existe em cena e voce quer guiar o olhar.
- Movimento: quando o caminho importa tanto quanto o ponto final.
- Trackers: quando a cena precisa responder continuamente a um valor que muda.

