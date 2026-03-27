# Cálculo em Movimento

Laboratório editorial de um livro de cinemática com:

- conteúdo-fonte em Markdown
- assets visuais separados do renderer
- renderização HTML via `mdBook`
- matemática em LaTeX mantida no Markdown via preprocessor local
- animações renderizadas via `Manim Community`
- pipeline simples com `make`

## Estrutura

- `AGENTS.md`: contrato operacional para agentes de IA e automações
- `content/`: conteúdo real do livro, separado por página/capítulo
- `content/assets/`: figuras e ilustrações usadas pelo conteúdo
- `content/media/`: vídeos e outras mídias geradas para o livro
- `content/reference_data/glossary.json`: base editável do glossário e do índice remissivo
- `content/references/`: páginas geradas de consulta editorial
- `animations/manim/`: cenas-fonte do Manim
- `animations/manim/book_motion.py`: biblioteca local de componentes reutilizáveis para as animações
- `animations/manim/recipes/`: galeria local de snippets inspirados na documentação oficial do Manim
- `docs/ai/pipelines/`: playbooks por ação para agentes e automações
- `.codex/skills/`: skills locais do repositório para workflows recorrentes
- `renderers/mdbook/`: configuração visual e build do `mdBook`
- `scripts/generate_scene_assets.py`: gera os SVGs esquemáticos 2D
- `scripts/render_manim_assets.py`: renderiza as animações do Manim
- `scripts/build_reference_pages.py`: gera lista de figuras, vídeos, fórmulas, glossário e índice remissivo
- `dist/book/`: saída gerada do livro

## Fluxo de edição

1. Edite o conteúdo em `content/*.md`
2. Para incluir fórmulas na lista de fórmulas, adicione `<!-- formula: Título -->` logo antes do bloco `$$ ... $$`
3. Para ampliar glossário e índice remissivo, edite `content/reference_data/glossary.json`
4. Se precisar ajustar ilustrações, edite `scripts/generate_scene_assets.py`
5. Se precisar ajustar animações, edite `animations/manim/*.py`; para componentes compartilhados, prefira `animations/manim/book_motion.py`
6. Se quiser partir de uma técnica já conhecida do Manim, consulte `animations/manim/recipes/README.md` e reaproveite uma receita local
7. Gere o livro com `make build`
8. Sirva localmente com `make serve`

## Recursos editoriais automáticos

- o glossário alimenta uma camada de links automáticos no corpo dos capítulos
- figuras e vídeos recebem numeração editorial por capítulo no HTML final
- o índice remissivo usa a base do glossário, limita excesso de ocorrências e inclui `veja também`
- as páginas em `content/references/` são geradas automaticamente; não vale a pena editá-las manualmente

## Comandos

```bash
make build
make build-pages
make animations
make check-media
make check-pipeline
make publish
make serve
make serve-stop
make clean
```

`make build` e `make serve` passam por:

- geração das páginas de referência
- geração dos SVGs
- renderização das animações Manim quando houver mudanças
- build ou serve do `mdBook`

`make build-pages` gera apenas o site estático pronto para publicação, usando os assets e vídeos já versionados no repositório.

`make check-media` roda as checagens automáticas de contrato de mídia e de impacto entre fontes e artefatos gerados.

`make check-pipeline` roda `make check-media` e fecha com `make build-pages`.

`make publish` dispara manualmente o workflow de publicação no GitHub Pages para a branch `main`.

## Porta do servidor

O `make serve` tenta usar a porta `3000`.

- se houver uma instância antiga do `mdBook` gerenciada por este projeto, ela é encerrada antes de subir outra
- se a `3000` estiver ocupada por outro processo, o script sobe automaticamente na próxima porta livre e informa a URL no terminal

## Observação

O conteúdo é a fonte de verdade. A camada visual fica no renderer `mdBook`, o que facilita trocar a apresentação depois sem reescrever os Markdown.

As fórmulas continuam sendo escritas diretamente no Markdown com `$...$` e `$$...$$`. Um preprocessor local converte isso para o formato esperado pelo `mdBook` antes do HTML final ser gerado.

## Publicação

O repositório está preparado para publicar no GitHub Pages via GitHub Actions.

- o workflow fica em `.github/workflows/publish-pages.yml`
- o build de publicação usa `make build-pages`
- a URL esperada da publicação é `https://osdeving.github.io/calculo-em-movimento/`

Observação importante:

- o GitHub Pages publica o site de forma pública, mesmo quando o repositório é privado, desde que o plano/conta permita esse recurso
