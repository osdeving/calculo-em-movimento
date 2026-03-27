---
name: livro-alterar-capitulo
description: Edita um capítulo existente deste livro em mdBook. Use quando a tarefa for reescrever texto, ajustar fórmulas, melhorar explicações, corrigir links ou alterar seções já existentes dentro de um arquivo em content/*.md.
---

# Livro: alterar capítulo

Use esta skill para mudanças autorais dentro de um capítulo já existente.

## Leia primeiro

- [../../../docs/ai/pipelines/alterar-capitulo.md](../../../docs/ai/pipelines/alterar-capitulo.md)

## Regras rápidas

- a fonte de verdade é `content/*.md`
- se o título do capítulo mudar, sincronize `content/SUMMARY.md`
- se uma fórmula central deve entrar na lista de fórmulas, use `<!-- formula: Título -->`
- se a mudança pedir figura ou vídeo, migre para a skill específica

## Fechamento

```bash
make build-pages
```
