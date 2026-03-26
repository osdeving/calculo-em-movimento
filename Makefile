.PHONY: assets build serve clean

BOOK_DIR := renderers/mdbook

assets:
	python3 scripts/generate_scene_assets.py

build: assets
	mdbook build $(BOOK_DIR)

serve: assets
	mdbook serve $(BOOK_DIR) -n 0.0.0.0 -p 3000

clean:
	rm -rf dist
