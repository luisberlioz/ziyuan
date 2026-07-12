"""
Manim animation: Equivalencia entre forma logarítmica y forma exponencial.

Basado en la sección 1.1 (Definición) y 1.3 (Conversión) de
logaritmos_y_ecuaciones.md del sitio Ziyuan.

    log_b N = x   ⟺   b^x = N

Animación: muestra la equivalencia usando el ejemplo canónico
log_2 32 = 5  ⟺  2^5 = 32, identifica las partes, y resume la
conversión bidireccional y las restricciones del dominio.

Render:
    source /data/MyTera/openclaw/workspace/projects/polynomial-animation/.venv/bin/activate
    cd /data/MyTera/ziyuan
    manim -ql logaritmos_equivalencia.py EquivalenciaLogExponencial   # preview 480p
    manim -qh logaritmos_equivalencia.py EquivalenciaLogExponencial   # final 1080p
"""

from manim import (
    Scene,
    Text,
    Tex,
    MathTex,
    VGroup,
    Arrow,
    SurroundingRectangle,
    DashedLine,
    Create,
    Write,
    FadeIn,
    FadeOut,
    Transform,
    ReplacementTransform,
    Indicate,
    Circumscribe,
    LaggedStart,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    ORIGIN,
    BLUE,
    YELLOW,
    GREEN,
    RED,
    ORANGE,
    WHITE,
    GREY,
    ITALIC,
    ManimColor,
    ArrowTriangleFilledTip,
)
import numpy as np


# Paleta consistente con el sitio Ziyuan (tema indigo)
PRIMARY = ManimColor("#3F51B5")    # indigo
ACCENT = ManimColor("#FF9800")     # naranja
LOG_COLOR = ManimColor("#1976D2")  # azul (forma log)
EXP_COLOR = ManimColor("#E65100")  # naranja oscuro (forma exp)


class EquivalenciaLogExponencial(Scene):
    """Ilustra log_b N = x  ⟺  b^x = N con el ejemplo log_2 32 = 5."""

    def construct(self):
        self.intro()
        self.seccion_ejemplo()
        self.seccion_partes()
        self.seccion_transformacion()
        self.seccion_restricciones()
        self.seccion_cierre()

    # -----------------------------------------------------------------
    # Helpers
    # -----------------------------------------------------------------
    def _make_double_arrow(self, mob1, mob2, color=YELLOW, buff=0.4, vertical_shift=0):
        """Flecha ⟺ entre dos mobjects."""
        start = mob1.get_right() + RIGHT * buff + UP * vertical_shift
        end = mob2.get_left() + LEFT * buff + UP * vertical_shift
        arrow = Arrow(
            start,
            end,
            color=color,
            stroke_width=6,
            buff=0,
            max_tip_length_to_length_ratio=0.18,
            tip_shape=ArrowTriangleFilledTip,
        )
        # Punta al inicio para hacer ⟸---⟹  (equivalente a ⟺ con doble punta)
        arrow.add_tip(tip_shape=ArrowTriangleFilledTip, at_start=True)
        return arrow

    # -----------------------------------------------------------------
    # 0. Intro
    # -----------------------------------------------------------------
    def intro(self):
        titulo = Text(
            "Equivalencia: forma logarítmica ↔ forma exponencial",
            font_size=34,
            color=WHITE,
        ).to_edge(UP, buff=0.4)

        subtitulo = Tex(
            r"$\log_b N = x \quad \Longleftrightarrow \quad b^x = N$",
            font_size=44,
        ).next_to(titulo, DOWN, buff=0.3)

        self.play(Write(titulo))
        self.play(Write(subtitulo))
        self.wait(0.6)

        # Mantener referencia al título; el subtítulo se reemplaza después
        self.titulo = titulo
        self.subtitulo_intro = subtitulo

    # -----------------------------------------------------------------
    # 1. Ejemplo concreto
    # -----------------------------------------------------------------
    def seccion_ejemplo(self):
        # Quitar subtítulo de intro para dar espacio
        self.play(FadeOut(self.subtitulo_intro), shift=UP * 0.5)

        sec = Text("1. Ejemplo concreto", font_size=26, color=ACCENT)
        sec.to_edge(LEFT, buff=0.6).shift(UP * 2.0)

        # Forma logarítmica (lado izquierdo)
        log_form = MathTex(r"\log_2 32 = 5", font_size=60, color=LOG_COLOR)
        log_form.move_to(LEFT * 3.2 + DOWN * 0.4)

        # Forma exponencial (lado derecho)
        exp_form = MathTex(r"2^5 = 32", font_size=60, color=EXP_COLOR)
        exp_form.move_to(RIGHT * 3.2 + DOWN * 0.4)

        # Flecha doble ⟺ entre ellas
        double_arrow = self._make_double_arrow(log_form, exp_form, buff=0.3)

        # Etiquetas "logarítmica" / "exponencial"
        lbl_log = Text("Forma logarítmica", font_size=22, color=LOG_COLOR)
        lbl_log.next_to(log_form, UP, buff=0.45)
        lbl_exp = Text("Forma exponencial", font_size=22, color=EXP_COLOR)
        lbl_exp.next_to(exp_form, UP, buff=0.45)

        self.play(Write(sec))
        self.play(Write(lbl_log), Write(log_form))
        self.wait(0.3)
        self.play(Create(double_arrow, run_time=1.2), Write(lbl_exp))
        self.play(Write(exp_form))
        self.wait(0.8)

        # Resaltar ambas formas a la vez
        box_log = SurroundingRectangle(log_form, color=LOG_COLOR, buff=0.15)
        box_exp = SurroundingRectangle(exp_form, color=EXP_COLOR, buff=0.15)
        self.play(Create(box_log), Create(box_exp))
        self.wait(0.5)
        self.play(FadeOut(box_log), FadeOut(box_exp))

        self.log_form = log_form
        self.exp_form = exp_form
        self.double_arrow = double_arrow
        self.lbl_log = lbl_log
        self.lbl_exp = lbl_exp
        self.sec_ejemplo = sec
        self.wait(0.4)

    # -----------------------------------------------------------------
    # 2. Partes
    # -----------------------------------------------------------------
    def seccion_partes(self):
        # Subir todo lo anterior
        grupo = VGroup(
            self.lbl_log, self.log_form, self.double_arrow,
            self.lbl_exp, self.exp_form,
        )
        self.play(grupo.animate.shift(UP * 1.4))

        sec = Text("2. Las piezas del rompecabezas", font_size=26, color=ACCENT)
        sec.next_to(self.sec_ejemplo, DOWN, buff=0.55).align_to(self.sec_ejemplo, LEFT)

        # Construimos MathTex con `\log_{2}` para que LaTeX pinte bien la base.
        # Usaremos dos MathTex separados (uno a cada lado) en lugar de partir
        # strings, que es propenso a errores de render.
        log_partes = MathTex(r"\log_{2} 32 = 5", font_size=56, color=LOG_COLOR)
        log_partes.move_to(LEFT * 3.2 + DOWN * 1.6)

        exp_partes = MathTex(r"2^{5} = 32", font_size=56, color=EXP_COLOR)
        exp_partes.move_to(RIGHT * 3.2 + DOWN * 1.6)

        # Flecha ⟺
        arrow = self._make_double_arrow(log_partes, exp_partes, buff=0.3)

        # Etiquetas superiores (forma log)
        # log_partes submobjects típicos: [0]=log, [1]=2 (subscript), [2]=,
        # [3]=32, [4]==, [5]=5. Vamos a usar índices seguros: las piezas
        # visuales que queremos etiquetar están claramente separadas.
        # Ubicación por aproximación usando la geometría del MathTex:
        log_left_x = log_partes.get_x() - 1.4
        log_mid_x = log_partes.get_x() - 0.1
        log_right_x = log_partes.get_x() + 1.4

        lbl_base_log = Text("base  b", font_size=20, color=LOG_COLOR)
        lbl_base_log.move_to([log_left_x, log_partes.get_y() + 1.0, 0])
        ln_base_log = DashedLine(
            lbl_base_log.get_bottom(), [log_left_x + 0.3, log_partes.get_y() + 0.3, 0],
            color=LOG_COLOR, stroke_width=2,
        )

        lbl_arg_log = Text("argumento  N", font_size=20, color=LOG_COLOR)
        lbl_arg_log.move_to([log_mid_x, log_partes.get_y() + 1.0, 0])
        ln_arg_log = DashedLine(
            lbl_arg_log.get_bottom(), [log_mid_x, log_partes.get_y() + 0.4, 0],
            color=LOG_COLOR, stroke_width=2,
        )

        lbl_x_log = Text("logaritmo  x", font_size=20, color=LOG_COLOR)
        lbl_x_log.move_to([log_right_x, log_partes.get_y() + 1.0, 0])
        ln_x_log = DashedLine(
            lbl_x_log.get_bottom(), [log_right_x, log_partes.get_y() + 0.4, 0],
            color=LOG_COLOR, stroke_width=2,
        )

        # Etiquetas inferiores (forma exp)
        exp_left_x = exp_partes.get_x() - 1.4
        exp_mid_x = exp_partes.get_x() + 0.3
        exp_right_x = exp_partes.get_x() + 1.7

        lbl_base_exp = Text("base  b", font_size=20, color=EXP_COLOR)
        lbl_base_exp.move_to([exp_left_x, exp_partes.get_y() - 1.0, 0])
        ln_base_exp = DashedLine(
            [exp_left_x, exp_partes.get_y() - 0.4, 0], lbl_base_exp.get_top(),
            color=EXP_COLOR, stroke_width=2,
        )

        lbl_exp_exp = Text("exponente  x", font_size=20, color=EXP_COLOR)
        lbl_exp_exp.move_to([exp_mid_x, exp_partes.get_y() - 1.0, 0])
        ln_exp_exp = DashedLine(
            [exp_mid_x, exp_partes.get_y() - 0.3, 0], lbl_exp_exp.get_top(),
            color=EXP_COLOR, stroke_width=2,
        )

        lbl_N_exp = Text("resultado  N", font_size=20, color=EXP_COLOR)
        lbl_N_exp.move_to([exp_right_x, exp_partes.get_y() - 1.0, 0])
        ln_N_exp = DashedLine(
            [exp_right_x, exp_partes.get_y() - 0.4, 0], lbl_N_exp.get_top(),
            color=EXP_COLOR, stroke_width=2,
        )

        self.play(Write(sec))
        self.play(FadeOut(self.log_form), FadeOut(self.exp_form))
        self.play(Write(log_partes), Write(exp_partes), Create(arrow))
        self.wait(0.3)

        # Aparecer etiquetas de la forma log
        self.play(
            Write(lbl_base_log), Create(ln_base_log),
            Write(lbl_arg_log), Create(ln_arg_log),
            Write(lbl_x_log), Create(ln_x_log),
        )
        self.wait(0.4)

        # Aparecer etiquetas de la forma exp
        self.play(
            Write(lbl_base_exp), Create(ln_base_exp),
            Write(lbl_exp_exp), Create(ln_exp_exp),
            Write(lbl_N_exp), Create(ln_N_exp),
        )
        self.wait(0.8)

        # Resaltar las correspondencias b↔b, N↔N, x↔x
        vg_b = VGroup(lbl_base_log, ln_base_log, lbl_base_exp, ln_base_exp)
        vg_N = VGroup(lbl_arg_log, ln_arg_log, lbl_N_exp, ln_N_exp)
        vg_x = VGroup(lbl_x_log, ln_x_log, lbl_exp_exp, ln_exp_exp)

        self.play(Circumscribe(vg_b, color=YELLOW), run_time=1.2)
        self.play(Circumscribe(vg_N, color=YELLOW), run_time=1.2)
        self.play(Circumscribe(vg_x, color=YELLOW), run_time=1.2)
        self.wait(0.4)

        self.log_partes = log_partes
        self.exp_partes = exp_partes
        self.arrow_partes = arrow
        self.sec_partes = sec
        self.grupo_etiquetas = VGroup(
            lbl_base_log, ln_base_log,
            lbl_arg_log, ln_arg_log,
            lbl_x_log, ln_x_log,
            lbl_base_exp, ln_base_exp,
            lbl_exp_exp, ln_exp_exp,
            lbl_N_exp, ln_N_exp,
        )
        self.wait(0.4)

    # -----------------------------------------------------------------
    # 3. Transformación bidireccional
    # -----------------------------------------------------------------
    def seccion_transformacion(self):
        # Subir partes y limpiar cabeceras
        grupo = VGroup(
            self.log_partes, self.exp_partes, self.arrow_partes,
            self.grupo_etiquetas,
        )
        self.play(grupo.animate.shift(UP * 0.7))
        self.play(FadeOut(self.sec_partes))

        sec = Text("3. La conversión es reversible", font_size=26, color=ACCENT)
        sec.next_to(self.sec_ejemplo, DOWN, buff=0.55).align_to(self.sec_ejemplo, LEFT)

        # Bloque superior: log → exp
        sub1 = Text("De logarítmica a exponencial:", font_size=22, color=LOG_COLOR)
        sub1.move_to(UP * 0.2 + LEFT * 4.0)

        ejemplo_log = MathTex(r"\log_2 32 = 5", font_size=48, color=LOG_COLOR)
        ejemplo_log.move_to(DOWN * 0.4 + LEFT * 4.0)

        flecha1 = Arrow(
            ejemplo_log.get_right() + RIGHT * 0.3,
            RIGHT * 1.5 + DOWN * 0.4,
            color=YELLOW, stroke_width=5, buff=0,
            max_tip_length_to_length_ratio=0.18,
            tip_shape=ArrowTriangleFilledTip,
        )
        ejemplo_exp = MathTex(r"2^{5} = 32", font_size=48, color=EXP_COLOR)
        ejemplo_exp.move_to(DOWN * 0.4 + RIGHT * 3.5)

        # Bloque inferior: exp → log
        sub2 = Text("De exponencial a logarítmica:", font_size=22, color=EXP_COLOR)
        sub2.move_to(DOWN * 1.5 + LEFT * 4.0)

        ejemplo_exp2 = MathTex(r"2^{5} = 32", font_size=48, color=EXP_COLOR)
        ejemplo_exp2.move_to(DOWN * 2.1 + LEFT * 4.0)

        flecha2 = Arrow(
            ejemplo_exp2.get_right() + RIGHT * 0.3,
            RIGHT * 1.5 + DOWN * 2.1,
            color=YELLOW, stroke_width=5, buff=0,
            max_tip_length_to_length_ratio=0.18,
            tip_shape=ArrowTriangleFilledTip,
        )
        ejemplo_log2 = MathTex(r"\log_2 32 = 5", font_size=48, color=LOG_COLOR)
        ejemplo_log2.move_to(DOWN * 2.1 + RIGHT * 3.5)

        self.play(Write(sec))
        self.play(Write(sub1), Write(ejemplo_log))
        self.play(Create(flecha1), Write(ejemplo_exp))
        self.wait(0.6)
        self.play(Write(sub2), Write(ejemplo_exp2))
        self.play(Create(flecha2), Write(ejemplo_log2))
        self.wait(0.6)

        # Indicarlas a la vez: son la misma información
        self.play(
            Indicate(ejemplo_log, color=LOG_COLOR, scale_factor=1.1),
            Indicate(ejemplo_log2, color=LOG_COLOR, scale_factor=1.1),
            Indicate(ejemplo_exp, color=EXP_COLOR, scale_factor=1.1),
            Indicate(ejemplo_exp2, color=EXP_COLOR, scale_factor=1.1),
        )
        self.wait(0.4)

        self.grupo_transform = VGroup(
            sub1, ejemplo_log, flecha1, ejemplo_exp,
            sub2, ejemplo_exp2, flecha2, ejemplo_log2,
            sec,
        )
        self.wait(0.4)

    # -----------------------------------------------------------------
    # 4. Restricciones
    # -----------------------------------------------------------------
    def seccion_restricciones(self):
        from manim.mobject.types.vectorized_mobject import VMobject
        # Limpiar casi todo dejando solo el título principal.
        # self.mobjects puede contener objetos que no son VMobject (cámara,
        # marcadores internos) por lo que filtramos por tipo VMobject.
        todo = VGroup(*[m for m in self.mobjects
                        if m is not self.titulo and isinstance(m, VMobject)])
        self.play(FadeOut(todo))

        sec = Text("4. Restricciones obligatorias", font_size=28, color=ACCENT)
        sec.next_to(self.titulo, DOWN, buff=0.4).align_to(self.titulo, LEFT).shift(LEFT * 4.0)

        restricciones = VGroup(
            Tex(r"Base: $\, b > 0$  y  $b \neq 1$", font_size=34),
            Tex(r"Argumento: $\, N > 0$", font_size=34),
            Tex(r"Resultado: $\, b^x > 0$  siempre", font_size=32, color=GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        restricciones.next_to(sec, DOWN, buff=0.5).align_to(sec, LEFT)

        ejes = self._mini_axes().scale(0.9)
        ejes.move_to(RIGHT * 3.4 + DOWN * 0.6)

        caption = Text(
            "El logaritmo sólo existe\ndonde la curva está definida",
            font_size=20, color=GREY,
        ).next_to(ejes, DOWN, buff=0.3)

        self.play(Write(sec))
        self.play(LaggedStart(*[Write(r) for r in restricciones], lag_ratio=0.4))
        self.play(Create(ejes), Write(caption))
        self.wait(1.2)
        self.wait(0.4)

    def _mini_axes(self):
        """Mini-gráfico de y = log_2(x)."""
        from manim import Axes

        axes = Axes(
            x_range=[-0.5, 9, 1],
            y_range=[-3, 4, 1],
            x_length=5.5,
            y_length=3.4,
            tips=False,
            axis_config={"stroke_color": GREY, "include_numbers": False},
        )

        def f(x):
            return np.log2(x) if x > 0 else None

        curva = axes.plot(
            f, x_range=[0.05, 8.5, 0.05],
            color=LOG_COLOR, stroke_width=4,
            use_smoothing=False,
        )
        asintota = DashedLine(
            axes.c2p(0, -3), axes.c2p(0, 4),
            color=RED, stroke_width=2,
        )
        x_label = MathTex("x", font_size=28).next_to(axes.x_axis, RIGHT, buff=0.15)
        y_label = MathTex("y", font_size=28).next_to(axes.y_axis, UP, buff=0.15)
        return VGroup(axes, curva, asintota, x_label, y_label)

    # -----------------------------------------------------------------
    # 5. Cierre
    # -----------------------------------------------------------------
    def seccion_cierre(self):
        from manim.mobject.types.vectorized_mobject import VMobject
        todo = VGroup(*[m for m in self.mobjects
                        if m is not self.titulo and isinstance(m, VMobject)])
        self.play(FadeOut(todo))

        msg1 = Text(
            "Forma logarítmica y forma exponencial",
            font_size=32, color=WHITE,
        )
        msg2 = Text(
            "son dos caras de la misma moneda.",
            font_size=32, color=ACCENT,
        )
        msg3 = Tex(
            r"$\log_b N = x \quad \Longleftrightarrow \quad b^x = N$",
            font_size=44,
        )
        msg4 = Text(
            "Toda propiedad logarítmica tiene su equivalente exponencial.",
            font_size=22, color=GREY, slant=ITALIC,
        )

        grupo = VGroup(msg1, msg2, msg3, msg4).arrange(DOWN, buff=0.35)
        grupo.move_to(DOWN * 0.2)

        self.play(Write(msg1))
        self.play(Write(msg2))
        self.play(Write(msg3))
        self.wait(0.5)
        self.play(Write(msg4))
        self.wait(2.5)
        # self.mobjects contiene no solo Mobjects sino también estado interno
        # de la escena, así que filtramos a VMobject.
        from manim.mobject.types.vectorized_mobject import VMobject
        todo = VGroup(*[m for m in self.mobjects if isinstance(m, VMobject)])
        self.play(FadeOut(todo))
        self.wait(0.3)
