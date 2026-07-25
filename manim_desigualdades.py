"""Manim video: "Propiedades de las desigualdades lineales".

Tres escenas animadas que ilustran las reglas básicas para resolver
desigualdades lineales, usando una recta numérica como ancla visual:

    1. Sumar el mismo número a ambos lados preserva el orden.
       Si x < y, entonces x + 42 < y + 42.

    2. Multiplicar por un número positivo preserva el orden.
       Si x < y y c > 0, entonces c·x < c·y.

    3. Multiplicar por un número negativo invierte el orden.
       Si x < y y c < 0, entonces c·x > c·y.

Render estándar (1080p, ~55s):
    manim -pqh manim_desigualdades.py DesigualdadesLineales
"""

from manim import (
    Scene, VGroup, Text, MathTex,
    Line, Dot, Arrow, DoubleArrow, Rectangle,
    NumberLine,
    Create, Write, FadeIn, FadeOut, Transform, AnimationGroup,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    BLUE, RED, GREEN, YELLOW, ORANGE, PURPLE, PINK, TEAL,
    GREY_A, GREY_B, GREY_C, GREY_D, GREY_E,
    BLACK, WHITE,
)
import numpy as np


class DesigualdadesLineales(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ────────────────────────────────────────────────────────────────
        # ESCENA 1 — Título
        # ────────────────────────────────────────────────────────────────
        titulo = Text(
            "Propiedades de las desigualdades",
            font="Latin Modern Roman",
            color=BLACK,
        ).scale(0.75)
        subtitulo = Text(
            "Suma y multiplicación",
            font="Latin Modern Roman",
            color=GREY_D,
        ).scale(0.5).next_to(titulo, DOWN, buff=0.35)

        self.play(Write(titulo), run_time=1.6)
        self.play(FadeIn(subtitulo, shift=UP * 0.3), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(titulo), FadeOut(subtitulo))
        self.wait(0.4)

        # ────────────────────────────────────────────────────────────────
        # ESCENA 2 — Hipótesis: x < y sobre la recta real
        # ────────────────────────────────────────────────────────────────
        # Recta numérica centrada en el origen, con marcas cada 5 unidades
        recta = NumberLine(
            x_range=[-15, 15, 5],
            length=11,
            color=GREY_A,
            stroke_width=2,
            include_numbers=True,
            label_direction=DOWN,
            font_size=22,
        ).shift(DOWN * 1.0)
        # Etiqueta "ℝ" al final de la recta
        r_label = MathTex(r"\mathbb{R}", color=GREY_D).scale(0.55).next_to(
            recta.get_end(), RIGHT, buff=0.12,
        )

        # Hipótesis mostrada arriba
        hip = VGroup(
            MathTex("x,\ y", color=BLACK).scale(1.0),
            MathTex(r"\in \mathbb{R}", color=BLACK).scale(0.9),
            MathTex(r"\text{con }", color=BLACK).scale(0.9),
            MathTex("x", color=RED).scale(1.0),
            MathTex("<", color=BLACK).scale(1.0),
            MathTex("y", color=BLUE).scale(1.0),
        ).arrange(RIGHT, buff=0.15).to_edge(UP, buff=0.6)

        # Puntos en la recta
        x_val, y_val = -4.0, 6.0  # x_val < y_val
        dot_x = Dot(recta.n2p(x_val), color=RED, radius=0.10)
        dot_y = Dot(recta.n2p(y_val), color=BLUE, radius=0.10)
        label_x = MathTex("x", color=RED).scale(0.85).next_to(
            dot_x, UP, buff=0.18,
        )
        label_y = MathTex("y", color=BLUE).scale(0.85).next_to(
            dot_y, UP, buff=0.18,
        )

        self.play(Create(recta), FadeIn(r_label), run_time=1.4)
        self.play(Write(hip), run_time=1.6)
        self.play(
            FadeIn(dot_x, scale=0.5), Write(label_x),
            FadeIn(dot_y, scale=0.5), Write(label_y),
            run_time=1.2,
        )
        self.wait(1.5)

        # ────────────────────────────────────────────────────────────────
        # ESCENA 3 — Propiedad 1: SUMA preserva el orden
        # ────────────────────────────────────────────────────────────────
        # Etiqueta "Propiedad 1" + enunciado
        prop1_tit = Text(
            "Propiedad 1 — Suma",
            font="Latin Modern Roman",
            color=BLACK,
        ).scale(0.55).to_edge(UP, buff=0.25)
        prop1_tit.shift(LEFT * 0.0)

        # Enunciado (lado a lado)
        prop1 = VGroup(
            MathTex("x", color=RED).scale(1.0),
            MathTex("+", color=BLACK).scale(1.0),
            MathTex("42", color=GREEN).scale(1.0),
            MathTex(r"\ <\ ", color=BLACK).scale(1.0),
            MathTex("y", color=BLUE).scale(1.0),
            MathTex("+", color=BLACK).scale(1.0),
            MathTex("42", color=GREEN).scale(1.0),
        ).arrange(RIGHT, buff=0.12).next_to(recta, UP, buff=0.9)

        self.play(FadeOut(hip), run_time=0.5)
        self.play(Write(prop1_tit), run_time=0.8)
        self.play(Write(prop1), run_time=1.5)
        self.wait(0.8)

        # Flecha de desplazamiento sobre cada punto (recta → x+42, y+42)
        delta = 6.0  # unidades a sumar en la recta
        arrow_dx = Arrow(
            start=dot_x.get_center(),
            end=recta.n2p(x_val + delta),
            color=GREEN, buff=0, stroke_width=5,
            max_tip_length_to_length_ratio=0.12,
        )
        arrow_dy = Arrow(
            start=dot_y.get_center(),
            end=recta.n2p(y_val + delta),
            color=GREEN, buff=0, stroke_width=5,
            max_tip_length_to_length_ratio=0.12,
        )
        self.play(Create(arrow_dx), Create(arrow_dy), run_time=0.9)

        # Etiqueta "+42" sobre cada flecha
        plus42_x = MathTex("+42", color=GREEN).scale(0.55).next_to(
            arrow_dx, UP, buff=0.10,
        )
        plus42_y = MathTex("+42", color=GREEN).scale(0.55).next_to(
            arrow_dy, UP, buff=0.10,
        )
        self.play(FadeIn(plus42_x), FadeIn(plus42_y), run_time=0.6)

        # Animar: ambos puntos se desplazan +delta simultáneamente
        new_x_val, new_y_val = x_val + delta, y_val + delta
        new_dot_x = Dot(recta.n2p(new_x_val), color=RED, radius=0.10)
        new_dot_y = Dot(recta.n2p(new_y_val), color=BLUE, radius=0.10)
        new_label_x = MathTex("x+42", color=RED).scale(0.7).next_to(
            new_dot_x, UP, buff=0.18,
        )
        new_label_y = MathTex("y+42", color=BLUE).scale(0.7).next_to(
            new_dot_y, UP, buff=0.18,
        )
        # Doble flecha mostrando que la distancia se conserva
        distance_arrow = DoubleArrow(
            start=recta.n2p(new_x_val) + DOWN * 0.35,
            end=recta.n2p(new_y_val) + DOWN * 0.35,
            color=GREY_B, stroke_width=2, buff=0.0,
            max_tip_length_to_length_ratio=0.08,
        )
        distance_text = Text(
            "distancia igual",
            font="Latin Modern Roman",
            color=GREY_D,
        ).scale(0.30).next_to(distance_arrow, DOWN, buff=0.15)

        self.play(
            Transform(dot_x, new_dot_x),
            Transform(dot_y, new_dot_y),
            FadeOut(arrow_dx), FadeOut(arrow_dy),
            FadeOut(plus42_x), FadeOut(plus42_y),
            FadeOut(label_x), FadeOut(label_y),
            run_time=1.4,
        )
        self.play(
            Write(new_label_x), Write(new_label_y),
            Create(distance_arrow), Write(distance_text),
            run_time=1.0,
        )
        self.wait(1.2)

        # Caption de conclusión
        conclusion1 = Text(
            "Sumar el mismo número a ambos lados preserva el orden.",
            font="Latin Modern Roman",
            color=BLACK,
        ).scale(0.4).to_edge(DOWN, buff=0.3)
        self.play(Write(conclusion1), run_time=1.2)
        self.wait(1.6)

        # Limpiar para la siguiente propiedad
        self.play(
            FadeOut(prop1_tit), FadeOut(prop1),
            FadeOut(conclusion1),
            FadeOut(distance_arrow), FadeOut(distance_text),
            FadeOut(new_label_x), FadeOut(new_label_y),
        )

        # ────────────────────────────────────────────────────────────────
        # ESCENA 4 — Propiedad 2: MULTIPLICACIÓN POR POSITIVO
        # Perspectiva: ambos lados crecen proporcionalmente desde el cero.
        # ────────────────────────────────────────────────────────────────
        # Restablecer los puntos a valores positivos para mostrar crecimiento
        # desde el cero de manera inequívoca (ambos valores crecerán a la
        # derecha del cero, sin cruzar el origen).
        x_val, y_val = 2.0, 5.0
        mult = 2.0

        self.play(FadeOut(dot_x), FadeOut(dot_y), run_time=0.4)
        dot_x = Dot(recta.n2p(x_val), color=RED, radius=0.10)
        dot_y = Dot(recta.n2p(y_val), color=BLUE, radius=0.10)
        label_x = MathTex("x", color=RED).scale(0.85).next_to(
            dot_x, UP, buff=0.18,
        )
        label_y = MathTex("y", color=BLUE).scale(0.85).next_to(
            dot_y, UP, buff=0.18,
        )

        # Marcar el cero como punto de referencia (perspectiva)
        origen_dot = Dot(recta.n2p(0), color=BLACK, radius=0.13)
        origen_label = MathTex("0", color=BLACK).scale(0.85).next_to(
            origen_dot, DOWN, buff=0.22,
        )

        self.play(
            FadeIn(dot_x, scale=0.5), FadeIn(dot_y, scale=0.5),
            FadeIn(label_x), FadeIn(label_y),
            FadeIn(origen_dot, scale=0.5), FadeIn(origen_label),
            run_time=1.0,
        )
        self.wait(0.4)

        # Enunciado: si c = 2 > 0, entonces 2·x < 2·y
        prop2_tit = Text(
            "Propiedad 2 — Multiplicación por un número positivo",
            font="Latin Modern Roman",
            color=BLACK,
        ).scale(0.55).to_edge(UP, buff=0.25)

        prop2 = VGroup(
            MathTex("2", color=GREEN).scale(1.0),
            MathTex(r"\cdot\ ", color=BLACK).scale(1.0),
            MathTex("x", color=RED).scale(1.0),
            MathTex(r"\ <\ ", color=BLACK).scale(1.0),
            MathTex("2", color=GREEN).scale(1.0),
            MathTex(r"\cdot\ ", color=BLACK).scale(1.0),
            MathTex("y", color=BLUE).scale(1.0),
        ).arrange(RIGHT, buff=0.10).next_to(recta, UP, buff=0.9)

        cond2 = MathTex(
            r"\text{con } c = 2 > 0",
            color=GREY_D,
        ).scale(0.55).next_to(prop2, DOWN, buff=0.18)

        self.play(Write(prop2_tit), run_time=0.9)
        self.play(Write(prop2), Write(cond2), run_time=1.5)
        self.wait(0.6)

        # Barras de magnitud desde el cero: visualizan "qué tan lejos del 0"
        # está cada punto. Al multiplicar por 2, ambas barras crecen
        # proporcionalmente — la barra azul (y) sigue siendo la mayor.
        # Las ponemos a alturas ligeramente distintas para que ambas se vean
        # (si comparten y, la más larga oculta a la corta en el solapamiento).
        mag_y_x = DOWN * 0.55   # barra roja (x)
        mag_y_y = DOWN * 0.72   # barra azul (y), más abajo

        mag_bar_x = Line(
            start=recta.n2p(0) + mag_y_x,
            end=recta.n2p(x_val) + mag_y_x,
            color=RED, stroke_width=8,
        )
        mag_bar_y = Line(
            start=recta.n2p(0) + mag_y_y,
            end=recta.n2p(y_val) + mag_y_y,
            color=BLUE, stroke_width=8,
        )
        mag_lbl_x = MathTex("2", color=RED).scale(0.55).next_to(
            mag_bar_x, DOWN, buff=0.18,
        )
        mag_lbl_y = MathTex("5", color=BLUE).scale(0.55).next_to(
            mag_bar_y, DOWN, buff=0.18,
        )
        # Marca vertical en el origen que ancla ambas barras
        origen_tick_mag = Line(
            start=recta.n2p(0) + mag_y_x + UP * 0.05,
            end=recta.n2p(0) + mag_y_y + DOWN * 0.05,
            color=BLACK, stroke_width=2,
        )

        self.play(
            Create(origen_tick_mag),
            Create(mag_bar_x), Create(mag_bar_y),
            FadeIn(mag_lbl_x), FadeIn(mag_lbl_y),
            run_time=1.2,
        )
        self.wait(0.6)

        # ───── Multiplicar por 2: ambos lados crecen desde el cero ─────
        new_x_val, new_y_val = x_val * mult, y_val * mult  # 4, 10
        new_dot_x2 = Dot(recta.n2p(new_x_val), color=RED, radius=0.10)
        new_dot_y2 = Dot(recta.n2p(new_y_val), color=BLUE, radius=0.10)
        new_label_x2 = MathTex("2x", color=RED).scale(0.7).next_to(
            new_dot_x2, UP, buff=0.18,
        )
        new_label_y2 = MathTex("2y", color=BLUE).scale(0.7).next_to(
            new_dot_y2, UP, buff=0.18,
        )

        new_mag_bar_x = Line(
            start=recta.n2p(0) + mag_y_x,
            end=recta.n2p(new_x_val) + mag_y_x,
            color=RED, stroke_width=8,
        )
        new_mag_bar_y = Line(
            start=recta.n2p(0) + mag_y_y,
            end=recta.n2p(new_y_val) + mag_y_y,
            color=BLUE, stroke_width=8,
        )
        new_mag_lbl_x = MathTex("4", color=RED).scale(0.55).next_to(
            new_mag_bar_x, DOWN, buff=0.18,
        )
        new_mag_lbl_y = MathTex("10", color=BLUE).scale(0.55).next_to(
            new_mag_bar_y, DOWN, buff=0.18,
        )

        # Animar puntos y magnitudes en paralelo — Transform interpola los
        # extremos de las líneas, así que las barras "crecen" desde el cero.
        self.play(
            Transform(dot_x, new_dot_x2),
            Transform(dot_y, new_dot_y2),
            Transform(mag_bar_x, new_mag_bar_x),
            Transform(mag_bar_y, new_mag_bar_y),
            FadeOut(label_x), FadeOut(label_y),
            FadeOut(mag_lbl_x), FadeOut(mag_lbl_y),
            run_time=1.6,
        )
        self.play(
            Write(new_label_x2), Write(new_label_y2),
            Write(new_mag_lbl_x), Write(new_mag_lbl_y),
            run_time=1.0,
        )
        self.wait(1.0)

        conclusion2 = Text(
            "Multiplicar por un número positivo preserva el orden:\n"
            "ambos lados crecen proporcionalmente desde el cero.",
            font="Latin Modern Roman",
            color=BLACK,
        ).scale(0.4).to_edge(DOWN, buff=0.3)
        self.play(Write(conclusion2), run_time=1.4)
        self.wait(1.8)

        self.play(
            FadeOut(prop2_tit), FadeOut(prop2), FadeOut(cond2),
            FadeOut(conclusion2),
            FadeOut(origen_dot), FadeOut(origen_label),
            FadeOut(mag_bar_x), FadeOut(mag_bar_y),
            FadeOut(new_label_x2), FadeOut(new_label_y2),
            FadeOut(new_mag_lbl_x), FadeOut(new_mag_lbl_y),
            FadeOut(origen_tick_mag),
        )

        # ────────────────────────────────────────────────────────────────
        # ESCENA 5 — Propiedad 3: MULTIPLICACIÓN POR NEGATIVO (invierte)
        # ────────────────────────────────────────────────────────────────
        # Restablecer puntos a la posición original
        self.play(FadeOut(dot_x), FadeOut(dot_y), run_time=0.4)
        dot_x = Dot(recta.n2p(x_val), color=RED, radius=0.10)
        dot_y = Dot(recta.n2p(y_val), color=BLUE, radius=0.10)
        label_x = MathTex("x", color=RED).scale(0.85).next_to(
            dot_x, UP, buff=0.18,
        )
        label_y = MathTex("y", color=BLUE).scale(0.85).next_to(
            dot_y, UP, buff=0.18,
        )
        self.play(
            FadeIn(dot_x, scale=0.5), FadeIn(dot_y, scale=0.5),
            FadeIn(label_x), FadeIn(label_y),
            run_time=0.8,
        )

        prop3_tit = Text(
            "Propiedad 3 — Multiplicación por un número negativo",
            font="Latin Modern Roman",
            color=BLACK,
        ).scale(0.55).to_edge(UP, buff=0.25)

        # Enunciado: si c < 0, entonces c·x > c·y  (orden invertido)
        prop3 = VGroup(
            MathTex(r"(-\!2)", color=PINK).scale(1.0),
            MathTex(r"\cdot\ ", color=BLACK).scale(1.0),
            MathTex("x", color=RED).scale(1.0),
            MathTex(r"\ >\ ", color=PINK).scale(1.0),
            MathTex(r"(-\!2)", color=PINK).scale(1.0),
            MathTex(r"\cdot\ ", color=BLACK).scale(1.0),
            MathTex("y", color=BLUE).scale(1.0),
        ).arrange(RIGHT, buff=0.10).next_to(recta, UP, buff=0.9)

        cond3 = MathTex(
            r"\text{con } c = -2 < 0 \quad \Longrightarrow \quad \text{el orden se invierte}",
            color=GREY_D,
        ).scale(0.55).next_to(prop3, DOWN, buff=0.18)

        self.play(Write(prop3_tit), run_time=0.9)
        self.play(Write(prop3), Write(cond3), run_time=1.6)
        self.wait(1.0)

        # Animar paso a paso: primero la reflexión (×-1) y luego el escalado
        # Paso A: reflexión a través del origen (×−1)
        neg_x_val = -x_val  # 4
        neg_y_val = -y_val  # -6
        mid_dot_x = Dot(recta.n2p(neg_x_val), color=RED, radius=0.10)
        mid_dot_y = Dot(recta.n2p(neg_y_val), color=BLUE, radius=0.10)
        # Flechas que muestran el "giro" a través del origen
        reflect_arrow_x = Arrow(
            start=dot_x.get_center(),
            end=recta.n2p(neg_x_val),
            color=PINK, buff=0, stroke_width=5,
            max_tip_length_to_length_ratio=0.10,
        )
        reflect_arrow_y = Arrow(
            start=dot_y.get_center(),
            end=recta.n2p(neg_y_val),
            color=PINK, buff=0, stroke_width=5,
            max_tip_length_to_length_ratio=0.10,
        )
        reflect_lbl = MathTex(r"\text{reflejar}", color=PINK).scale(0.55)
        reflect_lbl.next_to(recta.get_center(), UP, buff=2.3)

        self.play(Create(reflect_arrow_x), Create(reflect_arrow_y),
                  FadeIn(reflect_lbl), run_time=0.9)
        self.play(
            Transform(dot_x, mid_dot_x),
            Transform(dot_y, mid_dot_y),
            FadeOut(reflect_arrow_x), FadeOut(reflect_arrow_y),
            FadeOut(label_x), FadeOut(label_y),
            run_time=1.4,
        )

        # Mostrar: ahora el orden está invertido
        mid_label_x = MathTex("-x", color=RED).scale(0.7).next_to(
            dot_x, UP, buff=0.18,
        )
        mid_label_y = MathTex("-y", color=BLUE).scale(0.7).next_to(
            dot_y, UP, buff=0.18,
        )
        self.play(Write(mid_label_x), Write(mid_label_y), run_time=0.8)
        # Etiqueta de orden invertido
        order_swap = Text(
            "el orden se invirtió",
            font="Latin Modern Roman",
            color=PINK,
        ).scale(0.35).next_to(recta, UP, buff=2.55)
        self.play(FadeOut(reflect_lbl), Write(order_swap), run_time=0.9)
        self.wait(1.0)

        # Paso B: escalado ×2 (manteniendo el signo negativo)
        # (-1) × (-2) sobre los puntos actuales:
        # punto en 4  →  -8
        # punto en -6 →  12
        final_x_val = neg_x_val * 2  # 8 con un signo extra
        # Como partimos de (-1)*x y multiplicamos por (-2), el resultado es 2*x
        # Mejor: aplicamos la transformación global c·x con c=-2 directamente
        final_x_val = -2 * x_val   # -2 · (-4) = 8
        final_y_val = -2 * y_val   # -2 · 6 = -12
        final_dot_x = Dot(recta.n2p(final_x_val), color=RED, radius=0.10)
        final_dot_y = Dot(recta.n2p(final_y_val), color=BLUE, radius=0.10)

        scale_arrow_x = Arrow(
            start=recta.n2p(neg_x_val),
            end=recta.n2p(final_x_val),
            color=PINK, buff=0, stroke_width=5,
            max_tip_length_to_length_ratio=0.10,
        )
        scale_arrow_y = Arrow(
            start=recta.n2p(neg_y_val),
            end=recta.n2p(final_y_val),
            color=PINK, buff=0, stroke_width=5,
            max_tip_length_to_length_ratio=0.10,
        )
        scale_lbl_x = MathTex(r"\times 2", color=PINK).scale(0.55).next_to(
            scale_arrow_x, UP, buff=0.10,
        )
        scale_lbl_y = MathTex(r"\times 2", color=PINK).scale(0.55).next_to(
            scale_arrow_y, UP, buff=0.10,
        )
        self.play(
            Create(scale_arrow_x), Create(scale_arrow_y),
            FadeIn(scale_lbl_x), FadeIn(scale_lbl_y),
            run_time=0.9,
        )
        self.play(
            Transform(dot_x, final_dot_x),
            Transform(dot_y, final_dot_y),
            FadeOut(mid_label_x), FadeOut(mid_label_y),
            FadeOut(scale_arrow_x), FadeOut(scale_arrow_y),
            FadeOut(scale_lbl_x), FadeOut(scale_lbl_y),
            run_time=1.5,
        )

        final_label_x = MathTex("-2x", color=RED).scale(0.7).next_to(
            dot_x, UP, buff=0.18,
        )
        final_label_y = MathTex("-2y", color=BLUE).scale(0.7).next_to(
            dot_y, UP, buff=0.18,
        )
        self.play(
            Write(final_label_x), Write(final_label_y),
            FadeOut(order_swap),
            run_time=1.0,
        )
        self.wait(1.0)

        conclusion3 = Text(
            "Multiplicar por un número negativo invierte el orden.",
            font="Latin Modern Roman",
            color=BLACK,
        ).scale(0.4).to_edge(DOWN, buff=0.3)
        self.play(Write(conclusion3), run_time=1.4)
        self.wait(1.8)

        # ────────────────────────────────────────────────────────────────
        # ESCENA 6 — Resumen final
        # ────────────────────────────────────────────────────────────────
        self.play(
            FadeOut(prop3_tit), FadeOut(prop3), FadeOut(cond3),
            FadeOut(conclusion3),
            FadeOut(recta), FadeOut(r_label),
            FadeOut(dot_x), FadeOut(dot_y),
            FadeOut(final_label_x), FadeOut(final_label_y),
        )

        resumen_tit = Text(
            "Resumen",
            font="Latin Modern Roman",
            color=BLACK,
        ).scale(0.75).to_edge(UP, buff=0.6)

        # Tres líneas, una por propiedad
        resumen = VGroup(
            VGroup(
                MathTex("x", color=RED).scale(0.7),
                MathTex("<", color=BLACK).scale(0.7),
                MathTex("y", color=BLUE).scale(0.7),
                MathTex(r"\ \Longrightarrow\ ", color=BLACK).scale(0.7),
                MathTex("x + a", color=BLACK).scale(0.7),
                MathTex("<", color=GREEN).scale(0.7),
                MathTex("y + a", color=BLACK).scale(0.7),
            ).arrange(RIGHT, buff=0.10),
            VGroup(
                MathTex("x", color=RED).scale(0.7),
                MathTex("<", color=BLACK).scale(0.7),
                MathTex("y", color=BLUE).scale(0.7),
                MathTex(r",\ c > 0\ \Longrightarrow\ ", color=BLACK).scale(0.7),
                MathTex("cx", color=BLACK).scale(0.7),
                MathTex("<", color=GREEN).scale(0.7),
                MathTex("cy", color=BLACK).scale(0.7),
            ).arrange(RIGHT, buff=0.10),
            VGroup(
                MathTex("x", color=RED).scale(0.7),
                MathTex("<", color=BLACK).scale(0.7),
                MathTex("y", color=BLUE).scale(0.7),
                MathTex(r",\ c < 0\ \Longrightarrow\ ", color=BLACK).scale(0.7),
                MathTex("cx", color=BLACK).scale(0.7),
                MathTex(">", color=PINK).scale(0.7),
                MathTex("cy", color=BLACK).scale(0.7),
            ).arrange(RIGHT, buff=0.10),
        ).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(Write(resumen_tit), run_time=1.0)
        for linea in resumen:
            self.play(FadeIn(linea, shift=RIGHT * 0.2), run_time=0.7)
        self.wait(2.5)
        self.play(
            *[FadeOut(m) for m in [resumen_tit, *resumen]],
            run_time=1.0,
        )
        self.wait(0.4)


if __name__ == "__main__":
    pass