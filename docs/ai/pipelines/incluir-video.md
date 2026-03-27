# Incluir vídeo

## Quando usar

Use este workflow para adicionar ou substituir uma animação pedagógica.

## Arquivos principais

- `animations/manim/*.py`
- `animations/manim/book_motion.py`
- `scripts/render_manim_assets.py`
- `content/<capitulo>.md`
- `content/media/manim/*.mp4`

## Passos

1. Crie ou atualize a cena Manim.
2. Se a cena usar componentes compartilháveis, coloque-os em `animations/manim/book_motion.py`.
3. Registre a cena em `scripts/render_manim_assets.py`, com `source`, `scene`, `output_stem`, `target` e dependências extras quando houver.
4. Se a cena depender de biblioteca compartilhada, declare essas dependências no campo `dependencies` do registro. As checagens automáticas usam isso para exigir atualização do `.mp4` correspondente.
5. Embuta o vídeo no capítulo com markup explícito:

```html
<figure class="book-figure book-motion">
  <video class="book-video" controls muted loop playsinline preload="metadata" data-autoplay-when-visible>
    <source src="media/manim/arquivo.mp4" type="video/mp4">
    Seu navegador não conseguiu reproduzir a animação.
  </video>
  <figcaption>Legenda pedagógica.</figcaption>
</figure>
```

6. Use legenda clara, porque a lista de vídeos e a numeração editorial dependem dela.
7. Renderize a cena.

## Impactos automáticos

- o vídeo entra em `content/media/manim/`
- a lista de vídeos é regenerada no build
- a legenda do `<figcaption>` vira a descrição pública da mídia
- o `lab.js` aplica autoplay/pause por visibilidade para vídeos com `data-autoplay-when-visible`

## Validação

```bash
python3 -m py_compile animations/manim/*.py scripts/render_manim_assets.py
python3 scripts/render_manim_assets.py
make check-media
make build-pages
```

## Não fazer

- não adicionar vídeo sem `figcaption`
- não esquecer de registrar a cena no `scripts/render_manim_assets.py`
