#!/usr/bin/env python3
"""
Visualización comparativa de dos reglas para elegir la longitud de paso
en un método iterativo de optimización:

1. Regla de Armijo con backtracking (descenso suficiente).
2. Longitud de paso exacta (búsqueda exacta sobre la dirección).

Problema utilizado:

    f(x) = 1/2 x^T Q x

con Q definida positiva. Para este problema la búsqueda exacta a lo largo
de una dirección de descenso tiene solución cerrada:

    alpha_exact = -(grad f(x)^T d) / (d^T Q d)

Idea central de la comparación: Armijo NO calcula el minimizador de
phi(alpha) = f(x + alpha d); únicamente garantiza una disminución
suficiente. La búsqueda exacta sí minimiza phi, y por eso da pasos más
cortos (salvo que la trayectoria inicial coincida) pero no necesita
evaluar la función un número arbitrario de veces.

Uso:

    python visualize_armijo_vs_exact.py
    python visualize_armijo_vs_exact.py --show
    python visualize_armijo_vs_exact.py --output-dir salida --alpha-initial 1.0
"""

from pathlib import Path
import argparse

import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# Problema de optimización
# ---------------------------------------------------------------------------

Q = np.array([
    [2.0, 0.6],
    [0.6, 1.3],
])

X0 = np.array([1.5, -1.2])

# Parámetros de la regla de Armijo.
ALPHA_INITIAL = 1.5
BETA = 0.5
C1 = 1.0e-4
MAX_BACKTRACKS = 40

# Criterios de parada.
MAX_ITERATIONS = 25
GRADIENT_TOLERANCE = 1.0e-10
STEP_TOLERANCE = 1.0e-10

# Colores.
COLOR_ARMIJO = "#E76F00"
COLOR_EXACT = "#1565C0"
COLOR_CURRENT = "#C62828"
COLOR_OPTIMUM = "#2E7D32"
COLOR_GRID = "#D5D8DC"


# ---------------------------------------------------------------------------
# Funciones del problema
# ---------------------------------------------------------------------------

def objective(x: np.ndarray) -> float:
    """Valor de f(x) = 1/2 x^T Q x."""
    x = np.asarray(x, dtype=float)
    return float(0.5 * x @ Q @ x)


def gradient(x: np.ndarray) -> np.ndarray:
    """Gradiente de f."""
    return Q @ np.asarray(x, dtype=float)


def line_objective(
    x: np.ndarray,
    direction: np.ndarray,
    alpha: np.ndarray,
) -> np.ndarray:
    """
    Evalúa la función objetivo sobre la recta de búsqueda:

        phi(alpha) = f(x + alpha * direction)

    Acepta alpha escalar o vector y devuelve un vector de valores.
    """
    alpha = np.atleast_1d(np.asarray(alpha, dtype=float))
    points = x[None, :] + alpha[:, None] * direction[None, :]
    return 0.5 * np.einsum("bi,ij,bj->b", points, Q, points)


# ---------------------------------------------------------------------------
# Reglas de elección de paso
# ---------------------------------------------------------------------------

def armijo_backtracking(
    x: np.ndarray,
    direction: np.ndarray,
    alpha_initial: float = ALPHA_INITIAL,
    beta: float = BETA,
    c1: float = C1,
    max_backtracks: int = MAX_BACKTRACKS,
) -> tuple[float, list[float]]:
    """
    Encuentra alpha por backtracking usando la regla de Armijo:

        f(x + alpha d) <= f(x) + c1 * alpha * grad f(x)^T d

    Se prueban alpha_0, beta*alpha_0, beta^2*alpha_0, ... y se acepta el
    primer valor que satisface la desigualdad.

    Devuelve:
        alpha_armijo : paso aceptado
        tested       : lista de pasos examinados, en orden

    Se exige que direction sea una dirección de descenso.
    """
    x = np.asarray(x, dtype=float)
    direction = np.asarray(direction, dtype=float)

    f_x = objective(x)
    directional_derivative = float(gradient(x) @ direction)

    if directional_derivative >= 0:
        raise ValueError("La dirección no es de descenso.")

    alpha = alpha_initial
    tested: list[float] = []

    for _ in range(max_backtracks):
        tested.append(alpha)

        f_candidate = objective(x + alpha * direction)
        armijo_bound = f_x + c1 * alpha * directional_derivative

        if f_candidate <= armijo_bound:
            return alpha, tested

        alpha *= beta

    raise RuntimeError(
        "Backtracking agotó los intentos sin cumplir la condición de Armijo."
    )


def exact_line_search(x: np.ndarray, direction: np.ndarray) -> float:
    """
    Búsqueda exacta para f(x) = 1/2 x^T Q x.

    Se minimiza phi(alpha) = f(x + alpha d). Como

        phi'(alpha) = g^T d + alpha d^T Q d,

    el minimizador en alpha >= 0 es

        alpha_exact = -(g^T d) / (d^T Q d).
    """
    x = np.asarray(x, dtype=float)
    direction = np.asarray(direction, dtype=float)

    g = gradient(x)
    numerator = -float(g @ direction)
    denominator = float(direction @ Q @ direction)

    if denominator <= 0:
        raise ValueError("La dirección no produce una recta cuadrática válida.")

    alpha_exact = numerator / denominator

    if alpha_exact < 0:
        raise ValueError("El minimizador exacto cae fuera de alpha >= 0.")

    return alpha_exact


def run_iterations(
    method: str,
    max_iterations: int = MAX_ITERATIONS,
    alpha_initial: float = ALPHA_INITIAL,
    beta: float = BETA,
    c1: float = C1,
) -> tuple[np.ndarray, np.ndarray, list[float]]:
    """
    Ejecuta steepest descent (direccion = -grad f) usando la regla indicada.

    method = "armijo"  -> backtracking con la condición de Armijo
    method = "exact"   -> búsqueda exacta sobre la dirección

    Devuelve:
        puntos : trayectoria x_0, x_1, ...
        valores : f(x_0), f(x_1), ...
        pasos   : alpha_0, alpha_1, ...
    """
    if method not in {"armijo", "exact"}:
        raise ValueError("method debe ser 'armijo' o 'exact'.")

    x = X0.copy()
    points = [x.copy()]
    values = [objective(x)]
    steps: list[float] = []

    for _ in range(max_iterations):
        g = gradient(x)

        if np.linalg.norm(g) <= GRADIENT_TOLERANCE:
            break

        direction = -g

        if method == "armijo":
            alpha, _ = armijo_backtracking(
                x, direction,
                alpha_initial=alpha_initial,
                beta=beta,
                c1=c1,
            )
        else:
            alpha = exact_line_search(x, direction)

        x_new = x + alpha * direction

        points.append(x_new.copy())
        values.append(objective(x_new))
        steps.append(alpha)

        if np.linalg.norm(x_new - x) <= STEP_TOLERANCE * (
            1.0 + np.linalg.norm(x)
        ):
            break

        x = x_new

    return np.asarray(points), np.asarray(values), steps


# ---------------------------------------------------------------------------
# Figuras
# ---------------------------------------------------------------------------

def configure_style() -> None:
    plt.rcParams.update({
        "font.size": 11,
        "axes.labelsize": 12,
        "axes.titlesize": 14,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.dpi": 110,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.axisbelow": True,
    })


def plot_line_search(
    x_current: np.ndarray,
    direction: np.ndarray,
    alpha_armijo: float,
    tested: list[float],
    alpha_exact: float,
    output_path: Path,
    c1: float = C1,
) -> None:
    """
    Dibuja phi(alpha) = f(x_k + alpha d_k), la recta que define el descenso
    suficiente de Armijo, los pasos examinados y el minimizador exacto.
    """
    alpha_plot = np.linspace(0.0, 2.2, 1000)
    phi = line_objective(x_current, direction, alpha_plot)

    f_current = objective(x_current)
    directional_derivative = float(gradient(x_current) @ direction)
    armijo_line = f_current + c1 * alpha_plot * directional_derivative

    fig, ax = plt.subplots(figsize=(11, 5.8))

    # Región que satisface la condición suficiente de Armijo.
    ax.axvspan(
        0.0,
        alpha_armijo,
        color=COLOR_ARMIJO,
        alpha=0.10,
        label="Región que satisface Armijo",
    )

    ax.plot(
        alpha_plot,
        phi,
        color="#222222",
        linewidth=2.4,
        label=r"$\phi(\alpha)=f(x_k+\alpha d_k)$",
    )

    ax.plot(
        alpha_plot,
        armijo_line,
        color=COLOR_ARMIJO,
        linestyle="--",
        linewidth=2.0,
        label=r"$f(x_k)+c_1\alpha\,\nabla f(x_k)^\top d_k$",
    )

    # Pasos examinados por el backtracking: rechazados y aceptado.
    for alpha in tested:
        accepted = np.isclose(alpha, alpha_armijo)
        value = objective(x_current + alpha * direction)

        ax.scatter(
            alpha,
            value,
            s=95 if accepted else 85,
            marker="o" if accepted else "X",
            color=COLOR_ARMIJO if accepted else "#8D6E63",
            edgecolor="white",
            linewidth=1.0,
            zorder=5,
        )

        ax.annotate(
            f"$\\alpha={alpha:.3f}$"
            + ("\n(aceptado)" if accepted else "\n(rechazado)"),
            xy=(alpha, value),
            xytext=(12, 30 if accepted else 42),
            textcoords="offset points",
            fontsize=9,
            color=COLOR_ARMIJO if accepted else "#6D4C41",
        )

    ax.axvline(alpha_armijo, color=COLOR_ARMIJO, linewidth=2.0, alpha=0.8)

    # Minimizador exacto de phi.
    ax.axvline(alpha_exact, color=COLOR_EXACT, linestyle=":", linewidth=2.5)
    phi_exact = objective(x_current + alpha_exact * direction)

    ax.scatter(
        alpha_exact,
        phi_exact,
        s=110,
        marker="*",
        color=COLOR_EXACT,
        edgecolor="white",
        linewidth=0.8,
        zorder=6,
    )

    ax.annotate(
        f"$\\alpha_{{\\mathrm{{exact}}}}={alpha_exact:.3f}$",
        xy=(alpha_exact, phi_exact),
        xytext=(12, -38),
        textcoords="offset points",
        fontsize=10,
        color=COLOR_EXACT,
        fontweight="bold",
    )

    ax.annotate(
        f"$\\alpha_{{\\mathrm{{Armijo}}}}={alpha_armijo:.3f}$",
        xy=(
            alpha_armijo,
            objective(x_current + alpha_armijo * direction),
        ),
        xytext=(-95, 40),
        textcoords="offset points",
        fontsize=10,
        color=COLOR_ARMIJO,
        fontweight="bold",
        arrowprops={"arrowstyle": "->", "color": COLOR_ARMIJO},
    )

    ax.set_xlim(0.0, 2.2)
    ax.set_ylim(bottom=min(0.0, float(phi.min()) * 1.10))
    ax.set_xlabel(r"Paso $\alpha$")
    ax.set_ylabel(r"Valor de la función")
    ax.set_title(
        "Búsqueda lineal en la primera iteración\n"
        "Armijo con backtracking frente a longitud exacta"
    )
    ax.grid(True, color=COLOR_GRID, linewidth=0.7)
    ax.legend(loc="best", frameon=False)

    fig.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_contours(
    points_armijo: np.ndarray,
    points_exact: np.ndarray,
    direction: np.ndarray,
    alpha_armijo: float,
    alpha_exact: float,
    output_path: Path,
) -> None:
    """
    Dibuja las curvas de nivel de f y las trayectorias completas de ambos
    métodos de steepest descent.
    """
    x_grid = np.linspace(-2.6, 2.4, 500)
    y_grid = np.linspace(-2.3, 1.9, 500)
    xx, yy = np.meshgrid(x_grid, y_grid)

    zz = 0.5 * (
        Q[0, 0] * xx**2
        + 2 * Q[0, 1] * xx * yy
        + Q[1, 1] * yy**2
    )

    # Niveles geométricos positivos: se omiten los valores casi planos.
    levels = np.geomspace(0.08, float(zz.max()), 14)

    fig, ax = plt.subplots(figsize=(9.2, 7))

    contours = ax.contour(
        xx, yy, zz,
        levels=levels,
        colors="#90A4AE",
        linewidths=0.9,
        alpha=0.9,
    )
    ax.clabel(contours, inline=True, fontsize=7, fmt="%.1f")

    # Dirección de descenso desde x_0.
    ax.arrow(
        X0[0], X0[1],
        direction[0], direction[1],
        length_includes_head=True,
        head_width=0.12,
        head_length=0.18,
        color=COLOR_CURRENT,
        linewidth=1.8,
        alpha=0.9,
    )

    ax.plot(
        points_armijo[:, 0], points_armijo[:, 1],
        color=COLOR_ARMIJO,
        linewidth=2.2,
        marker="o",
        markersize=4,
        label="Armijo + backtracking",
    )

    ax.plot(
        points_exact[:, 0], points_exact[:, 1],
        color=COLOR_EXACT,
        linewidth=2.2,
        marker="s",
        markersize=4,
        label="Longitud exacta",
    )

    armijo_point = X0 + alpha_armijo * direction
    exact_point = X0 + alpha_exact * direction

    ax.scatter(
        armijo_point[0], armijo_point[1],
        s=120, color=COLOR_ARMIJO,
        edgecolor="white", linewidth=1.0, zorder=6,
    )
    ax.scatter(
        exact_point[0], exact_point[1],
        s=120, color=COLOR_EXACT,
        edgecolor="white", linewidth=1.0, zorder=6,
    )

    ax.scatter(
        X0[0], X0[1],
        s=140, color=COLOR_CURRENT, marker="D",
        edgecolor="white", linewidth=1.0, zorder=7,
        label=r"Punto inicial $x_0$",
    )
    ax.scatter(
        0.0, 0.0,
        s=180, color=COLOR_OPTIMUM, marker="*",
        edgecolor="white", linewidth=0.8, zorder=7,
        label=r"Óptimo $x^\star=(0,0)$",
    )

    ax.annotate(
        "dirección de descenso",
        xy=X0 + 0.72 * direction,
        xytext=(20, 14),
        textcoords="offset points",
        color=COLOR_CURRENT,
        arrowprops={"arrowstyle": "-", "color": COLOR_CURRENT},
    )

    ax.set_xlim(x_grid.min(), x_grid.max())
    ax.set_ylim(y_grid.min(), y_grid.max())
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    ax.set_title("Trayectorias de steepest descent")
    ax.grid(True, color=COLOR_GRID, linewidth=0.5, alpha=0.7)
    ax.legend(loc="best", frameon=True)

    fig.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_convergence(
    values_armijo: np.ndarray,
    values_exact: np.ndarray,
    output_path: Path,
) -> None:
    """Compara f(x_k) en función del número de iteración."""
    floor = 1.0e-16

    fig, ax = plt.subplots(figsize=(9.5, 5.5))

    ax.semilogy(
        np.arange(len(values_armijo)),
        np.maximum(values_armijo, floor),
        color=COLOR_ARMIJO,
        linewidth=2.2,
        marker="o",
        markersize=5,
        label="Armijo + backtracking",
    )
    ax.semilogy(
        np.arange(len(values_exact)),
        np.maximum(values_exact, floor),
        color=COLOR_EXACT,
        linewidth=2.2,
        marker="s",
        markersize=5,
        label="Longitud exacta",
    )

    ax.set_xlabel("Iteración")
    ax.set_ylabel(r"$f(x_k)$")
    ax.set_title("Convergencia del valor objetivo")
    ax.grid(True, which="both", color=COLOR_GRID, linewidth=0.7)
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Compara la regla de Armijo con backtracking y la longitud "
            "de paso exacta."
        )
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "figuras",
        help="Directorio donde se guardarán las figuras.",
    )
    parser.add_argument(
        "--alpha-initial",
        type=float,
        default=ALPHA_INITIAL,
        help=f"Paso inicial del backtracking (default: {ALPHA_INITIAL}).",
    )
    parser.add_argument(
        "--beta",
        type=float,
        default=BETA,
        help=f"Factor de contracción (default: {BETA}).",
    )
    parser.add_argument(
        "--c1",
        type=float,
        default=C1,
        help=f"Parámetro c1 de Armijo (default: {C1}).",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Muestra las figuras al terminar.",
    )

    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    configure_style()

    # Primera iteración: la que ilustra la búsqueda lineal.
    x_current = X0.copy()
    direction = -gradient(x_current)

    alpha_armijo, tested = armijo_backtracking(
        x_current,
        direction,
        alpha_initial=args.alpha_initial,
        beta=args.beta,
        c1=args.c1,
    )
    alpha_exact = exact_line_search(x_current, direction)

    # Trayectorias completas.
    points_armijo, values_armijo, steps_armijo = run_iterations(
        "armijo",
        alpha_initial=args.alpha_initial,
        beta=args.beta,
        c1=args.c1,
    )
    points_exact, values_exact, steps_exact = run_iterations("exact")

    output_line = args.output_dir / "line_search_armijo_vs_exact.png"
    output_contours = args.output_dir / "contours_armijo_vs_exact.png"
    output_convergence = args.output_dir / "convergence_armijo_vs_exact.png"

    plot_line_search(
        x_current=x_current,
        direction=direction,
        alpha_armijo=alpha_armijo,
        tested=tested,
        alpha_exact=alpha_exact,
        output_path=output_line,
        c1=args.c1,
    )
    plot_contours(
        points_armijo=points_armijo,
        points_exact=points_exact,
        direction=direction,
        alpha_armijo=alpha_armijo,
        alpha_exact=alpha_exact,
        output_path=output_contours,
    )
    plot_convergence(
        values_armijo=values_armijo,
        values_exact=values_exact,
        output_path=output_convergence,
    )

    if args.show:
        # Las figuras ya se guardaron; se reabren para inspección.
        plt.show()

    print()
    print("Primera iteración")
    print("-" * 66)
    print(f"x_0                        = {X0}")
    print(f"direccion -grad f(x_0)     = {direction}")
    print(f"grad f(x_0)^T direccion    = {float(gradient(x_current) @ direction):.8f}")
    print(f"pasos examinados por Armijo = "
          f"{[round(a, 6) for a in tested]}")
    print(f"alpha aceptado por Armijo  = {alpha_armijo:.8f}")
    print(f"alpha exacto               = {alpha_exact:.8f}")
    print(f"f despues del paso Armijo  = "
          f"{objective(x_current + alpha_armijo * direction):.8f}")
    print(f"f despues del paso exacto  = "
          f"{objective(x_current + alpha_exact * direction):.8f}")
    print()
    print("Iteraciones hasta convergir")
    print("-" * 66)
    print(f"Armijo  : {len(steps_armijo)} pasos, "
          f"f final = {values_armijo[-1]:.3e}")
    print(f"Exacto  : {len(steps_exact)} pasos, "
          f"f final = {values_exact[-1]:.3e}")
    print()
    print("Figuras guardadas en:")
    for path in (output_line, output_contours, output_convergence):
        print(f"  {path.resolve()}")


if __name__ == "__main__":
    main()
