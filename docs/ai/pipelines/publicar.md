# Publicar

## Quando usar

Use este workflow para colocar a versão atual do livro no GitHub Pages.

## Arquivos principais

- `main`
- `.github/workflows/publish-pages.yml`

## Passos

1. Garanta que a mudança local builda:

```bash
make build-pages
```

2. Verifique o estado do repositório:

```bash
git status --short
```

3. Faça commit do que deve ser publicado.
4. Faça push para `main`.
5. Acompanhe o workflow `publish-pages`.
6. Verifique a URL pública:

`https://osdeving.github.io/calculo-em-movimento/`

## Observação

- `make publish` é útil para disparar manualmente o workflow quando já existe um commit em `main`
- para publicação normal, o push em `main` já aciona o workflow
