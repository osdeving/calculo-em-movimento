# Incluir figura

## Quando usar

Use este workflow para inserir:

- imagem estática em Markdown
- `<figure>` com legenda explícita
- ilustração gerada por `scripts/generate_scene_assets.py`
- asset de terceiro com crédito versionado

## Arquivos principais

- `content/<capitulo>.md`
- `content/assets/*`
- `scripts/generate_scene_assets.py`

## Passos

1. Decida se a figura será:
   - um asset pronto em `content/assets/`
   - uma figura gerada por `scripts/generate_scene_assets.py`
2. Se o asset vier de terceiros, registre a origem e a licença em `content/assets/THIRD_PARTY.md`.
3. Insira a figura no capítulo:
   - imagem simples: `![legenda](assets/arquivo.ext)`
   - figura mais controlada: `<figure class="book-figure"> ... <figcaption>...</figcaption></figure>`
4. Escreva `alt` e legenda com valor pedagógico, porque a lista de figuras depende disso.
5. Se a figura foi gerada por script, regenere os assets.

## Impactos automáticos

- imagens Markdown isoladas são embrulhadas em `figure.book-figure` pelo `lab.js`
- a legenda entra na lista de figuras gerada
- numeração editorial é aplicada no HTML final

## Validação

Se houver geração de asset:

```bash
python3 scripts/generate_scene_assets.py
```

Depois:

```bash
make check-media
make build-pages
```

## Não fazer

- não editar diretamente um asset gerado se a fonte canônica for o script
