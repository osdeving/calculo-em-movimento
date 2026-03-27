# Pipeline: usar tecnica Manim da galeria

Use este playbook quando a tarefa pedir uma animacao mais rica e voce quiser partir de uma tecnica ja mapeada na documentacao oficial do Manim.

## Fonte de verdade

- `animations/manim/recipes/*.py`
- `animations/manim/*.py`
- `animations/manim/book_motion.py`

## Passos

1. Identifique a tecnica dominante da cena.
   - cascata e ritmo: `composition_recipes.py`
   - morphing e continuidade: `transform_recipes.py`
   - guiar o olhar: `highlight_recipes.py`
   - trajetoria e rastro: `motion_recipes.py`
   - elementos vivos com tracker: `tracker_recipes.py`
2. Copie a receita minima para a cena real e adapte nomes, tempos e cores.
3. Mova para `book_motion.py` apenas componentes visuais recorrentes; nao leve para la animacoes que so fazem sentido em uma cena.
4. Se a cena virar artefato publicado do livro:
   - registre em `scripts/render_manim_assets.py`
   - renderize o video em `content/media/manim/`
   - embuta o video no capitulo com `<figure>`, `<video>` e `<figcaption>`
5. Se a nova cena introduzir um conceito central, avalie se precisa de formula marcada ou termo novo no glossario.

## Regras rapidas

- prefira adaptar uma receita local antes de abrir um branco total
- preserve a paleta escura e a legibilidade do livro
- controle `run_time` e `lag_ratio` com intencao; efeitos ricos nao podem virar ruído
- efeitos de destaque devem servir ao conceito, nao competir com ele

## Validacao

```bash
python3 -m py_compile animations/manim/*.py animations/manim/recipes/*.py scripts/render_manim_assets.py
```

Se a tecnica virou um video novo do livro, complete com:

```bash
python3 scripts/render_manim_assets.py
make build-pages
```

