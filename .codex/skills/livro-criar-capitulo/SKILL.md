---
name: livro-criar-capitulo
description: Cria um novo capítulo ou página autoral neste livro em mdBook. Use quando for necessário adicionar um novo arquivo em content/ e integrá-lo ao fluxo por meio de content/SUMMARY.md.
---

# Livro: criar capítulo

Use esta skill quando a mudança exige nova página no livro.

## Leia primeiro

- [../../../docs/ai/pipelines/criar-capitulo.md](../../../docs/ai/pipelines/criar-capitulo.md)

## Regras rápidas

- crie o arquivo em `content/`
- atualize `content/SUMMARY.md`
- se o novo capítulo trouxer mídia, aplique a skill específica correspondente

## Fechamento

```bash
make build-pages
```
