"""
gradient_zigzag_quadratic.py
============================
Draw the level curves of the quadratic
    f(x) = (1/2)(x_1^2 + gamma * x_2^2)
and overlay the gradient descent trajectory with exact line search,
illustrating the well-known zigzag phenomenon on badly-conditioned problems.

Usage (from this directory):
    python3 gradient_zigzag_quadratic.py

Output:
    gradient_zigzag_quadratic.png  (~6x5 in, 150 dpi)

The script is self-contained; it only needs numpy and matplotlib.
The default gamma = 10 is the badly-conditioned case shown in slide
"9.3 Comportamiento: bien vs. mal condicionado".
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.collections import PatchCollection

# --------------------------------------------------------------------------
# Configuration (mirrors the slide's quadratic with gamma = 10)
# --------------------------------------------------------------------------
GAMMA = 10.0            # conditioning: f(x) = 1/2 (x1^2 + gamma * x2^2)
N_STEPS = 9             # number of gradient steps to draw
X_START = (2.5, 0.7)    # initial point (off-axis => real zigzag)
X_LIM = (-3.2, 3.2)     # plot x-range
Y_LIM = (-1.4, 1.4)     # plot y-range
LEVEL_VALUES = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]  # levels of f to display

# Color palette (mirrors the beamer theme's accentblue / accentred)
COLOR_LEVELS = "#7a9fc9"      # lighter accentblue for level curves
COLOR_TRAJ = "#c62828"        # accentred for trajectory
COLOR_START = "#1f497d"       # accentblue (start marker)
COLOR_OPT = "#1f497d"         # accentblue (optimal point)

# --------------------------------------------------------------------------
# Trajectory: gradient descent with exact line search
# --------------------------------------------------------------------------
def exact_step(x, gamma):
    """One step of gradient descent with exact line search on the quadratic
    f(x) = 1/2 (x1^2 + gamma * x2^2).

    Closed-form:  t* = (x1^2 + gamma^2 x2^2) / (x1^2 + gamma^3 x2^2).
    """
    x1, x2 = x
    t_star = (x1 * x1 + gamma * gamma * x2 * x2) / (x1 * x1 + gamma**3 * x2 * x2 + 1e-30)
    return np.array([x1 * (1.0 - t_star), x2 * (1.0 - gamma * t_star)])


def trajectory(x0, gamma, n_steps):
    pts = [np.asarray(x0, dtype=float)]
    for _ in range(n_steps):
        pts.append(exact_step(pts[-1], gamma))
    return np.array(pts)


# --------------------------------------------------------------------------
# Plot
# --------------------------------------------------------------------------
def make_figure():
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)

    # --- Level curves: ellipses x1^2 + gamma x2^2 = 2c ---
    for c in LEVEL_VALUES:
        # semi-axes of the ellipse x1^2 / a^2 + x2^2 / b^2 = 1 with
        # x1^2 + gamma x2^2 = 2c  =>  a = sqrt(2c),  b = sqrt(2c/gamma)
        a = np.sqrt(2.0 * c)
        b = np.sqrt(2.0 * c / GAMMA)
        e = Ellipse(
            (0.0, 0.0), width=2 * a, height=2 * b,
            facecolor="none", edgecolor=COLOR_LEVELS, linewidth=1.4, zorder=1,
        )
        ax.add_patch(e)
        # label the outermost ellipse
        if c == LEVEL_VALUES[-1]:
            ax.text(a + 0.08, 0.0, f"$f(x) = {c:g}$",
                    color=COLOR_LEVELS, fontsize=9, va="center", ha="left")

    # --- Trajectory ---
    pts = trajectory(X_START, GAMMA, N_STEPS)
    ax.plot(pts[:, 0], pts[:, 1],
            color=COLOR_TRAJ, linewidth=1.6, zorder=3,
            marker="o", markersize=4.5, markerfacecolor=COLOR_TRAJ,
            markeredgecolor="white", markeredgewidth=0.6,
            label="descenso por gradiente")

    # Start marker
    ax.plot(pts[0, 0], pts[0, 1], "o",
            color=COLOR_START, markersize=8, zorder=4)
    ax.annotate(r"$x^{(0)}$", xy=pts[0], xytext=(8, 8),
                textcoords="offset points",
                fontsize=11, color=COLOR_START)

    # Optimal point
    ax.plot(0, 0, "*", color=COLOR_OPT, markersize=14, zorder=4)
    ax.annotate(r"$x^{\star} = (0,0)$", xy=(0, 0), xytext=(8, -14),
                textcoords="offset points",
                fontsize=11, color=COLOR_OPT)

    # --- Axes / cosmetics ---
    ax.axhline(0, color="0.55", linewidth=0.6, zorder=0)
    ax.axvline(0, color="0.55", linewidth=0.6, zorder=0)
    ax.set_xlim(*X_LIM)
    ax.set_ylim(*Y_LIM)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel(r"$x_1$", fontsize=11)
    ax.set_ylabel(r"$x_2$", fontsize=11)
    ax.set_title(
        rf"$\gamma = {GAMMA:g}$ \ \ \ "
        rf"$f(x) = \frac{{1}}{{2}}(x_1^2 + \gamma\,x_2^2)$",
        fontsize=12, pad=8,
    )
    ax.tick_params(axis="both", labelsize=9)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    plt.tight_layout()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "gradient_zigzag_quadratic.png")
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Wrote {out}")
    return out


if __name__ == "__main__":
    make_figure()
