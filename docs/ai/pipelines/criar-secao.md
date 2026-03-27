# Criar seção

## Quando usar

Use este workflow quando o capítulo já existe, mas precisa ganhar uma nova seção interna com heading próprio.

## Arquivos principais

- `content/<capitulo>.md`

## Passos

1. Escolha o capítulo correto.
2. Insira o novo heading no nível apropriado, normalmente `##` ou `###`.
3. Escreva a seção completa no próprio Markdown do capítulo.
4. Se a seção introduzir fórmulas centrais, use `<!-- formula: Título -->` antes dos blocos display relevantes.
5. Se a seção introduzir figura ou vídeo, siga também o playbook de figura ou vídeo.
6. Se a seção depender de base matemática, ligue para o apêndice quando fizer sentido.

## Impactos automáticos

- o `mdBook` gerará a âncora da nova seção
- a lista de fórmulas, figuras e vídeos pode mudar se a nova seção introduzir essas mídias
- o índice remissivo pode mudar se a redação incluir termos do glossário

## Validação

```bash
make build-pages
```
