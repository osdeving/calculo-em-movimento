.PHONY: assets animations references media build build-pages publish serve serve-stop clean

BOOK_DIR := renderers/mdbook

references:
	python3 scripts/build_reference_pages.py

assets:
	python3 scripts/generate_scene_assets.py

animations:
	python3 scripts/render_manim_assets.py

media: assets animations

build: references media
	mdbook build $(BOOK_DIR)

build-pages: references
	mdbook build $(BOOK_DIR)
	touch dist/book/.nojekyll

publish:
	gh workflow run publish-pages.yml --ref main

serve: references media
	python3 scripts/serve_mdbook.py

serve-stop:
	python3 scripts/serve_mdbook.py --stop

clean:
	python3 scripts/serve_mdbook.py --stop || true
	rm -rf dist
