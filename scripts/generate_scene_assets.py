from __future__ import annotations

import re
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "content" / "assets"


PAPER = "#f6f1e6"
PAPER_DARK = "#efe5d2"
INK = "#2a2926"
MUTED = "#665f56"
ACCENT = "#8b5e34"
ACCENT_SOFT = "#d8c1a2"
NIGHT = "#13202d"
NIGHT_SOFT = "#203244"
NIGHT_PANEL = "#182734"
SKY = "#dae9f3"
ROAD = "#5d6166"
ROAD_EDGE = "#484c50"
BLUE = "#4c78a8"
BLUE_SOFT = "#8eb6d9"
RED = "#cc5a4e"
GREEN = "#5e8f62"
YELLOW = "#d4a544"
ORANGE = "#d98943"
GRAY = "#8b9098"
DARK = "#30363b"
BOX = "#d6ab73"

plt.rcParams["svg.hashsalt"] = "calculo-em-movimento"


def ensure_dirs() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)


def setup_scene(title: str):
    fig, ax = plt.subplots(figsize=(10.5, 4.2))
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 42)
    ax.axis("off")

    ax.add_patch(Rectangle((1, 1), 98, 40, facecolor=PAPER, edgecolor=ACCENT_SOFT, linewidth=1.4))
    ax.add_patch(
        FancyBboxPatch(
            (4, 35.2),
            30,
            4.2,
            boxstyle="round,pad=0.25,rounding_size=1.1",
            facecolor=PAPER_DARK,
            edgecolor="none",
        )
    )
    ax.text(6, 37.1, title, fontsize=12, fontweight="bold", color=INK, va="center")
    return fig, ax


def setup_cover_scene():
    fig, ax = plt.subplots(figsize=(8.4, 10.6))
    fig.patch.set_facecolor(NIGHT)
    ax.set_facecolor(NIGHT)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 130)
    ax.axis("off")

    ax.add_patch(
        FancyBboxPatch(
            (2, 2),
            96,
            126,
            boxstyle="round,pad=0.8,rounding_size=4.0",
            facecolor=NIGHT,
            edgecolor=ACCENT_SOFT,
            linewidth=1.6,
        )
    )
    ax.add_patch(Polygon([[2, 128], [98, 128], [98, 74], [48, 88]], facecolor=NIGHT_SOFT, edgecolor="none"))
    ax.add_patch(Polygon([[2, 2], [2, 70], [42, 60], [98, 42], [98, 2]], facecolor=NIGHT_PANEL, edgecolor="none"))
    ax.add_patch(Circle((83, 113), 9.0, facecolor="#e9be76", edgecolor="none", alpha=0.18))
    ax.add_patch(Circle((14, 114), 11.0, facecolor="#b7d7ef", edgecolor="none", alpha=0.08))

    for y in range(18, 118, 10):
        ax.plot([9, 91], [y, y], color="#9fb7c8", linewidth=0.35, alpha=0.08)
    for x in range(12, 92, 10):
        ax.plot([x, x], [16, 120], color="#9fb7c8", linewidth=0.35, alpha=0.08)

    return fig, ax


def save_scene(fig, filename: str, png_filename: str | None = None) -> None:
    fig.tight_layout(pad=0.4)
    target = ASSET_DIR / filename
    temp_target = ASSET_DIR / (filename + ".tmp")
    fig.savefig(temp_target, format="svg", metadata={"Date": "2026-03-26T00:00:00"})

    if png_filename:
        png_target = ASSET_DIR / png_filename
        fig.savefig(
            png_target,
            format="png",
            dpi=220,
            facecolor=fig.get_facecolor(),
            edgecolor="none",
            metadata={"Software": "Matplotlib"},
        )
    plt.close(fig)

    svg_text = temp_target.read_text(encoding="utf-8")
    svg_text = re.sub(
        r"<dc:date>.*?</dc:date>",
        "<dc:date>2026-03-26T00:00:00</dc:date>",
        svg_text,
        flags=re.S,
    )

    current = target.read_text(encoding="utf-8") if target.exists() else None
    if current != svg_text:
        target.write_text(svg_text, encoding="utf-8")

    temp_target.unlink()


def draw_s_axis(ax, max_s: float, step: float, y: float = 7.0, label: str = "S (m)"):
    x0, x1 = 8.0, 92.0
    ax.add_patch(
        FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>", mutation_scale=12, linewidth=1.4, color=INK)
    )
    tick = 0.0
    while tick <= max_s + 1e-9:
        x = x0 + (x1 - x0) * tick / max_s
        ax.plot([x, x], [y - 1.1, y + 1.1], color=INK, linewidth=1.0)
        ax.text(x, y - 3.2, f"{tick:g}", fontsize=8, color=MUTED, ha="center", va="top")
        tick += step
    ax.text(x1 + 1.2, y + 0.2, label, fontsize=9, fontweight="bold", color=INK)
    return lambda s: x0 + (x1 - x0) * s / max_s


def draw_ground(ax, y: float = 11.5, height: float = 5.0):
    ax.add_patch(Rectangle((8, y), 84, height, facecolor=ROAD, edgecolor=ROAD_EDGE, linewidth=1.0))
    ax.plot([8, 92], [y + height, y + height], color="#d7d9dc", linewidth=1.0, alpha=0.7)


def draw_factory(ax, x: float = 10, y: float = 19):
    ax.add_patch(Rectangle((x, y), 11, 10, facecolor=BLUE_SOFT, edgecolor=INK, linewidth=1.1))
    ax.add_patch(Polygon([[x, y + 10], [x + 2.4, y + 13], [x + 4.8, y + 10], [x + 7.2, y + 13], [x + 9.6, y + 10], [x + 11, y + 10]], facecolor=BLUE, edgecolor=INK, linewidth=1.1))
    ax.add_patch(Rectangle((x + 8.4, y + 7.5), 1.5, 6.5, facecolor=GRAY, edgecolor=INK, linewidth=1.0))


def draw_post(ax, x: float, y: float = 12.2, label: str | None = None):
    ax.add_patch(Rectangle((x - 0.3, y), 0.6, 12.8, facecolor=GRAY, edgecolor=INK, linewidth=0.8))
    ax.add_patch(FancyBboxPatch((x - 2.5, y + 9.6), 5.0, 2.2, boxstyle="round,pad=0.2,rounding_size=0.4", facecolor=PAPER_DARK, edgecolor=INK, linewidth=0.9))
    if label:
        ax.text(x, y + 10.7, label, fontsize=8, ha="center", va="center", color=INK)


def draw_marker_label(ax, x: float, y: float, text: str, fc: str = PAPER_DARK):
    ax.add_patch(FancyBboxPatch((x - 4.6, y - 1.2), 9.2, 2.4, boxstyle="round,pad=0.25,rounding_size=0.5", facecolor=fc, edgecolor="none"))
    ax.text(x, y, text, fontsize=8, ha="center", va="center", color=INK)


def draw_box(ax, x: float, y: float, scale: float = 1.0, alpha: float = 1.0):
    w, h = 5.4 * scale, 4.0 * scale
    ax.add_patch(Rectangle((x - w / 2, y), w, h, facecolor=BOX, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.add_patch(Polygon([[x - w / 2, y + h], [x, y + h + 1.2 * scale], [x + w / 2, y + h], [x, y + h - 1.0 * scale]], facecolor="#e6c392", edgecolor=INK, linewidth=0.8, alpha=alpha))
    ax.plot([x, x], [y, y + h], color="#8f6a3d", linewidth=0.8, alpha=alpha)


def draw_apple(ax, x: float, y: float, scale: float = 1.0, alpha: float = 1.0, zorder: float = 6):
    radius = 1.45 * scale
    ax.add_patch(Circle((x - 0.8 * scale, y), radius, facecolor=RED, edgecolor=INK, linewidth=0.7, alpha=alpha, zorder=zorder))
    ax.add_patch(Circle((x + 0.8 * scale, y), radius, facecolor=RED, edgecolor=INK, linewidth=0.7, alpha=alpha, zorder=zorder))
    ax.add_patch(Polygon([[x - 1.4 * scale, y - 1.2 * scale], [x + 1.4 * scale, y - 1.2 * scale], [x, y + 1.8 * scale]], facecolor=RED, edgecolor=RED, linewidth=0.7, alpha=alpha, zorder=zorder))
    ax.plot([x, x + 0.2 * scale], [y + 1.6 * scale, y + 3.2 * scale], color=ACCENT_SOFT, linewidth=0.9, alpha=alpha, zorder=zorder + 0.1)
    ax.add_patch(Polygon([[x + 0.2 * scale, y + 2.6 * scale], [x + 2.0 * scale, y + 3.6 * scale], [x + 0.8 * scale, y + 4.6 * scale]], facecolor=GREEN, edgecolor="none", alpha=alpha, zorder=zorder + 0.1))


def draw_tree(ax, x: float, y: float, scale: float = 1.0):
    ax.add_patch(FancyBboxPatch((x - 2.2 * scale, y), 4.4 * scale, 20.0 * scale, boxstyle="round,pad=0.2,rounding_size=1.0", facecolor=ACCENT, edgecolor=INK, linewidth=1.0))
    canopy = [
        (x - 7.5, y + 20.0, 6.2),
        (x - 1.0, y + 23.0, 7.0),
        (x + 6.5, y + 21.5, 6.5),
        (x - 4.0, y + 28.0, 6.2),
        (x + 3.8, y + 28.8, 6.5),
    ]
    for cx, cy, radius in canopy:
        ax.add_patch(Circle((cx * scale + x * (1 - scale), cy * scale + y * (1 - scale)), radius * scale, facecolor=GREEN, edgecolor=INK, linewidth=0.8))
    apples = [
        (x - 6.8 * scale, y + 21.5 * scale),
        (x - 2.4 * scale, y + 26.0 * scale),
        (x + 3.6 * scale, y + 22.4 * scale),
        (x + 7.0 * scale, y + 18.6 * scale),
    ]
    for axp, ayp in apples:
        draw_apple(ax, axp, ayp, scale=0.5 * scale)


def draw_car(ax, x: float, y: float, scale: float = 1.0, color: str = BLUE, alpha: float = 1.0):
    ax.add_patch(FancyBboxPatch((x - 5.3 * scale, y + 2.3 * scale), 10.6 * scale, 3.2 * scale, boxstyle="round,pad=0.15,rounding_size=1.0", facecolor=color, edgecolor=INK, linewidth=1.1, alpha=alpha))
    ax.add_patch(Polygon([[x - 3.5 * scale, y + 5.5 * scale], [x - 1.2 * scale, y + 8.0 * scale], [x + 2.8 * scale, y + 8.0 * scale], [x + 4.4 * scale, y + 5.5 * scale]], facecolor=color, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.add_patch(Polygon([[x - 1.0 * scale, y + 7.4 * scale], [x + 2.0 * scale, y + 7.4 * scale], [x + 3.3 * scale, y + 5.8 * scale], [x - 0.2 * scale, y + 5.8 * scale]], facecolor=SKY, edgecolor="none", alpha=0.9 * alpha))
    for dx in (-3.3, 3.2):
        ax.add_patch(Circle((x + dx * scale, y + 2.0 * scale), 1.25 * scale, facecolor=DARK, edgecolor=INK, linewidth=1.0, alpha=alpha))
        ax.add_patch(Circle((x + dx * scale, y + 2.0 * scale), 0.55 * scale, facecolor="#d8dade", edgecolor="none", alpha=alpha))


def draw_cart(ax, x: float, y: float, scale: float = 1.0, color: str = GREEN, alpha: float = 1.0):
    ax.add_patch(Rectangle((x - 4.5 * scale, y + 2.4 * scale), 9.0 * scale, 3.0 * scale, facecolor=color, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.add_patch(Rectangle((x - 1.0 * scale, y + 5.4 * scale), 2.0 * scale, 2.0 * scale, facecolor=color, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.plot([x + 1.0 * scale, x + 3.8 * scale], [y + 7.4 * scale, y + 9.0 * scale], color=INK, linewidth=1.0, alpha=alpha)
    for dx in (-2.8, 2.8):
        ax.add_patch(Circle((x + dx * scale, y + 2.2 * scale), 1.15 * scale, facecolor=DARK, edgecolor=INK, linewidth=1.0, alpha=alpha))
        ax.add_patch(Circle((x + dx * scale, y + 2.2 * scale), 0.45 * scale, facecolor="#d8dade", edgecolor="none", alpha=alpha))


def draw_motorcycle(ax, x: float, y: float, scale: float = 1.0, color: str = RED, alpha: float = 1.0):
    for dx in (-3.6, 3.2):
        ax.add_patch(Circle((x + dx * scale, y + 1.8 * scale), 1.35 * scale, facecolor=DARK, edgecolor=INK, linewidth=1.0, alpha=alpha))
        ax.add_patch(Circle((x + dx * scale, y + 1.8 * scale), 0.55 * scale, facecolor="#d8dade", edgecolor="none", alpha=alpha))
    ax.plot([x - 3.0 * scale, x - 0.8 * scale, x + 1.0 * scale, x + 3.2 * scale], [y + 1.8 * scale, y + 4.7 * scale, y + 4.8 * scale, y + 1.8 * scale], color=INK, linewidth=1.2, alpha=alpha)
    ax.plot([x - 0.8 * scale, x + 0.6 * scale], [y + 4.7 * scale, y + 6.2 * scale], color=INK, linewidth=1.0, alpha=alpha)
    ax.add_patch(FancyBboxPatch((x - 1.6 * scale, y + 4.2 * scale), 4.0 * scale, 1.3 * scale, boxstyle="round,pad=0.12,rounding_size=0.5", facecolor=color, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.plot([x + 0.9 * scale, x + 2.8 * scale], [y + 6.0 * scale, y + 7.1 * scale], color=INK, linewidth=1.0, alpha=alpha)
    ax.plot([x - 0.8 * scale, x - 2.3 * scale], [y + 6.2 * scale, y + 7.2 * scale], color=INK, linewidth=1.0, alpha=alpha)


def draw_forklift(ax, x: float, y: float, scale: float = 1.0, alpha: float = 1.0):
    ax.add_patch(Rectangle((x - 5.2 * scale, y + 2.2 * scale), 6.2 * scale, 3.8 * scale, facecolor=YELLOW, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.add_patch(Rectangle((x - 2.2 * scale, y + 6.0 * scale), 3.0 * scale, 3.6 * scale, facecolor=YELLOW, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.add_patch(Rectangle((x + 1.0 * scale, y + 2.0 * scale), 0.6 * scale, 10.0 * scale, facecolor=DARK, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.add_patch(Rectangle((x + 2.0 * scale, y + 2.0 * scale), 0.6 * scale, 10.0 * scale, facecolor=DARK, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.add_patch(Rectangle((x + 2.0 * scale, y + 2.5 * scale), 4.2 * scale, 0.5 * scale, facecolor=DARK, edgecolor=INK, linewidth=0.8, alpha=alpha))
    ax.add_patch(Rectangle((x + 2.0 * scale, y + 4.0 * scale), 3.0 * scale, 0.5 * scale, facecolor=DARK, edgecolor=INK, linewidth=0.8, alpha=alpha))
    ax.add_patch(Circle((x - 3.0 * scale, y + 2.0 * scale), 1.2 * scale, facecolor=DARK, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.add_patch(Circle((x + 0.2 * scale, y + 2.0 * scale), 1.2 * scale, facecolor=DARK, edgecolor=INK, linewidth=1.0, alpha=alpha))
    draw_box(ax, x + 6.3 * scale, y + 2.2 * scale, scale=0.9 * scale, alpha=alpha)


def draw_robot(ax, x: float, y: float, scale: float = 1.0, alpha: float = 1.0):
    ax.add_patch(FancyBboxPatch((x - 4.2 * scale, y + 1.6 * scale), 8.4 * scale, 3.4 * scale, boxstyle="round,pad=0.12,rounding_size=0.9", facecolor=BLUE, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.add_patch(FancyBboxPatch((x - 1.7 * scale, y + 5.0 * scale), 3.4 * scale, 4.2 * scale, boxstyle="round,pad=0.15,rounding_size=0.7", facecolor=BLUE_SOFT, edgecolor=INK, linewidth=1.0, alpha=alpha))
    ax.add_patch(Circle((x - 0.6 * scale, y + 7.0 * scale), 0.3 * scale, facecolor=INK, edgecolor="none", alpha=alpha))
    ax.add_patch(Circle((x + 0.6 * scale, y + 7.0 * scale), 0.3 * scale, facecolor=INK, edgecolor="none", alpha=alpha))
    ax.plot([x - 0.8 * scale, x + 0.8 * scale], [y + 5.9 * scale, y + 5.9 * scale], color=INK, linewidth=0.8, alpha=alpha)
    for dx in (-2.8, 2.8):
        ax.add_patch(Circle((x + dx * scale, y + 1.6 * scale), 0.85 * scale, facecolor=DARK, edgecolor=INK, linewidth=0.9, alpha=alpha))


def draw_shelf(ax, x: float, y: float, scale: float = 1.0):
    ax.add_patch(Rectangle((x, y), 3.0 * scale, 12.0 * scale, facecolor="#c8c3ba", edgecolor=INK, linewidth=1.0))
    for offset in (2.5, 5.6, 8.7):
        ax.add_patch(Rectangle((x + 0.3 * scale, y + offset * scale), 2.4 * scale, 0.4 * scale, facecolor=INK, edgecolor="none"))
    draw_box(ax, x + 1.5 * scale, y + 1.0 * scale, scale=0.45 * scale)
    draw_box(ax, x + 1.5 * scale, y + 4.2 * scale, scale=0.45 * scale)
    draw_box(ax, x + 1.5 * scale, y + 7.3 * scale, scale=0.45 * scale)


def draw_traffic_light(ax, x: float, y: float, scale: float = 1.0):
    ax.plot([x, x], [y, y + 10.0 * scale], color=INK, linewidth=2.0)
    ax.add_patch(FancyBboxPatch((x - 1.3 * scale, y + 7.0 * scale), 2.6 * scale, 6.5 * scale, boxstyle="round,pad=0.12,rounding_size=0.5", facecolor=DARK, edgecolor=INK, linewidth=1.0))
    for dy, color in ((12.1, RED), (10.2, YELLOW), (8.3, GREEN)):
        ax.add_patch(Circle((x, y + dy * scale), 0.55 * scale, facecolor=color, edgecolor="none"))


def draw_arrow(ax, x0: float, y0: float, x1: float, y1: float, text: str | None = None):
    ax.add_patch(
        FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="->", mutation_scale=12, linewidth=1.4, color=ACCENT)
    )
    if text:
        ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 1.2, text, fontsize=8, ha="center", color=ACCENT)


def draw_cover_graph_panel(ax, x: float = 54.0, y: float = 70.0, width: float = 36.0, height: float = 40.0):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            width,
            height,
            boxstyle="round,pad=0.4,rounding_size=2.0",
            facecolor="#0e1721",
            edgecolor=ACCENT_SOFT,
            linewidth=1.0,
        )
    )
    for gy in range(1, 6):
        yy = y + gy * height / 6
        ax.plot([x + 3, x + width - 3], [yy, yy], color="#80a2bd", linewidth=0.35, alpha=0.15)
    for gx in range(1, 6):
        xx = x + gx * width / 6
        ax.plot([xx, xx], [y + 3, y + height - 3], color="#80a2bd", linewidth=0.35, alpha=0.15)

    ox, oy = x + 5, y + 6
    ax.add_patch(FancyArrowPatch((ox, oy), (x + width - 4, oy), arrowstyle="-|>", mutation_scale=10, linewidth=1.1, color=PAPER))
    ax.add_patch(FancyArrowPatch((ox, oy), (ox, y + height - 4), arrowstyle="-|>", mutation_scale=10, linewidth=1.1, color=PAPER))
    xs = [ox + t for t in range(0, 24, 2)]
    line = [oy + 0.8 * t for t in range(0, 12)]
    curve = [oy + 0.16 * (t ** 2) for t in range(0, 12)]

    integral_xs = xs[:6]
    integral_line = line[:6]
    area_points = [(integral_xs[0], oy)] + list(zip(integral_xs, integral_line)) + [(integral_xs[-1], oy)]
    ax.add_patch(Polygon(area_points, closed=True, facecolor=BLUE_SOFT, edgecolor="none", alpha=0.16))

    ax.plot(xs, line, color=BLUE_SOFT, linewidth=2.0)
    ax.plot(xs, curve, color=YELLOW, linewidth=2.2)
    ax.plot([ox + 3, ox + 21], [oy + 2.4, oy + 2.4], color=RED, linewidth=1.7)

    tangent_t = 6.0
    tangent_x = ox + 2 * tangent_t
    tangent_y = oy + 0.16 * (tangent_t ** 2)
    tangent_slope = 0.32 * tangent_t
    tangent_span = 4.5
    ax.plot(
        [tangent_x - tangent_span, tangent_x + tangent_span],
        [tangent_y - tangent_slope * tangent_span, tangent_y + tangent_slope * tangent_span],
        color="#f7f1e6",
        linewidth=1.25,
    )
    ax.add_patch(Circle((tangent_x, tangent_y), 0.55, facecolor=PAPER, edgecolor="none"))

    ax.text(ox + 2.7, oy + 9.2, "∫", fontsize=16, color=BLUE_SOFT, fontweight="bold")
    ax.text(tangent_x + 3.4, tangent_y + 5.0, "d/dt", fontsize=7.8, color="#f7f1e6", fontweight="bold")
    ax.text(x + width - 7.5, y + height - 6.4, "x(t)", fontsize=8, color=YELLOW, fontweight="bold")
    ax.text(x + width - 7.5, y + height - 11.8, "v(t)", fontsize=8, color=BLUE_SOFT, fontweight="bold")
    ax.text(x + width - 7.5, y + height - 17.2, "a(t)", fontsize=8, color="#ff8f82", fontweight="bold")


def draw_cover_graph_panel_analysis(ax, x: float = 54.0, y: float = 70.0, width: float = 36.0, height: float = 40.0):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            width,
            height,
            boxstyle="round,pad=0.4,rounding_size=2.0",
            facecolor="#0e1721",
            edgecolor=ACCENT_SOFT,
            linewidth=1.0,
        )
    )
    for gy in range(1, 6):
        yy = y + gy * height / 6
        ax.plot([x + 3, x + width - 3], [yy, yy], color="#80a2bd", linewidth=0.35, alpha=0.15)
    for gx in range(1, 6):
        xx = x + gx * width / 6
        ax.plot([xx, xx], [y + 3, y + height - 3], color="#80a2bd", linewidth=0.35, alpha=0.15)

    ox = x + 4.3
    top_base = y + 25.0
    mid_base = y + 14.0
    low_base = y + 6.5

    ax.add_patch(FancyArrowPatch((ox, y + 4.0), (x + width - 4.0, y + 4.0), arrowstyle="-|>", mutation_scale=10, linewidth=1.0, color=PAPER))
    ax.add_patch(FancyArrowPatch((ox, y + 4.0), (ox, y + height - 4.0), arrowstyle="-|>", mutation_scale=10, linewidth=1.0, color=PAPER))

    top_xs = [ox + t for t in range(0, 24, 2)]
    top_curve = [top_base + 0.13 * (t ** 2) for t in range(0, 12)]
    ax.plot(top_xs, top_curve, color=YELLOW, linewidth=2.0)
    tangent_t = 5.5
    tangent_x = ox + 2 * tangent_t
    tangent_y = top_base + 0.13 * (tangent_t ** 2)
    tangent_slope = 0.26 * tangent_t
    tangent_span = 4.2
    ax.plot(
        [tangent_x - tangent_span, tangent_x + tangent_span],
        [tangent_y - tangent_slope * tangent_span, tangent_y + tangent_slope * tangent_span],
        color="#f7f1e6",
        linewidth=1.2,
    )
    ax.add_patch(Circle((tangent_x, tangent_y), 0.5, facecolor=PAPER, edgecolor="none"))
    ax.text(tangent_x + 2.7, tangent_y + 4.1, "dx/dt", fontsize=7.3, color=PAPER, fontweight="bold")

    rect_xs = [ox + 1.0 + 1.55 * idx for idx in range(14)]
    curve_points_x = [ox + 1.0 + 1.55 * idx for idx in range(15)]
    curve_points_y = [mid_base + 0.16 * idx + 0.03 * (idx ** 2) for idx in range(15)]
    for idx, rx in enumerate(rect_xs):
        rect_height = curve_points_y[idx] - mid_base
        ax.add_patch(Rectangle((rx, mid_base), 1.15, rect_height, facecolor=BLUE_SOFT, edgecolor="none", alpha=0.18))
    ax.plot(curve_points_x, curve_points_y, color=BLUE_SOFT, linewidth=1.9)
    ax.text(ox + 2.0, mid_base + 5.0, "∫ v(t) dt", fontsize=8.6, color=BLUE_SOFT, fontweight="bold")

    ax.plot([ox + 2.0, x + width - 7.0], [low_base + 0.8, low_base + 0.8], color="#ff8f82", linewidth=1.7)
    ax.text(ox + 13.2, low_base + 2.2, "dv/dt", fontsize=7.3, color="#ffb1a9", fontweight="bold")

    ax.text(x + width - 8.0, y + height - 6.0, "x(t)", fontsize=8, color=YELLOW, fontweight="bold")
    ax.text(x + width - 8.0, y + height - 11.4, "v(t)", fontsize=8, color=BLUE_SOFT, fontweight="bold")
    ax.text(x + width - 8.0, y + height - 16.8, "a(t)", fontsize=8, color="#ff8f82", fontweight="bold")


def scene_car_between_posts():
    fig, ax = setup_scene("Leitura de posicao entre postes")
    to_x = draw_s_axis(ax, max_s=80, step=10)
    draw_ground(ax)

    x1 = to_x(30)
    x2 = to_x(66)
    draw_post(ax, x1, label="poste A")
    draw_post(ax, x2, label="poste B")
    ax.plot([x1, x1], [7, 28], color=ACCENT_SOFT, linewidth=1.0, linestyle="--")
    ax.plot([x2, x2], [7, 28], color=ACCENT_SOFT, linewidth=1.0, linestyle="--")
    draw_car(ax, x1, 12.0, scale=0.85, color=GRAY, alpha=0.45)
    draw_car(ax, x2, 12.0, scale=0.85, color=BLUE, alpha=1.0)
    draw_arrow(ax, x1 + 6, 26.5, x2 - 4, 26.5, "intervalo observado")
    draw_marker_label(ax, x1, 30.5, "t = 2 s")
    draw_marker_label(ax, x2, 30.5, "t = 5 s")
    draw_marker_label(ax, x1, 18.7, "x = 30 m")
    draw_marker_label(ax, x2, 18.7, "x = 66 m")
    save_scene(fig, "10_postes_medicao.svg")


def scene_conveyor():
    fig, ax = setup_scene("Esteira industrial em MU")
    to_x = draw_s_axis(ax, max_s=15, step=3)
    draw_factory(ax, x=10, y=20)
    ax.add_patch(Rectangle((20, 14.5), 56, 2.8, facecolor=DARK, edgecolor=INK, linewidth=1.0))
    for cx in range(22, 75, 6):
        ax.add_patch(Circle((cx, 14.2), 0.9, facecolor=GRAY, edgecolor=INK, linewidth=0.7))
    start = to_x(1.2)
    end = to_x(13.2)
    draw_box(ax, start, 17.2, scale=0.82, alpha=0.45)
    draw_box(ax, end, 17.2, scale=0.82, alpha=1.0)
    draw_arrow(ax, start + 4.5, 27.0, end - 3.5, 27.0, "v = 0,8 m/s")
    draw_marker_label(ax, start, 30.4, "x0 = 1,2 m")
    draw_marker_label(ax, end, 30.4, "x = 13,2 m")
    draw_marker_label(ax, end + 12, 21.8, "t = 15 s")
    save_scene(fig, "11_esteira_caixa.svg")


def scene_traffic_light():
    fig, ax = setup_scene("Carro saindo do semaforo")
    to_x = draw_s_axis(ax, max_s=80, step=10)
    draw_ground(ax)
    draw_traffic_light(ax, to_x(0) + 2.5, 13.0, scale=1.1)
    start = to_x(4)
    end = to_x(69)
    draw_car(ax, start, 12.0, scale=0.82, color=GRAY, alpha=0.45)
    draw_car(ax, end, 12.0, scale=0.92, color=RED, alpha=1.0)
    draw_arrow(ax, start + 6, 27.0, end - 4, 27.0, "acelera ao longo do eixo S")
    draw_marker_label(ax, start, 30.4, "v0 = 4 m/s")
    draw_marker_label(ax, end, 30.4, "Dx = 69 m")
    draw_marker_label(ax, end + 12, 20.5, "t = 6 s")
    draw_marker_label(ax, end + 12, 17.6, "a = 2,5 m/s2")
    save_scene(fig, "12_carro_semaforo.svg")


def scene_forklift():
    fig, ax = setup_scene("Empilhadeira freando")
    to_x = draw_s_axis(ax, max_s=15, step=3)
    ax.add_patch(Rectangle((8, 11.5), 84, 5.4, facecolor="#d7d0c5", edgecolor=INK, linewidth=1.0))
    for x in (14, 82):
        draw_shelf(ax, x, 16.5, scale=1.0)
    start = to_x(0)
    end = to_x(12)
    draw_forklift(ax, start + 12, 12.0, scale=0.88, alpha=0.55)
    draw_forklift(ax, end, 12.0, scale=0.92, alpha=1.0)
    draw_arrow(ax, start + 18, 28.0, end - 2.5, 28.0, "a = -1,5 m/s2")
    draw_marker_label(ax, start + 12, 31.0, "v0 = 6 m/s")
    draw_marker_label(ax, end, 31.0, "para em 4 s")
    draw_marker_label(ax, end + 11, 20.8, "Dx = 12 m")
    save_scene(fig, "13_empilhadeira_frenagem.svg")


def scene_vehicle_braking():
    fig, ax = setup_scene("Frenagem para Torricelli")
    to_x = draw_s_axis(ax, max_s=80, step=10)
    draw_ground(ax)
    start = to_x(0)
    end = to_x(72)
    draw_car(ax, start + 12, 12.0, scale=0.92, color=BLUE, alpha=0.65)
    draw_car(ax, end, 12.0, scale=0.92, color=BLUE, alpha=1.0)
    ax.plot([start + 18, end - 6], [12.2, 12.2], color=ACCENT, linewidth=1.2, linestyle=(0, (4, 4)))
    ax.plot([end + 4, end + 4], [11.5, 21], color=RED, linewidth=1.6)
    ax.text(end + 4, 22.4, "parada", fontsize=8, ha="center", color=RED)
    draw_arrow(ax, start + 18, 27.0, end - 4, 27.0, "distancia minima")
    draw_marker_label(ax, start + 12, 30.4, "v0 = 24 m/s")
    draw_marker_label(ax, end, 30.4, "Dx = 72 m")
    draw_marker_label(ax, end + 11.5, 18.3, "a = -4 m/s2")
    save_scene(fig, "14_veiculo_frenagem.svg")


def scene_inspection_cart():
    fig, ax = setup_scene("Carrinho de inspecao em MU")
    to_x = draw_s_axis(ax, max_s=50, step=10)
    ax.add_patch(Rectangle((8, 11.3), 84, 1.1, facecolor=DARK, edgecolor=INK, linewidth=0.8))
    ax.add_patch(Rectangle((8, 16.6), 84, 1.1, facecolor=DARK, edgecolor=INK, linewidth=0.8))
    for x in range(11, 92, 5):
        ax.plot([x, x], [12.4, 16.6], color=GRAY, linewidth=0.7)
    start = to_x(2)
    end = to_x(44)
    draw_cart(ax, start, 12.0, scale=0.84, color=GRAY, alpha=0.45)
    draw_cart(ax, end, 12.0, scale=0.9, color=GREEN, alpha=1.0)
    draw_arrow(ax, start + 5.5, 27.0, end - 4, 27.0, "v = 3,5 m/s")
    draw_marker_label(ax, start, 30.4, "x0 = 2 m")
    draw_marker_label(ax, end, 30.4, "x = 44 m")
    draw_marker_label(ax, end + 10.5, 20.4, "t = 12 s")
    save_scene(fig, "15_carrinho_inspecao.svg")


def scene_motorcycle():
    fig, ax = setup_scene("Moto em MUV acelerado")
    to_x = draw_s_axis(ax, max_s=50, step=10)
    draw_ground(ax)
    start = to_x(0)
    end = to_x(47.5)
    draw_motorcycle(ax, start + 10, 12.2, scale=0.95, color=GRAY, alpha=0.45)
    draw_motorcycle(ax, end, 12.2, scale=0.95, color=RED, alpha=1.0)
    draw_arrow(ax, start + 16, 27.0, end - 3.5, 27.0, "a = 3 m/s2")
    draw_marker_label(ax, start + 10, 30.4, "v0 = 2 m/s")
    draw_marker_label(ax, end, 30.4, "Dx = 47,5 m")
    draw_marker_label(ax, end + 10.0, 20.4, "t = 5 s")
    save_scene(fig, "16_moto_arrancada.svg")


def scene_robot():
    fig, ax = setup_scene("Robo de armazem freando")
    to_x = draw_s_axis(ax, max_s=20, step=4)
    ax.add_patch(Rectangle((8, 11.5), 84, 5.4, facecolor="#d7d0c5", edgecolor=INK, linewidth=1.0))
    for x in (12, 24, 76, 88):
        draw_shelf(ax, x, 16.8, scale=0.9)
    start = to_x(0)
    end = to_x(16)
    draw_robot(ax, start + 10, 12.0, scale=0.95, alpha=0.45)
    draw_robot(ax, end, 12.0, scale=1.0, alpha=1.0)
    draw_arrow(ax, start + 15, 27.0, end - 3.5, 27.0, "a = -2 m/s2")
    draw_marker_label(ax, start + 10, 30.4, "v0 = 8 m/s")
    draw_marker_label(ax, end, 30.4, "Dx = 16 m")
    draw_marker_label(ax, end + 10.0, 20.4, "para em 4 s")
    save_scene(fig, "17_robo_armazem.svg")


def scene_cover():
    fig, ax = setup_cover_scene()

    ax.text(
        50.0,
        121.0,
        "LIVRO-LABORATÓRIO DE CÁLCULO E CINEMÁTICA",
        fontsize=8.8,
        color="#d9c6a7",
        ha="center",
        va="center",
        fontweight="bold",
    )
    ax.text(
        50.0,
        108.0,
        "Cálculo em Movimento",
        fontsize=28,
        color="#f8f1e6",
        ha="center",
        va="center",
        fontweight="bold",
        fontfamily="DejaVu Serif",
    )
    ax.text(
        50.0,
        99.0,
        "Limites, derivadas e integrais para entender a cinemática",
        fontsize=10.8,
        color="#f0dfc3",
        ha="center",
        va="center",
    )
    ax.text(
        50.0,
        93.5,
        "por Willams Sousa",
        fontsize=11.4,
        color="#c7dced",
        ha="center",
        va="center",
        fontfamily="DejaVu Serif",
        fontstyle="italic",
    )

    draw_cover_graph_panel(ax, x=10.0, y=53.0, width=34.0, height=36.0)
    draw_cover_graph_panel_analysis(ax, x=53.0, y=53.0, width=36.0, height=36.0)

    axis_y = 19.0
    ax.add_patch(FancyArrowPatch((10.0, axis_y), (90.0, axis_y), arrowstyle="-|>", mutation_scale=13, linewidth=1.5, color=PAPER))
    for tick in range(0, 81, 10):
        xpos = 12.0 + 0.95 * tick
        ax.plot([xpos, xpos], [axis_y - 1.2, axis_y + 1.2], color=PAPER, linewidth=1.0)
        ax.text(xpos, axis_y - 3.6, f"{tick}", fontsize=8, color="#d7e3ed", ha="center")
    ax.text(86.0, axis_y + 4.3, "eixo S", fontsize=9, fontweight="bold", color=PAPER)

    draw_car(ax, 68.0, 20.0, scale=1.04, color=BLUE_SOFT, alpha=1.0)
    ax.add_patch(FancyArrowPatch((60.0, 33.0), (73.0, 33.0), arrowstyle="-|>", mutation_scale=13, linewidth=1.8, color=RED))
    ax.text(66.5, 35.6, "v", fontsize=10, color=RED, ha="center", fontweight="bold")

    ax.add_patch(FancyBboxPatch((8.0, 5.2), 24.0, 10.5, boxstyle="round,pad=0.35,rounding_size=1.5", facecolor="#f7e7ca", edgecolor="none", alpha=0.96))
    ax.text(11.0, 12.1, "retas, areas,", fontsize=10, color=INK, fontweight="bold")
    ax.text(11.0, 8.5, "curvas e movimento", fontsize=10, color=INK, fontweight="bold")
    save_scene(fig, "00_capa_calculo_em_movimento.svg", png_filename="00_capa_calculo_em_movimento.png")


def generate_scene_assets() -> None:
    scene_cover()
    scene_car_between_posts()
    scene_conveyor()
    scene_traffic_light()
    scene_forklift()
    scene_vehicle_braking()
    scene_inspection_cart()
    scene_motorcycle()
    scene_robot()

def main() -> None:
    ensure_dirs()
    generate_scene_assets()


if __name__ == "__main__":
    main()
