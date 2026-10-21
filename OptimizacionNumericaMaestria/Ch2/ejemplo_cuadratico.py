"""
Ejemplo cuadrático de la diapositiva "Ejemplo cuadrático"
(Capítulo 2 de Brunton, Figura 2.3).

    f(x) = 1/2 x^T A x,   A = [[2, 1], [1, 3]]  (definida positiva)
    x*   = 0,   x0 = [-2, 0],   b = 0,   c = 0

Se compara el descenso de gradiente con tres tamanos de paso:
    gamma = 0.01   -> convergencia lenta
    gamma = 0.1    -> convergencia rapida y sin oscilaciones
    gamma = 0.543  -> casi inestable, oscila alrededor del minimo

Reproduce la estructura de la Figura 2.3 del libro:
fila superior  : cada trayectoria sobre las curvas de nivel de f
fila inferior  : f(x_k) frente a la iteracion (escala lineal y logaritmica)

Salida: images/ejemplo_cuadratico.png
"""

import os

import warnings

import matplotlib

matplotlib.use("Agg")  # backend sin ventana, para correr en servidor
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------------------
# Problema
# ---------------------------------------------------------------------------
A = np.array([[2.0, 1.0],
              [1.0, 3.0]])
B = np.zeros(2)          # termino lineal  (b en el libro)
X0 = np.array([-2.0, 0.0])
X_STAR = np.zeros(2)     # minimo: f cuadratica con minimo en el origen

GAMMAS = [0.01, 0.1, 0.543]
MAX_ITER = 30           # el libro usa N = 30

COLORS = {0.01: "#00529B", 0.1: "#D95F02", 0.543: "#00876C"}
LABELS = {0.01: r"$\gamma=0.01$  (muy pequeño)",
          0.1:   r"$\gamma=0.1$  (justo)",
          0.543: r"$\gamma=0.543$  (muy grande)"}

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "images", "ejemplo_cuadratico.png")


def f(x):
    """Objetivo cuadratico."""
    return 0.5 * x @ A @ x


def grad_f(x):
    """Gradiente: Ax + b (A es simetrica)."""
    return A @ x + B


def gradient_descent(gamma, max_iter=MAX_ITER):
    """Descenso de gradiente. Devuelve trayectorias y valores de f."""
    x = np.array(X0, dtype=float)
    traj = [x.copy()]
    fvals = [f(x)]
    for _ in range(max_iter):
        x = x - gamma * grad_f(x)
        traj.append(x.copy())
        fvals.append(f(x))
    return np.array(traj), np.array(fvals)


def eigenvalues():
    vals = np.linalg.eigvalsh(A)
    return float(vals.min()), float(vals.max())


def main():
    lam_min, lam_max = eigenvalues()
    gamma_max = 2.0 / lam_max          # frontera de estabilidad
    gamma_opt = 2.0 / (lam_min + lam_max)   # paso optimo
    rho_opt = (lam_max - lam_min) / (lam_min + lam_max)

    print("Ejemplo cuadratico:  f(x) = 1/2 x^T A x,  A = [[2,1],[1,3]]")
    print(f"  x0 = {X0},  x* = {X_STAR},  N = {MAX_ITER}")
    print()
    print(f"  autovalores de A : {lam_min:.4f}, {lam_max:.4f}")
    print(f"  paso maximo (estabilidad) gamma_max = 2/lambda_max   = {gamma_max:.4f}")
    print(f"  paso optimo                  gamma_opt = 2/(lmin+lmax) = {gamma_opt:.4f}")
    print(f"  contraccion optima rho = (lmax-lmin)/(lmax+lmin) = {rho_opt:.4f}")
    print()
    print("  gamma     | f final    | monotona   | radio | 1-gamma*lambda_min | 1-gamma*lambda_max")
    for g in GAMMAS:
        traj, fvals = gradient_descent(g)
        rho = max(abs(1.0 - g * lam_min), abs(1.0 - g * lam_max))
        monotone = bool(np.all(np.diff(fvals) <= 1e-12))
        print(f"  {g:<8} | {fvals[-1]:<10.4f} | {str(monotone):<12} | "
              f"{rho:<5.3f} | {1-g*lam_min:>18.4f} | {1-g*lam_max:>18.4f}")
    print()
    print(f"  Nota: 0.543 < gamma_max = {gamma_max:.4f}, por eso oscila sin divergir.")
    print()

    results = {g: gradient_descent(g) for g in GAMMAS}

    # ----------------------------------------------------------------------
    # Figura
    # ----------------------------------------------------------------------
    plt.rcParams.update({
        "font.family": "DejaVu Sans",   # suporta acentos
        "mathtext.fontset": "dejavusans",
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "legend.fontsize": 8.5,
        "figure.dpi": 110,
    })

    # malla para las curvas de nivel
    lim = 3.0
    xs = np.linspace(-lim, lim, 400)
    X, Y = np.meshgrid(xs, xs)
    Z = 0.5 * (A[0, 0] * X**2 + 2 * A[0, 1] * X * Y + A[1, 1] * Y**2)
    levels = np.concatenate([[0.0], np.geomspace(0.05, 12.0, 11)])

    fig = plt.figure(figsize=(12.4, 7.4))
    gs = fig.add_gridspec(2, 3, height_ratios=[1.15, 1.0],
                          hspace=0.34, wspace=0.26,
                          left=0.065, right=0.985, top=0.885, bottom=0.085)

    # --- fila superior: cada trayectoria sobre las curvas de nivel ---------
    for col, g in enumerate(GAMMAS):
        ax = fig.add_subplot(gs[0, col])
        ax.contour(X, Y, Z, levels=levels, colors="#9aa5b1",
                   linewidths=0.55, alpha=0.85)
        traj, _ = results[g]
        ax.plot(traj[:, 0], traj[:, 1], "-o", color=COLORS[g],
                markersize=3.0, linewidth=1.5,
                label=LABELS[g])
        ax.plot(*X_STAR, "*", color="black", markersize=13,
                zorder=5, label=r"$x^\star$")
        ax.plot(X0[0], X0[1], "s", color="#444444", markersize=6,
                zorder=5, label=r"$x_0$")
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_aspect("equal")
        ax.set_title(LABELS[g])
        ax.set_xlabel(r"$x_1$")
        if col == 0:
            ax.set_ylabel(r"$x_2$")
        else:
            ax.set_yticklabels([])
        if col == 2:
            ax.legend(loc="upper left", framealpha=0.92, borderpad=0.5)

    # --- fila inferior izquierda: f(x_k) vs iteracion (lineal) -------------
    ax1 = fig.add_subplot(gs[1, :2])
    for g in GAMMAS:
        _, fvals = results[g]
        ax1.plot(np.arange(len(fvals)), fvals, "-o", color=COLORS[g],
                 markersize=2.8, linewidth=1.4, label=LABELS[g])
    ax1.set_xlabel("iteración  $k$")
    ax1.set_ylabel(r"$f(x_k)$")
    ax1.set_title(r"$f(x_k)$ frente a la iteración  (escala lineal)")
    ax1.set_xlim(0, MAX_ITER)
    ax1.grid(alpha=0.3)
    ax1.legend(loc="upper right", framealpha=0.92)

    # --- fila inferior derecha: escala logaritmica -------------------------
    ax2 = fig.add_subplot(gs[1, 2])
    for g in GAMMAS:
        _, fvals = results[g]
        ax2.plot(np.arange(len(fvals)), np.maximum(fvals, 1e-14), "-o",
                 color=COLORS[g], markersize=2.8, linewidth=1.4, label=LABELS[g])
    ax2.set_yscale("log")
    ax2.set_xlabel("iteración  $k$")
    ax2.set_ylabel(r"$\log f(x_k)$")
    ax2.set_title("escala logarítmica")
    ax2.set_xlim(0, MAX_ITER)
    ax2.grid(alpha=0.3, which="both")

    fig.suptitle(
        r"Descenso de gradiente sobre $f(x)=\frac{1}{2}x^{T}Ax$,  "
        r"$A=[[2,\,1],[1,\,3]]$,  $x_0=(-2,\,0)$,  $x^\star=0$",
        fontsize=13, y=0.965)

    fig.savefig(OUT, dpi=180, bbox_inches="tight", facecolor="white")
    print(f"  figura guardada en: {OUT}")


if __name__ == "__main__":
    main()
