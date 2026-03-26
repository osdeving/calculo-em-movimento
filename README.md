# Cálculo em Movimento

Laboratório editorial de um livro de cinemática com:

- conteúdo-fonte em Markdown
- assets visuais separados do renderer
- renderização HTML via `mdBook`
- pipeline simples com `make`

## Estrutura

- `content/`: conteúdo real do livro, separado por página/capítulo
- `content/assets/`: figuras e ilustrações usadas pelo conteúdo
- `renderers/mdbook/`: configuração visual e build do `mdBook`
- `scripts/generate_scene_assets.py`: gera os SVGs esquemáticos 2D
- `dist/book/`: saída gerada do livro

## Fluxo de edição

1. Edite o conteúdo em `content/*.md`
2. Se precisar ajustar ilustrações, edite `scripts/generate_scene_assets.py`
3. Gere o livro com `make build`
4. Sirva localmente com `make serve`

## Comandos

```bash
make build
make serve
make clean
```

## Observação

O conteúdo é a fonte de verdade. A camada visual fica no renderer `mdBook`, o que facilita trocar a apresentação depois sem reescrever os Markdown.
