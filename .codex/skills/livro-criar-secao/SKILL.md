---
name: livro-criar-secao
description: Cria uma nova seção dentro de um capítulo existente deste livro em mdBook. Use quando o arquivo do capítulo já existe, mas precisa ganhar um novo heading, texto, fórmulas, exemplos ou links internos.
---

# Livro: criar seção

Use esta skill para ampliar um capítulo sem criar nova página no sumário.

## Leia primeiro

- [../../../docs/ai/pipelines/criar-secao.md](../../../docs/ai/pipelines/criar-secao.md)

## Regras rápidas

- edite só o arquivo do capítulo enquanto a mudança for interna
- se a seção ganhar mídia, use também a skill de figura ou vídeo
- se a seção introduzir fórmula central, marque-a para a lista de fórmulas

## Fechamento

```bash
make build-pages
```
