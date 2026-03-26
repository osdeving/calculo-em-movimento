from __future__ import annotations

import html
import json
import re
import sys


FENCE_RE = re.compile(r"^\s*```")
DISPLAY_INLINE_RE = re.compile(r"(?<!\\)\$\$(.+?)(?<!\\)\$\$")
INLINE_RE = re.compile(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$(?!\$)")


def replace_inline_math(line: str) -> str:
    def _display(match: re.Match[str]) -> str:
        expr = html.escape(match.group(1).strip(), quote=True)
        return f'<span class="display-math-inline" data-math-display="{expr}"></span>'

    def _inline(match: re.Match[str]) -> str:
        expr = html.escape(match.group(1).strip(), quote=True)
        return f'<span class="inline-math" data-math-inline="{expr}"></span>'

    line = DISPLAY_INLINE_RE.sub(_display, line)
    line = INLINE_RE.sub(_inline, line)
    return line


def convert_math_delimiters(markdown: str) -> str:
    lines = markdown.splitlines()
    result: list[str] = []
    in_fence = False
    in_display_block = False
    display_lines: list[str] = []

    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            result.append(line)
            continue

        if in_fence:
            result.append(line)
            continue

        if line.strip() == "$$":
            if not in_display_block:
                in_display_block = True
                display_lines = []
            else:
                result.append('<div class="display-math">')
                result.append(r"\[")
                result.extend(display_lines)
                result.append(r"\]")
                result.append("</div>")
                in_display_block = False
                display_lines = []
            continue

        if in_display_block:
            display_lines.append(line)
            continue

        result.append(replace_inline_math(line))

    return "\n".join(result) + ("\n" if markdown.endswith("\n") else "")


def visit_items(items: list[dict]) -> None:
    for item in items:
        chapter = item.get("Chapter")
        if chapter:
            chapter["content"] = convert_math_delimiters(chapter["content"])
            visit_items(chapter.get("sub_items", []))


def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] == "supports":
        return 0 if len(argv) > 2 and argv[2] == "html" else 1

    context, book = json.load(sys.stdin)
    visit_items(book.get("sections", []))
    json.dump(book, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
