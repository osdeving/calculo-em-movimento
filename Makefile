.PHONY: assets build serve serve-stop clean

BOOK_DIR := renderers/mdbook

assets:
	python3 scripts/generate_scene_assets.py

build: assets
	mdbook build $(BOOK_DIR)

serve: assets
	python3 scripts/serve_mdbook.py

serve-stop:
	python3 scripts/serve_mdbook.py --stop

clean:
	python3 scripts/serve_mdbook.py --stop || true
	rm -rf dist
