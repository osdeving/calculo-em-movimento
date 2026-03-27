# AGENTS.md

## Propósito

Este repositório mantém um livro em `mdBook` cujo conteúdo-fonte vive em Markdown e cuja camada visual pode evoluir sem reescrever os capítulos.

O objetivo deste arquivo é orientar agentes de IA e contribuidores automatizados sobre:

- onde está a fonte de verdade de cada tipo de conteúdo
- quais pipelines são modulares
- quais arquivos são gerados
- como validar cada mudança sem quebrar o livro

## Fonte de Verdade

- `content/*.md`: capítulos, prefácio, introdução, apêndice e páginas autorais
- `content/SUMMARY.md`: ordem e navegação do livro
- `content/reference_data/glossary.json`: base do glossário e do índice remissivo
- `scripts/generate_scene_assets.py`: fonte das ilustrações 2D geradas
- `animations/manim/*.py`: fontes das animações Manim
- `animations/manim/book_motion.py`: biblioteca compartilhada de componentes visuais para animações
- `scripts/render_manim_assets.py`: registro de cenas Manim e pipeline de render
- `renderers/mdbook/theme/*`: camada visual do `mdBook`

## Arquivos Gerados

Não edite manualmente estes arquivos se a mudança puder ser feita na fonte:

- `content/references/*.md`
- `renderers/mdbook/theme/generated_glossary.js`
- `content/media/manim/*.mp4`
- `content/assets/*` quando forem artefatos gerados por script
- `dist/book/*`

Quando precisar mudar um desses artefatos, altere a fonte e rode o pipeline correspondente.

## Pipelines Modulares

Os workflows modulares deste repositório estão documentados em:

- [docs/ai/pipelines/README.md](/home/willams/curso_calculo_cinematica_bundle/docs/ai/pipelines/README.md)
- [docs/ai/pipelines/workflows.yaml](/home/willams/curso_calculo_cinematica_bundle/docs/ai/pipelines/workflows.yaml)

Os playbooks principais são:

- alterar capítulo existente
- criar seção em capítulo existente
- criar capítulo novo
- incluir figura
- incluir vídeo
- publicar no GitHub Pages

## Regras Operacionais

- Se o pedido for textual, edite primeiro `content/*.md`.
- Se o pedido criar uma nova página, atualize `content/SUMMARY.md`.
- Se o pedido incluir fórmula que deve aparecer na lista de fórmulas, adicione `<!-- formula: Título -->` imediatamente antes do bloco `$$ ... $$`.
- Se o pedido incluir figura, siga o playbook de figura; a lista de figuras é gerada automaticamente no build.
- Se o pedido incluir vídeo, siga o playbook de vídeo; a lista de vídeos é gerada automaticamente no build.
- Se o pedido alterar termos centrais do livro, considere atualizar `content/reference_data/glossary.json`.
- Se o pedido alterar layout, CSS ou comportamento do `mdBook`, valide ao menos com `make build-pages`.

## Validação Base

Use a menor validação suficiente para a mudança:

- texto puro: `make build-pages`
- ilustração gerada: `make assets` ou `python3 scripts/generate_scene_assets.py`, depois `make build-pages`
- vídeo novo ou alterado: `python3 -m py_compile ...`, `python3 scripts/render_manim_assets.py`, depois `make build-pages`
- checagem rápida de contratos e impactos: `make check-media`
- checagem local de pipeline + build estático: `make check-pipeline`
- publicação: push em `main` e conferir workflow `publish-pages`

## Skills Locais

As skills versionadas do repositório vivem em `.codex/skills/`.

Se o runtime atual não descobrir skills do projeto automaticamente, use os playbooks em `docs/ai/pipelines/` diretamente. As skills apontam para os mesmos fluxos e servem como atalhos operacionais para tarefas recorrentes.
