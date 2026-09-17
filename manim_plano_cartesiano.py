"""Manim video: "Localización de puntos en el plano cartesiano".

Renderiza un video corto (~35s) que explica cómo localizar puntos en
el plano cartesiano, usando los mismos ejemplos didácticos que la sección
1.1 de `docs/temas_basicos_funciones.md`. Render estándar:
    manim -pqh manim_plano_cartesiano.py PlanoCartesiano
    manim -pqh --resolution=1920,1080 manim_plano_cartesiano.py PlanoCartesiano
"""

from manim import (
    Scene, Axes, Dot, Text, VGroup, Arrow, Rectangle, Line, DashedLine,
    Create, Write, FadeIn, FadeOut, AnimationGroup,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    BLUE, RED, GREEN, YELLOW, ORANGE, PURPLE, WHITE,
    GREY_A, GREY_C, GREY_D, BLACK, PURE_RED,
    MathTex,
)
import numpy as np


class PlanoCartesiano(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Fijar dimensiones razonables para legibilidad
        # self.camera.frame_width = 14

        # ────────────────────────────────────────────────────────────────
        # ESCENA 1 — Título
        # ────────────────────────────────────────────────────────────────
        titulo = Text(
            "Localización de puntos en el plano cartesiano",
            font="Latin Modern Roman",
            color=BLACK,
        ).scale(0.7)
        subtitulo = Text(
            "¿Cómo se ubica un punto (x, y)?",
            font="Latin Modern Roman",
            color=GREY_D,
        ).scale(0.45).next_to(titulo, DOWN, buff=0.3)

        self.play(Write(titulo), run_time=1.6)
        self.play(FadeIn(subtitulo, shift=UP * 0.3), run_time=1.0)
        self.wait(1.2)
        self.play(FadeOut(titulo), FadeOut(subtitulo))
        self.wait(0.4)

        # ────────────────────────────────────────────────────────────────
        # ESCENA 2 — Aparece el plano cartesiano con ejes y origen
        # ────────────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={
                "color": GREY_A,
                "stroke_width": 2,
                "include_numbers": False,
            },
            tips=True,
        ).shift(DOWN * 0.2)

        # Etiquetas X, Y
        x_label = MathTex("x", color=BLACK).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.2
        ).scale(0.9)
        y_label = MathTex("y", color=BLACK).next_to(
            axes.y_axis.get_end(), UP, buff=0.2
        ).scale(0.9)
        origin_label = MathTex("O", color=BLACK).next_to(
            axes.c2p(0, 0), DOWN + LEFT, buff=0.12
        ).scale(0.7)

        # Marca visible del origen
        origen_dot = Dot(axes.c2p(0, 0), color=BLACK, radius=0.06)

        # Texto "Origen"
        origen_texto = Text("(0, 0) — Origen", font="Latin Modern Roman",
                            color=BLACK).scale(0.4).to_edge(UP, buff=0.3)

        self.play(Create(axes), run_time=2.0)
        self.play(
            FadeIn(x_label, shift=LEFT * 0.2),
            FadeIn(y_label, shift=DOWN * 0.2),
            run_time=0.8,
        )
        self.play(FadeIn(origen_dot, scale=0.5),
                  Write(origin_label), run_time=0.8)
        self.play(Write(origen_texto), run_time=1.0)
        self.wait(1.6)
        self.play(FadeOut(origen_texto), FadeOut(origen_dot),
                  FadeOut(origin_label))

        # ────────────────────────────────────────────────────────────────
        # ESCENA 3 — Cuadrantes: I, II, III, IV
        # ────────────────────────────────────────────────────────────────
        # Cuadrantes como rectángulos de fondo muy tenues
        def quad_rect(x0, y0, x1, y1):
            return Rectangle(
                width=axes.c2p(x1, 0)[0] - axes.c2p(x0, 0)[0],
                height=axes.c2p(0, y1)[1] - axes.c2p(0, y0)[1],
                stroke_width=0,
                fill_color=BLUE,
                fill_opacity=0.06,
            ).move_to(
                [(axes.c2p(x0, 0)[0] + axes.c2p(x1, 0)[0]) / 2,
                 (axes.c2p(0, y0)[1] + axes.c2p(0, y1)[1]) / 2,
                 0]
            )

        q1 = quad_rect(0, 0, 5, 4)        # I:  (+, +)
        q2 = quad_rect(-5, 0, 0, 4)       # II: (-, +)
        q3 = quad_rect(-5, -4, 0, 0)      # III:(-, -)
        q4 = quad_rect(0, -4, 5, 0)       # IV: (+, -)

        roman = lambda t, c=BLACK: MathTex(t, color=c).scale(0.7)
        q1_lbl = roman("I").move_to(axes.c2p(2.5, 2.0))
        q2_lbl = roman("II").move_to(axes.c2p(-2.5, 2.0))
        q3_lbl = roman("III").move_to(axes.c2p(-2.5, -2.0))
        q4_lbl = roman("IV").move_to(axes.c2p(2.5, -2.0))

        signs_I = MathTex("(+,\ +)", color=GREY_D).scale(0.45).next_to(q1_lbl, DOWN, buff=0.15)
        signs_II = MathTex("(-,\ +)", color=GREY_D).scale(0.45).next_to(q2_lbl, DOWN, buff=0.15)
        signs_III = MathTex("(-,\ -)", color=GREY_D).scale(0.45).next_to(q3_lbl, DOWN, buff=0.15)
        signs_IV = MathTex("(+\ ,\ -)", color=GREY_D).scale(0.45).next_to(q4_lbl, DOWN, buff=0.15)

        self.play(
            FadeIn(q1), FadeIn(q2), FadeIn(q3), FadeIn(q4),
            run_time=0.7,
        )
        self.play(
            FadeIn(q1_lbl, scale=0.6), FadeIn(signs_I),
            FadeIn(q2_lbl, scale=0.6), FadeIn(signs_II),
            FadeIn(q3_lbl, scale=0.6), FadeIn(signs_III),
            FadeIn(q4_lbl, scale=0.6), FadeIn(signs_IV),
            run_time=1.2,
        )
        self.wait(2.0)

        # ────────────────────────────────────────────────────────────────
        # ESCENA 4 — Cómo se lee un par ordenado
        # ────────────────────────────────────────────────────────────────
        par_label = MathTex("(x,\ y)", color=BLACK).scale(1.5).to_edge(UP, buff=0.4)
        x_expl = MathTex("x", color=RED).scale(0.9).next_to(par_label, DOWN, buff=0.35).shift(LEFT * 1.7)
        x_text = Text("abscisa", color=BLACK, font="Latin Modern Roman").scale(0.32).next_to(x_expl, DOWN, buff=0.12)
        y_expl = MathTex("y", color=BLUE).scale(0.9).next_to(par_label, DOWN, buff=0.35).shift(RIGHT * 1.7)
        y_text = Text("ordenada", color=BLACK, font="Latin Modern Roman").scale(0.32).next_to(y_expl, DOWN, buff=0.12)
        x_arrow = Arrow(par_label.get_bottom() + LEFT * 0.18 + DOWN * 0.05,
                        x_expl.get_top(), color=RED, stroke_width=2, buff=0.05)
        y_arrow = Arrow(par_label.get_bottom() + RIGHT * 0.18 + DOWN * 0.05,
                        y_expl.get_top(), color=BLUE, stroke_width=2, buff=0.05)

        self.play(Write(par_label), run_time=1.0)
        self.play(
            Create(x_arrow), FadeIn(x_expl), FadeIn(x_text),
            run_time=0.8,
        )
        self.play(
            Create(y_arrow), FadeIn(y_expl), FadeIn(y_text),
            run_time=0.8,
        )
        self.wait(2.2)
        self.play(
            FadeOut(par_label), FadeOut(x_expl), FadeOut(x_text),
            FadeOut(y_expl), FadeOut(y_text),
            FadeOut(x_arrow), FadeOut(y_arrow),
        )

        # ────────────────────────────────────────────────────────────────
        # ESCENA 5 — Ejemplo 1: P(3, 2)
        # ────────────────────────────────────────────────────────────────
        def locate(coord, color_pt=PURE_RED, label_offset=DOWN + RIGHT * 0.6,
                   example_text=None, persist_label=True, tick_color=GREY_C):
            """Ubica un punto en el plano trazando líneas guía."""
            x, y = coord
            c = axes.c2p(x, y)
            cx = axes.c2p(x, 0)
            cy = axes.c2p(0, y)

            # Líneas guía punteadas desde el punto a los ejes
            h_line = DashedLine(
                start=c, end=cx,
                color=tick_color, stroke_width=2, dash_length=0.12,
            )
            v_line = DashedLine(
                start=c, end=cy,
                color=tick_color, stroke_width=2, dash_length=0.12,
            )

            # Marcas de tick en los ejes
            x_tick = Dot(cx, color=color_pt, radius=0.07)
            y_tick = Dot(cy, color=color_pt, radius=0.07)
            x_val_label = MathTex(f"{x}", color=BLACK).scale(0.5).next_to(
                cx, DOWN, buff=0.15,
            )
            y_val_label = MathTex(f"{y}", color=BLACK).scale(0.5).next_to(
                cy, LEFT, buff=0.15,
            )

            punto = Dot(c, color=color_pt, radius=0.10)
            label = MathTex(f"P({x},\ {y})", color=color_pt).scale(0.6)
            label.move_to(c + label_offset)

            anims = []
            if example_text is not None:
                anims.append(FadeIn(example_text, shift=DOWN * 0.2))
            anims += [
                Create(h_line),
                Create(v_line),
                FadeIn(x_tick, scale=0.4),
                FadeIn(y_tick, scale=0.4),
                Write(x_val_label),
                Write(y_val_label),
                FadeIn(punto, scale=0.3),
            ]
            if persist_label:
                anims.append(Write(label))
            self.play(AnimationGroup(*anims, lag_ratio=0.3), run_time=2.6)
            self.wait(0.5)
            return h_line, v_line, x_tick, y_tick, x_val_label, y_val_label, punto, label

        # Limpio elementos del plano cartesiano (quad_lbl y rect) y dejo
        # solo los ejes para reutilizarlos con el ejemplo.
        self.play(
            FadeOut(q1), FadeOut(q2), FadeOut(q3), FadeOut(q4),
            FadeOut(q1_lbl), FadeOut(signs_I),
            FadeOut(q2_lbl), FadeOut(signs_II),
            FadeOut(q3_lbl), FadeOut(signs_III),
            FadeOut(q4_lbl), FadeOut(signs_IV),
            run_time=0.7,
        )

        # Ejemplo 1
        ej1 = Text("Ejemplo 1:  P(3, 2)", font="Latin Modern Roman",
                   color=BLACK).scale(0.5).to_edge(UP, buff=0.3)
        artifacts1 = locate((3, 2), example_text=ej1,
                            label_offset=DOWN + RIGHT * 0.5)
        h1, v1, xt1, yt1, xl1, yl1, p1, lbl1 = artifacts1
        self.wait(2.0)
        self.play(
            FadeOut(h1), FadeOut(v1),
            FadeOut(xt1), FadeOut(yt1),
            FadeOut(xl1), FadeOut(yl1),
            FadeOut(p1), FadeOut(lbl1),
            FadeOut(ej1),
        )

        # ────────────────────────────────────────────────────────────────
        # ESCENA 6 — Ejemplo 2:  P(−2, 3)  (cuadrante II)
        # ────────────────────────────────────────────────────────────────
        ej2 = Text("Ejemplo 2:  P(−2, 3)", font="Latin Modern Roman",
                   color=BLACK).scale(0.5).to_edge(UP, buff=0.3)
        artifacts2 = locate((-2, 3), example_text=ej2,
                            label_offset=UP + LEFT * 0.5,
                            color_pt=BLUE)
        h2, v2, xt2, yt2, xl2, yl2, p2, lbl2 = artifacts2
        self.wait(2.0)
        self.play(
            FadeOut(h2), FadeOut(v2),
            FadeOut(xt2), FadeOut(yt2),
            FadeOut(xl2), FadeOut(yl2),
            FadeOut(p2), FadeOut(lbl2),
            FadeOut(ej2),
        )

        # ────────────────────────────────────────────────────────────────
        # ESCENA 7 — Ejemplo 3:  P(−3, −2)  (cuadrante III)
        # ────────────────────────────────────────────────────────────────
        ej3 = Text("Ejemplo 3:  P(−3, −2)", font="Latin Modern Roman",
                   color=BLACK).scale(0.5).to_edge(UP, buff=0.3)
        artifacts3 = locate((-3, -2), example_text=ej3,
                            label_offset=DOWN + LEFT * 0.7,
                            color_pt=ORANGE)
        h3, v3, xt3, yt3, xl3, yl3, p3, lbl3 = artifacts3
        self.wait(2.0)

        # ────────────────────────────────────────────────────────────────
        # ESCENA 8 — Resumen final
        # ────────────────────────────────────────────────────────────────
        self.play(
            FadeOut(h3), FadeOut(v3),
            FadeOut(xt3), FadeOut(yt3),
            FadeOut(xl3), FadeOut(yl3),
            FadeOut(p3), FadeOut(lbl3),
            FadeOut(ej3),
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
        )

        resumen = VGroup(
            Text("Resumen", font="Latin Modern Roman",
                 color=BLACK).scale(0.7),
            Text("• Un punto se representa como (x, y).", font="Latin Modern Roman",
                 color=BLACK).scale(0.45),
            Text("• x: cuántos pasos a la derecha (o izquierda) desde el origen.",
                 font="Latin Modern Roman", color=BLACK).scale(0.4),
            Text("• y: cuántos pasos hacia arriba (o abajo) desde el origen.",
                 font="Latin Modern Roman", color=BLACK).scale(0.4),
            Text("• El signo (x, y) determina el cuadrante.",
                 font="Latin Modern Roman", color=BLACK).scale(0.4),
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)

        for linea in resumen:
            self.play(FadeIn(linea, shift=RIGHT * 0.2), run_time=0.55)
        self.wait(2.0)
        self.play(*[FadeOut(m) for m in resumen], run_time=1.0)
        self.wait(0.4)


if __name__ == "__main__":
    pass
