"""
Version horizontal (1 fila x 3 columnas) de la Figura 2.3 del libro:
los tres tamanos de paso lado a lado en una sola imagen ancha.

    f(x) = 1/2 x^T A x,   A = [[2, 1], [1, 3]]  (definida positiva)
    x* = 0,   x0 = [-2, 0],   N = 30

Salida: images/ejemplo_cuadratico_ancho.png
"""

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

A = np.array([[2.0, 1.0],
              [1.0, 3.0]])
B = np.zeros(2)
X0 = np.array([-2.0, 0.0])
X_STAR = np.zeros(2)
MAX_ITER = 30

GAMMAS = [0.01, 0.1, 0.543]
COLORS = {0.01: "#00529B", 0.1: "#D95F02", 0.543: "#00876C"}
TITLES = {0.01: r"$\gamma=0.01$",
          0.1:   r"$\gamma=0.1$",
          0.543: r"$\gamma=0.543$"}
VERDICT = {0.01: "convergencia lenta",
           0.1:   "rapido y estable",
           0.543: "casi inestable, oscila"}

HERE = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(HERE, "images")


def f(x):
    return 0.5 * x @ A @ x


def grad_f(x):
    return A @ x + B


def gradient_descent(gamma, max_iter=MAX_ITER):
    x = np.array(X0, dtype=float)
    traj = [x.copy()]
    for _ in range(max_iter):
        x = x - gamma * grad_f(x)
        traj.append(x.copy())
    return np.array(traj)


def main():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "mathtext.fontset": "dejavusans",
        "axes.labelsize": 12,
        "axes.titlesize": 14,
    })

    lam = np.linalg.eigvalsh(A)
    lam_min, lam_max = float(lam.min()), float(lam.max())
    gamma_max = 2.0 / lam_max

    lim = 3.0
    xs = np.linspace(-lim, lim, 400)
    X, Y = np.meshgrid(xs, xs)
    Z = 0.5 * (A[0, 0] * X**2 + 2 * A[0, 1] * X * Y + A[1, 1] * Y**2)
    levels = np.concatenate([[0.0], np.geomspace(0.05, 12.0, 11)])

    results = {g: gradient_descent(g) for g in GAMMAS}

    fig, axes = plt.subplots(1, 3, figsize=(15.0, 5.4), dpi=150)
    fig.subplots_adjust(left=0.06, right=0.985, top=0.845, bottom=0.115,
                        wspace=0.18)

    for ax, g in zip(axes, GAMMAS):
        traj = results[g]
        ax.contour(X, Y, Z, levels=levels, colors="#9aa5b1",
                   linewidths=0.7, alpha=0.9)
        ax.plot(traj[::5, 0], traj[::5, 1], "o", color="white",
                markersize=4.5, markeredgecolor=COLORS[g],
                markeredgewidth=1.1, zorder=4)
        ax.plot(traj[:, 0], traj[:, 1], "-", color=COLORS[g],
                linewidth=1.9, zorder=3)
        ax.plot(*X_STAR, "*", color="black", markersize=18, zorder=6)
        ax.plot(X0[0], X0[1], "s", color="#444444", markersize=9, zorder=6)

        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_aspect("equal")
        ax.set_xlabel(r"$x_1$")
        ax.set_title(TITLES[g])
        ax.grid(alpha=0.18)

        info = (r"$f(x_N)=$" + f"{f(traj[-1]):.2e}" + "\n"
                + r"$1-\gamma\lambda_{max}=$"
                + f"{1.0 - g * lam_max:+.3f}")
        ax.text(0.035, 0.965, info, transform=ax.transAxes, va="top",
                ha="left", fontsize=10,
                bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                          alpha=0.92, edgecolor="#cccccc"))

        ax.text(0.5, -0.145, VERDICT[g], transform=ax.transAxes,
                ha="center", va="top", fontsize=11, style="italic",
                color=COLORS[g])

    axes[0].set_ylabel(r"$x_2$")
    axes[0].text(-0.20, 0.5, r"$x^\star = 0$", transform=axes[0].transAxes,
                 rotation=90, va="center", ha="center", fontsize=11)

    fig.suptitle(
        r"Descenso de gradiente:  $f(x)=\frac{1}{2}x^{T}Ax$,  "
        r"$A=[[2,\,1],[1,\,3]]$,  $x_0=(-2,\,0)$,  $x^\star=0$,  "
        r"$\gamma_{max}=2/\lambda_{max}=" + f"{gamma_max:.3f}" + "$",
        fontsize=14, y=0.965)

    out = os.path.join(IMGDIR, "ejemplo_cuadratico_ancho.png")
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("figura ancha guardada en:", out)
    for g in GAMMAS:
        print(f"  gamma={g:<6} f(x_N)={f(results[g][-1]):.3e}  "
              f"1-g*lmax={1.0 - g * lam_max:+.4f}")


if __name__ == "__main__":
    main()
