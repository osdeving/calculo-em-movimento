# Guias de consulta

> Página gerada automaticamente pelo pipeline editorial do livro.

Esta área reúne atalhos de navegação para consulta rápida do material.

- [Lista de figuras](lista-de-figuras.md)
- [Lista de vídeos](lista-de-videos.md)
- [Lista de fórmulas](lista-de-formulas.md)
- [Glossário](glossario.md)
- [Índice remissivo](indice-remissivo.md)

## O que você encontra aqui

- **Figuras**: 19 entradas com legenda e capítulo de origem.
- **Vídeos**: 18 animações integradas ao texto.
- **Fórmulas**: 12 fórmulas principais marcadas editorialmente.
- **Glossário**: 18 termos-base do curso.
- **Índice remissivo**: 17 termos com ocorrências linkáveis no corpo do livro.

## Como manter isso atualizado

- para incluir uma fórmula na lista, adicione um comentário `<!-- formula: Título -->` logo antes do bloco `$$ ... $$`
- para ampliar o glossário e o índice, edite `content/reference_data/glossary.json`
- depois rode `make build` ou `make serve`
