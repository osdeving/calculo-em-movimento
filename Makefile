.PHONY: assets animations media build build-pages publish serve serve-stop clean

BOOK_DIR := renderers/mdbook

assets:
	python3 scripts/generate_scene_assets.py

animations:
	python3 scripts/render_manim_assets.py

media: assets animations

build: media
	mdbook build $(BOOK_DIR)

build-pages:
	mdbook build $(BOOK_DIR)
	touch dist/book/.nojekyll

publish:
	gh workflow run publish-pages.yml --ref main

serve: media
	python3 scripts/serve_mdbook.py

serve-stop:
	python3 scripts/serve_mdbook.py --stop

clean:
	python3 scripts/serve_mdbook.py --stop || true
	rm -rf dist
