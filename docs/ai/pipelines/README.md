# Pipelines de IA

Este diretório descreve, por ação, como um agente deve trabalhar neste repositório.

Use estes playbooks quando precisar fazer mudanças modulares, sem improvisar a pipeline a cada tarefa.

## Ações disponíveis

- [alterar-capitulo.md](/home/willams/curso_calculo_cinematica_bundle/docs/ai/pipelines/alterar-capitulo.md)
- [criar-secao.md](/home/willams/curso_calculo_cinematica_bundle/docs/ai/pipelines/criar-secao.md)
- [criar-capitulo.md](/home/willams/curso_calculo_cinematica_bundle/docs/ai/pipelines/criar-capitulo.md)
- [incluir-figura.md](/home/willams/curso_calculo_cinematica_bundle/docs/ai/pipelines/incluir-figura.md)
- [incluir-video.md](/home/willams/curso_calculo_cinematica_bundle/docs/ai/pipelines/incluir-video.md)
- [publicar.md](/home/willams/curso_calculo_cinematica_bundle/docs/ai/pipelines/publicar.md)

## Regras gerais

- `content/*.md` é a fonte de verdade do conteúdo autoral.
- `content/references/*.md` é gerado; não editar manualmente.
- `dist/book/` é gerado; não editar manualmente.
- Se a mudança cria uma nova página, atualizar `content/SUMMARY.md`.
- Se a mudança introduz vídeo ou figura, garantir legenda clara; as páginas de referência dependem disso.
- Se a mudança introduz fórmula central, considerar `<!-- formula: Título -->` antes do bloco display.

## Fechamento padrão

Quando não houver razão para usar algo mais específico, feche a mudança com:

```bash
make build-pages
```
