# Criar capítulo

## Quando usar

Use este workflow quando a mudança cria uma nova página do livro, e não apenas uma nova seção.

## Arquivos principais

- `content/<novo-capitulo>.md`
- `content/SUMMARY.md`

## Passos

1. Escolha o slug do arquivo em `content/`.
2. Crie o capítulo com `#` principal e estrutura interna coerente.
3. Adicione a página no lugar correto em `content/SUMMARY.md`.
4. Se o capítulo introduzir fórmulas centrais, marque as que devem entrar na lista de fórmulas.
5. Se houver figuras ou vídeos, use os playbooks específicos e só depois feche o build completo.
6. Atualize links cruzados de introdução, prefácio ou capítulos vizinhos apenas se isso ajudar a navegação.

## Impactos automáticos

- o sumário do `mdBook` muda imediatamente
- as páginas de referência passam a considerar o novo capítulo no próximo build

## Validação

```bash
make build-pages
```
