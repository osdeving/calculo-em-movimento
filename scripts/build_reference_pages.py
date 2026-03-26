from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = REPO_ROOT / "content"
SUMMARY_PATH = CONTENT_ROOT / "SUMMARY.md"
REFERENCE_ROOT = CONTENT_ROOT / "references"
GLOSSARY_SOURCE = CONTENT_ROOT / "reference_data" / "glossary.json"
THEME_GLOSSARY_JS = REPO_ROOT / "renderers" / "mdbook" / "theme" / "generated_glossary.js"
CONTENT_SKIP_FILES = {"capa.md", "index.md", "como-usar.md", "plano-de-acao.md"}
REMISSIVE_SKIP_FILES = {
    "capa.md",
    "index.md",
    "como-usar.md",
    "plano-de-acao.md",
    "21-mini-resumo-das-regras-de-calculo-que-realmente-usamos-aqui.md",
    "22-folha-de-consulta-compacta.md",
    "23-exercicios-propostos.md",
    "24-gabarito-dos-exercicios.md",
}
MAX_INDEX_REFERENCES = 12

SUMMARY_LINK_RE = re.compile(r"^\s*-\s+\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FIGURE_START_RE = re.compile(r"<figure\b", re.IGNORECASE)
FIGURE_END_RE = re.compile(r"</figure>", re.IGNORECASE)
FIGCAPTION_RE = re.compile(r"<figcaption>(.*?)</figcaption>", re.IGNORECASE | re.DOTALL)
SOURCE_RE = re.compile(r'<source[^>]+src="([^"]+)"', re.IGNORECASE)
IMG_TAG_RE = re.compile(r'<img[^>]+src="([^"]+)"', re.IGNORECASE)
MARKDOWN_IMAGE_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
FORMULA_MARKER_RE = re.compile(r"<!--\s*formula:\s*(.*?)\s*-->")
HTML_TAG_RE = re.compile(r"<[^>]+>")
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FORMAT_MARKER_RE = re.compile(r"[*_`>#\[\]\(\)!]")


@dataclass
class SectionRef:
    title: str
    anchor: str | None
    text: str


@dataclass
class MediaItem:
    kind: str
    editorial_label: str
    caption: str
    asset_path: str
    chapter_title: str
    chapter_label: str | None
    section_title: str
    source_path: Path
    anchor: str | None


@dataclass
class FormulaItem:
    title: str
    latex: str
    chapter_title: str
    section_title: str
    source_path: Path
    anchor: str | None


def slugify_heading(text: str) -> str:
    slug = text.strip().lower()
    slug = slug.replace(".", "")
    slug = re.sub(r"[^\w\s-]", "", slug, flags=re.UNICODE)
    slug = re.sub(r"\s+", "-", slug, flags=re.UNICODE)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def extract_chapter_label(chapter_title: str) -> str | None:
    numeric_match = re.match(r"^(\d+)\.", chapter_title)
    if numeric_match:
        return numeric_match.group(1)

    appendix_match = re.match(r"^Apêndice\s+([A-Z])\.", chapter_title)
    if appendix_match:
        return appendix_match.group(1)

    return None


def relative_md_link(source_path: Path, anchor: str | None = None) -> str:
    relative = source_path.relative_to(CONTENT_ROOT).as_posix()
    if source_path.parent == REFERENCE_ROOT:
        return f"./{source_path.name}#{anchor}" if anchor else f"./{source_path.name}"
    link = f"../{relative}"
    return f"{link}#{anchor}" if anchor else link


def strip_markup(text: str) -> str:
    cleaned = COMMENT_RE.sub(" ", text)
    cleaned = HTML_TAG_RE.sub(" ", cleaned)
    cleaned = FORMAT_MARKER_RE.sub(" ", cleaned)
    cleaned = cleaned.replace("\\", " ")
    cleaned = re.sub(r"\$\$.*?\$\$", " ", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"\$.*?\$", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned, flags=re.UNICODE)
    return cleaned.strip()


def clean_caption(text: str) -> str:
    cleaned = COMMENT_RE.sub(" ", text)
    cleaned = HTML_TAG_RE.sub(" ", cleaned)
    cleaned = cleaned.replace("**", " ")
    cleaned = cleaned.replace("*", " ")
    cleaned = cleaned.replace("_", " ")
    cleaned = re.sub(r"\s+", " ", cleaned, flags=re.UNICODE)
    return cleaned.strip()


def extract_display_math(lines: list[str], start_index: int) -> tuple[str | None, int]:
    index = start_index
    while index < len(lines) and not lines[index].strip():
        index += 1

    if index >= len(lines):
        return None, index

    line = lines[index].strip()
    if line.startswith("$$") and line.endswith("$$") and len(line) > 4:
        return line[2:-2].strip(), index + 1

    if line != "$$":
        return None, index

    index += 1
    formula_lines: list[str] = []
    while index < len(lines):
        current = lines[index].strip()
        if current == "$$":
            return "\n".join(formula_lines).strip(), index + 1
        formula_lines.append(lines[index])
        index += 1

    return None, index


def parse_summary_paths() -> list[Path]:
    paths: list[Path] = []
    for line in SUMMARY_PATH.read_text(encoding="utf-8").splitlines():
        match = SUMMARY_LINK_RE.match(line)
        if not match:
            continue
        raw_path = match.group(1)
        if not raw_path.endswith(".md"):
            continue
        path = (CONTENT_ROOT / raw_path).resolve()
        if REFERENCE_ROOT in path.parents or path.parent == REFERENCE_ROOT:
            continue
        if path.name == "SUMMARY.md":
            continue
        if path.name in CONTENT_SKIP_FILES:
            continue
        paths.append(path)
    return paths


def section_link(source_path: Path, anchor: str | None) -> str:
    return relative_md_link(source_path, anchor)


def scan_chapter(source_path: Path) -> tuple[str, str | None, list[SectionRef], list[MediaItem], list[MediaItem], list[FormulaItem]]:
    lines = source_path.read_text(encoding="utf-8").splitlines()
    chapter_title = source_path.stem
    for line in lines:
        match = HEADING_RE.match(line)
        if match and len(match.group(1)) == 1:
            chapter_title = match.group(2).strip()
            break
    chapter_label = extract_chapter_label(chapter_title)

    current_section_title = chapter_title
    current_anchor: str | None = None
    current_section_lines: list[str] = []
    sections: list[SectionRef] = []
    figures: list[MediaItem] = []
    videos: list[MediaItem] = []
    formulas: list[FormulaItem] = []
    figure_counter = 0
    video_counter = 0

    index = 0
    while index < len(lines):
        line = lines[index]

        heading_match = HEADING_RE.match(line)
        if heading_match:
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()
            if level >= 2:
                sections.append(
                    SectionRef(
                        title=current_section_title,
                        anchor=current_anchor,
                        text=strip_markup("\n".join(current_section_lines)),
                    )
                )
                current_section_title = heading_text
                current_anchor = slugify_heading(heading_text)
                current_section_lines = [line]
                index += 1
                continue
            current_section_lines.append(line)
            index += 1
            continue

        formula_match = FORMULA_MARKER_RE.match(line.strip())
        if formula_match:
            title = formula_match.group(1).strip()
            latex, next_index = extract_display_math(lines, index + 1)
            if latex:
                formulas.append(
                    FormulaItem(
                        title=title,
                        latex=latex,
                        chapter_title=chapter_title,
                        section_title=current_section_title,
                        source_path=source_path,
                        anchor=current_anchor,
                    )
                )
            current_section_lines.append(line)
            index = max(next_index, index + 1)
            continue

        if FIGURE_START_RE.search(line):
            block_lines = [line]
            index += 1
            while index < len(lines):
                block_lines.append(lines[index])
                if FIGURE_END_RE.search(lines[index]):
                    index += 1
                    break
                index += 1

            block = "\n".join(block_lines)
            caption_match = FIGCAPTION_RE.search(block)
            caption = clean_caption(caption_match.group(1)) if caption_match else "Figura sem legenda"
            asset_match = SOURCE_RE.search(block) or IMG_TAG_RE.search(block)
            asset_path = asset_match.group(1) if asset_match else ""
            is_video = "<video" in block.lower()
            target = videos if is_video else figures
            if is_video:
                video_counter += 1
                kind = "Vídeo"
                editorial_label = f"Vídeo {chapter_label}.{video_counter}" if chapter_label else f"Vídeo {video_counter}"
            else:
                figure_counter += 1
                kind = "Figura"
                editorial_label = f"Figura {chapter_label}.{figure_counter}" if chapter_label else f"Figura {figure_counter}"
            target.append(
                MediaItem(
                    kind=kind,
                    editorial_label=editorial_label,
                    caption=caption,
                    asset_path=asset_path,
                    chapter_title=chapter_title,
                    chapter_label=chapter_label,
                    section_title=current_section_title,
                    source_path=source_path,
                    anchor=current_anchor,
                )
            )
            current_section_lines.extend(block_lines)
            continue

        image_match = MARKDOWN_IMAGE_RE.search(line)
        if image_match:
            figure_counter += 1
            figures.append(
                MediaItem(
                    kind="Figura",
                    editorial_label=f"Figura {chapter_label}.{figure_counter}" if chapter_label else f"Figura {figure_counter}",
                    caption=image_match.group(1).strip() or "Imagem sem legenda",
                    asset_path=image_match.group(2).strip(),
                    chapter_title=chapter_title,
                    chapter_label=chapter_label,
                    section_title=current_section_title,
                    source_path=source_path,
                    anchor=current_anchor,
                )
            )

        current_section_lines.append(line)
        index += 1

    sections.append(
        SectionRef(
            title=current_section_title,
            anchor=current_anchor,
            text=strip_markup("\n".join(current_section_lines)),
        )
    )

    return chapter_title, chapter_label, sections, figures, videos, formulas


def load_glossary() -> list[dict]:
    return json.loads(GLOSSARY_SOURCE.read_text(encoding="utf-8"))


def term_pattern(term: str) -> re.Pattern[str]:
    escaped = re.escape(term.lower())
    escaped = escaped.replace(r"\ ", r"\s+")
    return re.compile(rf"(?<!\w){escaped}(?!\w)", flags=re.IGNORECASE | re.UNICODE)


def build_index(
    glossary_terms: list[dict],
    chapter_data: list[tuple[str, str | None, list[SectionRef], list[MediaItem], list[MediaItem], list[FormulaItem], Path]],
) -> dict[str, list[tuple[str, str, str]]]:
    index_map: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for term in glossary_terms:
        patterns = [term_pattern(term["term"])]
        for alias in term.get("aliases", []):
            patterns.append(term_pattern(alias))

        seen_links: set[str] = set()
        for chapter_title, _chapter_label, sections, _figures, _videos, _formulas, source_path in chapter_data:
            if source_path.name in REMISSIVE_SKIP_FILES:
                continue
            for section in sections:
                if not section.anchor:
                    continue
                haystack = section.text.lower()
                if not haystack:
                    continue
                if any(pattern.search(haystack) for pattern in patterns):
                    link = section_link(source_path, section.anchor)
                    if link in seen_links:
                        continue
                    seen_links.add(link)
                    index_map[term["term"]].append((chapter_title, section.title, link))
    return dict(sorted(index_map.items(), key=lambda item: item[0].lower()))


def write_page(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_glossary_js(glossary: list[dict]) -> None:
    payload = []
    for entry in glossary:
        payload.append(
            {
                "term": entry["term"],
                "slug": slugify_heading(entry["term"]),
                "definition": entry["definition"].strip(),
                "aliases": entry.get("aliases", []),
            }
        )
    THEME_GLOSSARY_JS.write_text(
        "window.BOOK_GLOSSARY = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )


def render_reference_home(figures: list[MediaItem], videos: list[MediaItem], formulas: list[FormulaItem], glossary: list[dict], index_map: dict[str, list[tuple[str, str, str]]]) -> str:
    return f"""# Guias de consulta

> Página gerada automaticamente pelo pipeline editorial do livro.

Esta área reúne atalhos de navegação para consulta rápida do material.

- [Lista de figuras](lista-de-figuras.md)
- [Lista de vídeos](lista-de-videos.md)
- [Lista de fórmulas](lista-de-formulas.md)
- [Glossário](glossario.md)
- [Índice remissivo](indice-remissivo.md)

## O que você encontra aqui

- **Figuras**: {len(figures)} entradas com legenda e capítulo de origem.
- **Vídeos**: {len(videos)} animações integradas ao texto.
- **Fórmulas**: {len(formulas)} fórmulas principais marcadas editorialmente.
- **Glossário**: {len(glossary)} termos-base do curso.
- **Índice remissivo**: {len(index_map)} termos com ocorrências linkáveis no corpo do livro.

## Como manter isso atualizado

- para incluir uma fórmula na lista, adicione um comentário `<!-- formula: Título -->` logo antes do bloco `$$ ... $$`
- para ampliar o glossário e o índice, edite `content/reference_data/glossary.json`
- depois rode `make build` ou `make serve`
"""


def render_media_list(title: str, intro: str, items: list[MediaItem]) -> str:
    lines = [
        f"# {title}",
        "",
        "> Página gerada automaticamente pelo pipeline editorial do livro.",
        "",
        intro,
        "",
    ]
    for number, item in enumerate(items, start=1):
        lines.append(f"{number}. [{item.editorial_label}. {item.caption}]({section_link(item.source_path, item.anchor)})")
        lines.append(f"   Em: **{item.chapter_title}**, seção **{item.section_title}**.")
        if item.asset_path:
            lines.append(f"   Asset: `{item.asset_path}`.")
        lines.append("")
    return "\n".join(lines)


def render_formula_list(formulas: list[FormulaItem]) -> str:
    lines = [
        "# Lista de fórmulas",
        "",
        "> Página gerada automaticamente pelo pipeline editorial do livro.",
        "",
        "Esta lista mostra apenas as fórmulas marcadas como centrais no texto, com link direto para a seção em que elas são apresentadas ou justificadas.",
        "",
    ]
    for number, formula in enumerate(formulas, start=1):
        lines.append(f"## {number}. {formula.title}")
        lines.append("")
        lines.append(f"Origem: [{formula.chapter_title} | {formula.section_title}]({section_link(formula.source_path, formula.anchor)})")
        lines.append("")
        lines.append("$$")
        lines.append(formula.latex)
        lines.append("$$")
        lines.append("")
    return "\n".join(lines)


def render_glossary(glossary: list[dict]) -> str:
    lines = [
        "# Glossário",
        "",
        "> Página gerada automaticamente a partir de `content/reference_data/glossary.json`.",
        "",
        "Os termos abaixo são os conceitos-base usados ao longo do livro.",
        "",
    ]
    for entry in sorted(glossary, key=lambda item: item["term"].lower()):
        anchor = slugify_heading(entry["term"])
        lines.append(f"## <a id=\"{anchor}\"></a>{entry['term']}")
        lines.append("")
        lines.append(entry["definition"].strip())
        if entry.get("aliases"):
            lines.append("")
            lines.append(f"Aliases: `{', '.join(entry['aliases'])}`.")
        if entry.get("see"):
            refs = ", ".join(f"[{term}](glossario.md#{slugify_heading(term)})" for term in entry["see"])
            lines.append("")
            lines.append(f"Veja também: {refs}.")
        lines.append("")
    return "\n".join(lines)


def render_index(glossary: list[dict], index_map: dict[str, list[tuple[str, str, str]]]) -> str:
    lines = [
        "# Índice remissivo",
        "",
        "> Página gerada automaticamente a partir dos termos do glossário e das ocorrências encontradas nas seções do livro.",
        "",
    ]
    current_letter = None
    glossary_lookup = {entry["term"]: entry for entry in glossary}
    for term, refs in index_map.items():
        first_letter = term[0].upper()
        if first_letter != current_letter:
            current_letter = first_letter
            lines.append(f"## {current_letter}")
            lines.append("")

        glossary_link = f"[definição](glossario.md#{slugify_heading(term)})"
        visible_refs = refs[:MAX_INDEX_REFERENCES]
        hidden_count = max(len(refs) - len(visible_refs), 0)
        ref_links = ", ".join(f"[{section}]({link})" for _chapter, section, link in visible_refs)
        line = f"- **{term}** ({glossary_link}): {ref_links}"
        entry = glossary_lookup.get(term, {})
        if entry.get("see"):
            see_links = ", ".join(f"[{item}](glossario.md#{slugify_heading(item)})" for item in entry["see"])
            line += f". Veja também: {see_links}"
        if hidden_count:
            line += f". (+{hidden_count} ocorrências adicionais omitidas)"
        lines.append(line)
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    chapter_paths = parse_summary_paths()
    chapter_data: list[tuple[str, str | None, list[SectionRef], list[MediaItem], list[MediaItem], list[FormulaItem], Path]] = []
    all_figures: list[MediaItem] = []
    all_videos: list[MediaItem] = []
    all_formulas: list[FormulaItem] = []

    for path in chapter_paths:
        chapter_title, chapter_label, sections, figures, videos, formulas = scan_chapter(path)
        chapter_data.append((chapter_title, chapter_label, sections, figures, videos, formulas, path))
        all_figures.extend(figures)
        all_videos.extend(videos)
        all_formulas.extend(formulas)

    glossary = load_glossary()
    index_map = build_index(glossary, chapter_data)
    write_glossary_js(glossary)

    write_page(
        REFERENCE_ROOT / "index.md",
        render_reference_home(all_figures, all_videos, all_formulas, glossary, index_map),
    )
    write_page(
        REFERENCE_ROOT / "lista-de-figuras.md",
        render_media_list(
            "Lista de figuras",
            "As figuras abaixo apontam para a seção em que aparecem no texto.",
            all_figures,
        ),
    )
    write_page(
        REFERENCE_ROOT / "lista-de-videos.md",
        render_media_list(
            "Lista de vídeos",
            "Os vídeos abaixo apontam para a seção em que a animação é usada pedagogicamente.",
            all_videos,
        ),
    )
    write_page(REFERENCE_ROOT / "lista-de-formulas.md", render_formula_list(all_formulas))
    write_page(REFERENCE_ROOT / "glossario.md", render_glossary(glossary))
    write_page(REFERENCE_ROOT / "indice-remissivo.md", render_index(glossary, index_map))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
