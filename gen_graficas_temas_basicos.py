"""Generate plot illustrations for the 'Temas Básicos' page of Ziyuan.

Produces 4 PNGs into docs/images/:
  - graf_lineal.png        Linear function with intercepts and monotonicity
  - graf_cuadratica.png    Quadratic function with vertex, axis, intercepts
  - graf_exponencial.png   Exponential function with asymptote
  - graf_logaritmica.png   Logarithmic function with asymptote

Style: clean, didactic, large labels, light grid, dark axes. Same visual
language as gen_recta.py.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

OUT_DIR = "/data/MyTera/ziyuan/docs/images"
os.makedirs(OUT_DIR, exist_ok=True)

# Shared style
plt.rcParams.update({
    "font.size": 13,
    "axes.labelsize": 14,
    "axes.titlesize": 15,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "legend.fontsize": 12,
    "figure.dpi": 110,
})

AXIS_COLOR = "#222222"
GRID_COLOR = "#cccccc"
CURVE_COLOR = "#1565c0"
INTERCEPT_COLOR = "#c62828"
ASINT_COLOR = "#6a1b9a"
AXIS_OF_SYM_COLOR = "#ef6c00"


def _draw_axes(ax, xlim, ylim, xticks=None, yticks=None):
    """Draw clean cartesian axes with arrows on the positive ends."""
    ax.grid(True, color=GRID_COLOR, linewidth=0.6, alpha=0.7, zorder=0)
    ax.axhline(0, color=AXIS_COLOR, linewidth=1.6, zorder=2)
    ax.axvline(0, color=AXIS_COLOR, linewidth=1.6, zorder=2)
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[1] - 0.6, 0),
                arrowprops=dict(arrowstyle="->", color=AXIS_COLOR, lw=1.6))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[1] - 0.6),
                arrowprops=dict(arrowstyle="->", color=AXIS_COLOR, lw=1.6))
    ax.text(xlim[1] - 0.15, -0.25, "x", ha="center", va="top",
            fontsize=14, fontweight="bold", color=AXIS_COLOR)
    ax.text(-0.25, ylim[1] - 0.15, "y", ha="right", va="center",
            fontsize=14, fontweight="bold", color=AXIS_COLOR)

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if xticks is not None:
        ax.set_xticks(xticks)
    if yticks is not None:
        ax.set_yticks(yticks)
    ax.set_aspect("equal", adjustable="box")
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(length=0)


def _label_point(ax, x, y, label, dx=0.25, dy=0.25, ha="left"):
    ax.plot(x, y, "o", color=INTERCEPT_COLOR, markersize=8, zorder=4)
    ax.text(x + dx, y + dy, label, fontsize=12, fontweight="bold",
            color=INTERCEPT_COLOR, ha=ha, va="bottom", zorder=5)


def _draw_asymptote_h(ax, y, x_range, label_text, label_xy):
    """Horizontal asymptote, drawn thicker and more visible."""
    ax.plot(x_range, [y, y], "--", color=ASINT_COLOR, linewidth=1.8,
            alpha=0.85, zorder=2)
    ax.text(label_xy[0], label_xy[1], label_text, fontsize=11,
            color=ASINT_COLOR, ha="right", va="bottom",
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white",
                      edgecolor="none", alpha=0.85))


def _draw_asymptote_v(ax, x, y_range, label_text, label_xy):
    ax.plot([x, x], y_range, "--", color=ASINT_COLOR, linewidth=1.8,
            alpha=0.85, zorder=2)
    ax.text(label_xy[0], label_xy[1], label_text, fontsize=11,
            color=ASINT_COLOR, ha="left", va="top",
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white",
                      edgecolor="none", alpha=0.85))


def _draw_axis_of_symmetry(ax, x, y_range, label_text):
    ax.plot([x, x], y_range, "--", color=AXIS_OF_SYM_COLOR,
            linewidth=1.5, alpha=0.85, zorder=2)
    ax.text(x + 0.05, y_range[1] - 0.15, label_text, fontsize=12,
            color=AXIS_OF_SYM_COLOR, fontweight="bold", va="top")


# -------------------------------------------------------------------- #
# 1) Linear function                                                    #
# -------------------------------------------------------------------- #
def graf_lineal():
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))

    # LEFT: f(x) = 2x + 3  (increasing)
    ax = axes[0]
    _draw_axes(ax, (-5, 5), (-3, 7), xticks=range(-4, 5), yticks=range(-2, 7, 2))
    x = np.linspace(-4, 4.5, 200)
    ax.plot(x, 2 * x + 3, color=CURVE_COLOR, linewidth=2.4, zorder=3)
    _label_point(ax, 0, 3, "(0, 3)", dx=-0.15, dy=0.25, ha="right")
    _label_point(ax, -1.5, 0, r"$\left(-\frac{3}{2},\ 0\right)$",
                 dx=0.0, dy=-0.6, ha="center")
    # Legend box outside the curve
    ax.text(-4.5, 5.8, "Creciente  (m > 0)", fontsize=13,
            color="#37474f", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#f5f5f5",
                      edgecolor="#bdbdbd"))
    ax.text(2.6, 6.3, r"$f(x) = 2x + 3$", fontsize=16,
            color=CURVE_COLOR, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="none", alpha=0.85))
    ax.set_title("Creciente", fontsize=14, fontweight="bold", pad=8)

    # RIGHT: f(x) = -(2/3)x + 4  (decreasing)
    ax = axes[1]
    _draw_axes(ax, (-1, 8), (-2, 6), xticks=range(0, 8), yticks=range(-1, 6))
    x = np.linspace(-0.5, 7.5, 200)
    ax.plot(x, -2 / 3 * x + 4, color=CURVE_COLOR, linewidth=2.4, zorder=3)
    _label_point(ax, 0, 4, "(0, 4)", dx=0.2, dy=0.25, ha="left")
    _label_point(ax, 6, 0, "(6, 0)", dx=0.2, dy=-0.55, ha="left")
    ax.text(0.4, 5.2, "Decreciente  (m < 0)", fontsize=13,
            color="#37474f", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#f5f5f5",
                      edgecolor="#bdbdbd"))
    ax.text(0.5, 2.5, r"$f(x) = -\dfrac{2}{3}\,x + 4$", fontsize=16,
            color=CURVE_COLOR, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="none", alpha=0.85))
    ax.set_title("Decreciente", fontsize=14, fontweight="bold", pad=8)

    fig.suptitle("Función lineal:  f(x) = m·x + b",
                 fontsize=17, fontweight="bold", y=1.03)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "graf_lineal.png"),
                dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# -------------------------------------------------------------------- #
# 2) Quadratic function                                                 #
# -------------------------------------------------------------------- #
def graf_cuadratica():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # LEFT: f(x) = x^2 - 4x + 3   (opens up, vertex (2, -1))
    ax = axes[0]
    _draw_axes(ax, (-1, 6), (-3, 7), xticks=range(0, 6), yticks=range(-2, 7, 2))
    x = np.linspace(-0.5, 5.5, 300)
    ax.plot(x, x ** 2 - 4 * x + 3, color=CURVE_COLOR, linewidth=2.4, zorder=3)
    # Vertex — pull label further away from the curve (down-left)
    _label_point(ax, 2, -1, "Vértice (2, −1)", dx=-0.15, dy=-0.45, ha="right")
    _draw_axis_of_symmetry(ax, 2, (-3, 7), r"eje: $x = 2$")
    _label_point(ax, 0, 3, "(0, 3)", dx=-0.15, dy=0.25, ha="right")
    _label_point(ax, 1, 0, "(1, 0)", dx=-0.15, dy=-0.55, ha="right")
    _label_point(ax, 3, 0, "(3, 0)", dx=0.2, dy=-0.55, ha="left")
    # Concavity label — top-right area, away from equation
    ax.text(4.7, 5.0, "Concavidad ↑\n(mínimo)",
            fontsize=12, color="#37474f", fontweight="bold", ha="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#bdbdbd"))
    # Equation — bottom-left corner (free space, doesn't overlap curve)
    ax.text(0.2, -2.5, r"$f(x) = x^2 - 4x + 3$", fontsize=15,
            color=CURVE_COLOR, fontweight="bold", ha="left",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="none", alpha=0.85))
    ax.set_title("Abre hacia arriba  (a > 0)", fontsize=13,
                 fontweight="bold", pad=8)

    # RIGHT: f(x) = -x^2 + 6x - 9  (opens down, vertex (3, 0))
    ax = axes[1]
    # Wider y-range so the parabola opens fully past (0,-9) and beyond
    _draw_axes(ax, (-1, 7), (-13, 2),
               xticks=range(0, 7), yticks=range(-12, 2, 3))
    x = np.linspace(-0.5, 6.5, 400)
    ax.plot(x, -x ** 2 + 6 * x - 9, color=CURVE_COLOR, linewidth=2.4, zorder=3)
    _label_point(ax, 3, 0, "Vértice (3, 0)", dx=0.3, dy=0.4, ha="left")
    _draw_axis_of_symmetry(ax, 3, (-13, 2), r"eje: $x = 3$")
    _label_point(ax, 0, -9, "(0, −9)", dx=0.3, dy=-0.6, ha="left")
    ax.text(5.5, -10, "Concavidad ↓\n(máximo)",
            fontsize=12, color="#37474f", fontweight="bold", ha="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#bdbdbd"))
    ax.text(0.5, -5.5, r"$f(x) = -x^2 + 6x - 9$", fontsize=15,
            color=CURVE_COLOR, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="none", alpha=0.85))
    ax.set_title("Abre hacia abajo  (a < 0)", fontsize=13,
                 fontweight="bold", pad=8)

    fig.suptitle("Función cuadrática:  f(x) = ax² + bx + c",
                 fontsize=17, fontweight="bold", y=1.03)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "graf_cuadratica.png"),
                dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# -------------------------------------------------------------------- #
# 3) Exponential function                                               #
# -------------------------------------------------------------------- #
def graf_exponencial():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # LEFT: f(x) = 2^x       (increasing, base > 1)
    ax = axes[0]
    _draw_axes(ax, (-4, 5), (-1, 8), xticks=range(-3, 5), yticks=range(0, 8))
    x = np.linspace(-4, 4.4, 300)
    ax.plot(x, 2 ** x, color=CURVE_COLOR, linewidth=2.4, zorder=3)
    _label_point(ax, 0, 1, "(0, 1)", dx=0.25, dy=0.2, ha="left")
    _draw_asymptote_h(ax, 0, (-4, 5), "y = 0  (asíntota)",
                      label_xy=(5.0, 0.18))
    ax.text(-3.6, 5.5, "Creciente  (a > 1)",
            fontsize=12, color="#37474f", fontweight="bold",
            ha="left",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#bdbdbd"))
    ax.text(1.5, 6.0, r"$f(x) = 2^x$", fontsize=16,
            color=CURVE_COLOR, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="none", alpha=0.85))
    ax.set_title("Creciente", fontsize=14, fontweight="bold", pad=8)

    # RIGHT: f(x) = (1/2)^x   (decreasing, 0 < a < 1)
    ax = axes[1]
    _draw_axes(ax, (-1, 5), (-1, 8), xticks=range(0, 5), yticks=range(0, 8))
    x = np.linspace(-0.5, 4.5, 300)
    ax.plot(x, (1 / 2) ** x, color=CURVE_COLOR, linewidth=2.4, zorder=3)
    _label_point(ax, 0, 1, "(0, 1)", dx=0.25, dy=0.2, ha="left")
    _draw_asymptote_h(ax, 0, (-1, 5), "y = 0  (asíntota)",
                      label_xy=(5.0, 0.18))
    ax.text(0.4, 6.7, "Decreciente  (0 < a < 1)",
            fontsize=12, color="#37474f", fontweight="bold",
            ha="left",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#bdbdbd"))
    ax.text(2.5, 4.0, r"$f(x) = \left(\dfrac{1}{2}\right)^x$", fontsize=16,
            color=CURVE_COLOR, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="none", alpha=0.85))
    ax.set_title("Decreciente", fontsize=14, fontweight="bold", pad=8)

    fig.suptitle("Función exponencial:  f(x) = a^x",
                 fontsize=17, fontweight="bold", y=1.03)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "graf_exponencial.png"),
                dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# -------------------------------------------------------------------- #
# 4) Logarithmic function                                               #
# -------------------------------------------------------------------- #
def graf_logaritmica():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # LEFT: f(x) = log_2(x)   (increasing, base > 1)
    ax = axes[0]
    _draw_axes(ax, (-1, 8), (-3, 4), xticks=range(0, 8), yticks=range(-2, 4))
    x = np.linspace(0.05, 7.5, 400)
    ax.plot(x, np.log2(x), color=CURVE_COLOR, linewidth=2.4, zorder=3)
    _label_point(ax, 1, 0, "(1, 0)", dx=0.2, dy=-0.55, ha="left")
    _draw_asymptote_v(ax, 0, (-3, 4), "x = 0  (asíntota)",
                      label_xy=(0.05, 3.85))
    ax.text(3.6, 2.0, "Creciente  (a > 1)",
            fontsize=12, color="#37474f", fontweight="bold",
            ha="left",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#bdbdbd"))
    ax.text(2.5, 1.4, r"$f(x) = \log_2 x$", fontsize=16,
            color=CURVE_COLOR, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="none", alpha=0.85))
    ax.set_title("Creciente", fontsize=14, fontweight="bold", pad=8)

    # RIGHT: f(x) = log_{1/2}(x)  (decreasing, 0 < a < 1)
    ax = axes[1]
    _draw_axes(ax, (-1, 8), (-3, 4), xticks=range(0, 8), yticks=range(-2, 4))
    x = np.linspace(0.05, 7.5, 400)
    ax.plot(x, -np.log2(x), color=CURVE_COLOR, linewidth=2.4, zorder=3)
    _label_point(ax, 1, 0, "(1, 0)", dx=0.2, dy=-0.55, ha="left")
    _draw_asymptote_v(ax, 0, (-3, 4), "x = 0  (asíntota)",
                      label_xy=(0.05, 3.85))
    ax.text(3.5, -2.0, "Decreciente  (0 < a < 1)",
            fontsize=12, color="#37474f", fontweight="bold",
            ha="left",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#bdbdbd"))
    ax.text(2.5, -1.4, r"$f(x) = \log_{1/2} x$", fontsize=16,
            color=CURVE_COLOR, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="none", alpha=0.85))
    ax.set_title("Decreciente", fontsize=14, fontweight="bold", pad=8)

    fig.suptitle("Función logarítmica:  f(x) = log_a x",
                 fontsize=17, fontweight="bold", y=1.03)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "graf_logaritmica.png"),
                dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    graf_lineal()
    graf_cuadratica()
    graf_exponencial()
    graf_logaritmica()
    print("Generated 4 plots in", OUT_DIR)
    for fn in ("graf_lineal.png", "graf_cuadratica.png",
               "graf_exponencial.png", "graf_logaritmica.png"):
        path = os.path.join(OUT_DIR, fn)
        size = os.path.getsize(path)
        print(f"  {fn:30s} {size:>8d} bytes")
