# Alterar capítulo

## Quando usar

Use este workflow quando a tarefa for editar um capítulo já existente:

- reescrever explicação
- acrescentar exemplo textual
- ajustar ordem interna
- corrigir fórmulas
- melhorar links para apêndices ou capítulos

## Arquivos principais

- `content/<capitulo>.md`

## Passos

1. Identifique o arquivo do capítulo e a seção afetada.
2. Edite o Markdown autoral no próprio arquivo do capítulo.
3. Se o título do capítulo mudar, sincronize o texto do link em `content/SUMMARY.md`.
4. Se entrar uma fórmula que deve aparecer na lista de fórmulas, adicione `<!-- formula: Título -->` antes do bloco `$$ ... $$`.
5. Se entrar um termo novo recorrente, avalie atualizar `content/reference_data/glossary.json`.
6. Se a mudança pedir figura ou vídeo, pare e use o playbook específico em vez de improvisar.

## Impactos automáticos

- `content/references/*.md` será regenerado no build
- links internos, glossário e listas editoriais podem mudar como consequência da nova redação

## Validação

```bash
make build-pages
```

## Não fazer

- não editar `content/references/*.md` manualmente
- não editar `dist/book/*` manualmente
