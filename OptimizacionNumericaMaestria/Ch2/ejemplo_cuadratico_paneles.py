"""
Genera los tres paneles superiores de la Figura 2.3 por separado:
uno por cada tamano de paso. Util para enviar imagenes individuales.

    f(x) = 1/2 x^T A x,   A = [[2, 1], [1, 3]]  (definida positiva)
    x* = 0,   x0 = [-2, 0]

Salida: images/panel_gamma_<valor>.png
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
TITLES = {0.01: r"$\gamma=0.01$   demasiado pequeno",
          0.1:   r"$\gamma=0.1$   justo",
          0.543: r"$\gamma=0.543$   casi inestable"}

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
        "legend.fontsize": 11,
    })

    lim = 3.0
    xs = np.linspace(-lim, lim, 400)
    X, Y = np.meshgrid(xs, xs)
    Z = 0.5 * (A[0, 0] * X**2 + 2 * A[0, 1] * X * Y + A[1, 1] * Y**2)
    levels = np.concatenate([[0.0], np.geomspace(0.05, 12.0, 11)])

    lam = np.linalg.eigvalsh(A)
    lam_min, lam_max = float(lam.min()), float(lam.max())

    for g in GAMMAS:
        traj = gradient_descent(g)

        fig, ax = plt.subplots(figsize=(6.4, 6.0), dpi=150)
        ax.contour(X, Y, Z, levels=levels, colors="#9aa5b1",
                   linewidths=0.7, alpha=0.9)
        ax.plot(traj[:, 0], traj[:, 1], "-o", color=COLORS[g],
                markersize=4.0, linewidth=1.9, label=r"iterados $x_k$")
        ax.plot(*X_STAR, "*", color="black", markersize=18,
                zorder=5, label=r"$x^\star = 0$")
        ax.plot(X0[0], X0[1], "s", color="#444444", markersize=9,
                zorder=5, label=r"$x_0 = (-2,\,0)$")

        # puntos de partida de cada iteracion (subconjunto, para no saturar)
        ax.plot(traj[::5, 0], traj[::5, 1], "o", color="white",
                markersize=4.0, markeredgecolor=COLORS[g],
                markeredgewidth=1.0, zorder=4)

        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_aspect("equal")
        ax.set_xlabel(r"$x_1$")
        ax.set_ylabel(r"$x_2$")
        ax.set_title(TITLES[g], fontsize=14)
        ax.grid(alpha=0.18)

        info = (r"$\gamma_{max}=\frac{2}{\lambda_{max}}=" + f"{2.0/lam_max:.3f}"
                + "$" + "\n" + r"$f(x_0)=$" + f"{f(X0):.2f}" + ",  "
                + r"$f(x_N)=$" + f"{f(traj[-1]):.2e}" + ",  "
                + r"$N=$" + str(MAX_ITER))
        ax.text(0.03, 0.97, info, transform=ax.transAxes, va="top", ha="left",
                fontsize=9.5,
                bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                          alpha=0.9, edgecolor="#cccccc"))

        ax.legend(loc="lower left", framealpha=0.92, borderpad=0.5)

        out = os.path.join(IMGDIR, f"panel_gamma_{str(g).replace('.', '_')}.png")
        fig.tight_layout()
        fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        print(f"  gamma={g:<6} -> {out}")


if __name__ == "__main__":
    main()
