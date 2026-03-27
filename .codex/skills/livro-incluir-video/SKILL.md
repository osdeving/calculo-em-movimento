---
name: livro-incluir-video
description: Inclui uma animação Manim neste livro em mdBook. Use quando a tarefa pedir vídeo novo, troca de vídeo existente, nova cena Manim, embed em capítulo ou sincronização da lista de vídeos.
---

# Livro: incluir vídeo

Use esta skill quando a tarefa central for mídia animada.

## Leia primeiro

- [../../../docs/ai/pipelines/incluir-video.md](../../../docs/ai/pipelines/incluir-video.md)

## Regras rápidas

- componentes reutilizáveis vão para `animations/manim/book_motion.py`
- cada nova cena precisa ser registrada em `scripts/render_manim_assets.py`
- o embed no capítulo deve usar `<figure>` + `<video>` + `<figcaption>`
- a lista de vídeos é gerada; não editar manualmente

## Fechamento

```bash
python3 -m py_compile animations/manim/*.py scripts/render_manim_assets.py
python3 scripts/render_manim_assets.py
make build-pages
```
