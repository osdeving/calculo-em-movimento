# Cálculo em Movimento

Laboratório editorial de um livro de cinemática com:

- conteúdo-fonte em Markdown
- assets visuais separados do renderer
- renderização HTML via `mdBook`
- matemática em LaTeX mantida no Markdown via preprocessor local
- animações renderizadas via `Manim Community`
- pipeline simples com `make`

## Estrutura

- `content/`: conteúdo real do livro, separado por página/capítulo
- `content/assets/`: figuras e ilustrações usadas pelo conteúdo
- `content/media/`: vídeos e outras mídias geradas para o livro
- `animations/manim/`: cenas-fonte do Manim
- `renderers/mdbook/`: configuração visual e build do `mdBook`
- `scripts/generate_scene_assets.py`: gera os SVGs esquemáticos 2D
- `scripts/render_manim_assets.py`: renderiza as animações do Manim
- `dist/book/`: saída gerada do livro

## Fluxo de edição

1. Edite o conteúdo em `content/*.md`
2. Se precisar ajustar ilustrações, edite `scripts/generate_scene_assets.py`
3. Se precisar ajustar animações, edite `animations/manim/*.py`
4. Gere o livro com `make build`
5. Sirva localmente com `make serve`

## Comandos

```bash
make build
make animations
make serve
make serve-stop
make clean
```

`make build` e `make serve` passam por:

- geração dos SVGs
- renderização das animações Manim quando houver mudanças
- build ou serve do `mdBook`

## Porta do servidor

O `make serve` tenta usar a porta `3000`.

- se houver uma instância antiga do `mdBook` gerenciada por este projeto, ela é encerrada antes de subir outra
- se a `3000` estiver ocupada por outro processo, o script sobe automaticamente na próxima porta livre e informa a URL no terminal

## Observação

O conteúdo é a fonte de verdade. A camada visual fica no renderer `mdBook`, o que facilita trocar a apresentação depois sem reescrever os Markdown.

As fórmulas continuam sendo escritas diretamente no Markdown com `$...$` e `$$...$$`. Um preprocessor local converte isso para o formato esperado pelo `mdBook` antes do HTML final ser gerado.
