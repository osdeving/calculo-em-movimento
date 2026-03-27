---
name: livro-incluir-figura
description: Inclui uma figura estática ou gerada neste livro em mdBook. Use quando a tarefa envolver adicionar uma imagem, SVG, asset de terceiro ou ilustração gerada por scripts para algum capítulo.
---

# Livro: incluir figura

Use esta skill quando a tarefa central for inserir uma figura pedagógica.

## Leia primeiro

- [../../../docs/ai/pipelines/incluir-figura.md](../../../docs/ai/pipelines/incluir-figura.md)

## Regras rápidas

- a figura deve ter legenda útil
- se houver licença de terceiro, registre em `content/assets/THIRD_PARTY.md`
- se o asset for gerado, altere o script-fonte em vez do arquivo final

## Fechamento

```bash
make build-pages
```
