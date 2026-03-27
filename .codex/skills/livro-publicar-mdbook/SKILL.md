---
name: livro-publicar-mdbook
description: Publica este livro em mdBook no GitHub Pages. Use quando a tarefa for fechar a versão atual, validar o build estático, enviar para main e acompanhar o workflow publish-pages.
---

# Livro: publicar mdBook

Use esta skill para a etapa de publicação.

## Leia primeiro

- [../../../docs/ai/pipelines/publicar.md](../../../docs/ai/pipelines/publicar.md)

## Regras rápidas

- valide com `make build-pages` antes do push
- publicação normal acontece por push em `main`
- `make publish` serve para reexecutar o workflow manualmente

## Fechamento

```bash
make build-pages
git push origin main
```
