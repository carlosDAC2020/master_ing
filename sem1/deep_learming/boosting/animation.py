"""
comando para el renderizado de la animacion
uv run manim -pql animation.py BoostingPresentation

uv run manim --save_sections -pql animation.py BoostingPresentation
"""

from manim import *

class BoostingPresentation(Scene):
    def construct(self):
        # 1. Introduction
        self.next_section(name="Introduction")
        self.show_intro()
        self.wait(1)

        # 2. Diagrama Ilustrativo
        self.next_section(name="Diagrama Ilustrativo")
        self.show_diagram()
        self.wait(1)

        # 3. Iterative Refinement
        self.next_section(name="Iterative Refinement")
        self.show_refinement()
        self.wait(1)

        # 4. Learning Rate
        self.next_section(name="Learning Rate")
        self.show_learning_rate()
        self.wait(1)

        # 5. Regularization
        self.next_section(name="Regularization")
        self.show_regularization()
        self.wait(1)

        # 6. Real World Applications
        self.next_section(name="Real World Applications")
        self.show_real_world_intro()
        self.wait(1)

        self.next_section(name="Fraud Detection")
        self.show_fraud_detection()
        self.wait(1)

        self.next_section(name="Recommendation Systems")
        self.show_recommendation_systems()
        self.wait(1)

        self.next_section(name="Credit Risk")
        self.show_credit_risk()
        self.wait(1)

        self.next_section(name="End")
        self.end()
        self.wait(1)


    def create_dot_grid(self, colors, rows=2, cols=5, radius=0.15, buff=0.12):
        """Creates a grid of colored circles inside a rounded rectangle."""
        dots = VGroup()
        for i in range(rows):
            for j in range(cols):
                dot = Circle(radius=radius, fill_opacity=1, stroke_width=1, stroke_color=WHITE)
                dot.set_fill(colors[i * cols + j])
                dot.move_to([j * (radius * 2 + buff), -i * (radius * 2 + buff), 0])
                dots.add(dot)
        dots.move_to(ORIGIN)
        box = RoundedRectangle(
            corner_radius=0.15, width=dots.width + 0.4, height=dots.height + 0.4,
            stroke_color=WHITE, stroke_width=1.5, fill_color=BLACK, fill_opacity=0.3
        ).move_to(dots.get_center())
        return VGroup(box, dots)

    def create_model_box(self, label_text, color=BLUE):
        """Creates a visual decision tree diagram with a label underneath."""
        node_radius = 0.12
        h_gap = 0.45   # horizontal gap between siblings
        v_gap = 0.5    # vertical gap between levels

        # ── Nodes ──
        root = Circle(radius=node_radius, fill_opacity=1, stroke_width=1.5, stroke_color=WHITE)
        root.set_fill(color)

        mid_left = Circle(radius=node_radius, fill_opacity=1, stroke_width=1.5, stroke_color=WHITE)
        mid_left.set_fill(color)
        mid_right = Circle(radius=node_radius, fill_opacity=1, stroke_width=1.5, stroke_color=WHITE)
        mid_right.set_fill(color)

        leaf1 = Circle(radius=node_radius * 0.8, fill_opacity=1, stroke_width=1, stroke_color=WHITE)
        leaf1.set_fill(color).set_opacity(0.7)
        leaf2 = Circle(radius=node_radius * 0.8, fill_opacity=1, stroke_width=1, stroke_color=WHITE)
        leaf2.set_fill(color).set_opacity(0.7)
        leaf3 = Circle(radius=node_radius * 0.8, fill_opacity=1, stroke_width=1, stroke_color=WHITE)
        leaf3.set_fill(color).set_opacity(0.7)
        leaf4 = Circle(radius=node_radius * 0.8, fill_opacity=1, stroke_width=1, stroke_color=WHITE)
        leaf4.set_fill(color).set_opacity(0.7)

        # ── Position nodes ──
        root.move_to(ORIGIN)
        mid_left.move_to(LEFT * h_gap + DOWN * v_gap)
        mid_right.move_to(RIGHT * h_gap + DOWN * v_gap)
        leaf1.move_to(LEFT * h_gap * 1.5 + DOWN * v_gap * 2)
        leaf2.move_to(LEFT * h_gap * 0.5 + DOWN * v_gap * 2)
        leaf3.move_to(RIGHT * h_gap * 0.5 + DOWN * v_gap * 2)
        leaf4.move_to(RIGHT * h_gap * 1.5 + DOWN * v_gap * 2)

        # ── Edges (lines connecting nodes) ──
        edges = VGroup(
            Line(root.get_center(), mid_left.get_center(), stroke_width=1.5, color=color),
            Line(root.get_center(), mid_right.get_center(), stroke_width=1.5, color=color),
            Line(mid_left.get_center(), leaf1.get_center(), stroke_width=1.5, color=color),
            Line(mid_left.get_center(), leaf2.get_center(), stroke_width=1.5, color=color),
            Line(mid_right.get_center(), leaf3.get_center(), stroke_width=1.5, color=color),
            Line(mid_right.get_center(), leaf4.get_center(), stroke_width=1.5, color=color),
        )

        nodes = VGroup(root, mid_left, mid_right, leaf1, leaf2, leaf3, leaf4)
        tree = VGroup(edges, nodes)

        # ── Label below tree ──
        label = Text(label_text, font_size=18, color=color).next_to(tree, DOWN, buff=0.15)

        return VGroup(tree, label)

    def create_result_box(self, label_text, dot_colors, box_color, rows=None, cols=None):
        """Creates a small result box with dots and a label on top."""
        n = len(dot_colors)
        if rows is None:
            rows = max(1, (n + 2) // 3)
            cols = min(n, 3)
        dots = VGroup()
        for i in range(rows):
            for j in range(cols):
                idx = i * cols + j
                if idx < n:
                    dot = Circle(radius=0.1, fill_opacity=1, stroke_width=0.5, stroke_color=WHITE)
                    dot.set_fill(dot_colors[idx])
                    dot.move_to([j * 0.3, -i * 0.3, 0])
                    dots.add(dot)
        dots.move_to(ORIGIN)
        box = RoundedRectangle(
            corner_radius=0.1, width=max(dots.width + 0.3, 1.2), height=dots.height + 0.3,
            stroke_color=box_color, stroke_width=1.5, fill_color=box_color, fill_opacity=0.08
        ).move_to(dots.get_center())
        label = Text(label_text, font_size=22, color=box_color).next_to(box, UP, buff=0.1)
        return VGroup(label, box, dots)

    # ── Main Diagram Method ──

    def show_diagram(self):
        # Title
        diagram_title = Text("¿Cómo funciona Boosting?", font_size=40)
        self.play(Write(diagram_title))
        self.wait(1)
        self.play(diagram_title.animate.scale(0.6).to_corner(UL))

        # ── Colors ──
        GRAY_DOT = GRAY_C
        GREEN_DOT = "#2ecc71"
        RED_DOT = "#e74c3c"

        # ── Iteration config ──
        iterations = [
            {"model": "Modelo #1", "color": BLUE,  "correct": 3, "incorrect": 7},
            {"model": "Modelo #2", "color": TEAL,  "correct": 5, "incorrect": 5},
            {"model": "Modelo #3", "color": GOLD,  "correct": 8, "incorrect": 2},
        ]

        prev_incorrect = 0

        for idx, it in enumerate(iterations):
            # ── Iteration label (below title, right side) ──
            iter_label = Text(
                f"Iteración {idx + 1}", font_size=24, color=GRAY_B
            ).to_edge(UP, buff=0.6).shift(RIGHT * 4)

            # ── Data box ──
            if idx == 0:
                data_colors = [GRAY_DOT] * 10
                data_label_text = "Datos"
            else:
                data_colors = [RED_DOT] * prev_incorrect + [GRAY_DOT] * (10 - prev_incorrect)
                data_label_text = "Datos (ponderados)"

            data = self.create_dot_grid(data_colors)
            data.move_to(LEFT * 3.5)

            data_label = Text(data_label_text, font_size=22, color=WHITE).next_to(data, UP, buff=0.2)

            # ── Arrow → Model ──
            arrow1 = Arrow(
                data.get_right() + RIGHT * 0.1, data.get_right() + RIGHT * 1.6,
                buff=0, stroke_width=2.5, color=GRAY_B
            )

            # ── Model box ──
            model = self.create_model_box(it["model"], it["color"])
            model.next_to(arrow1, RIGHT, buff=0.1)

            # ── Arrow → Results ──
            arrow2 = Arrow(
                model.get_right() + RIGHT * 0.1, model.get_right() + RIGHT * 1.6,
                buff=0, stroke_width=2.5, color=GRAY_B
            )

            # ── Result boxes ──
            correct_box = self.create_result_box("Correctos", [GREEN_DOT] * it["correct"], GREEN_DOT)
            incorrect_box = self.create_result_box("Incorrectos", [RED_DOT] * it["incorrect"], RED_DOT)
            results = VGroup(correct_box, incorrect_box).arrange(DOWN, buff=0.4)
            results.next_to(arrow2, RIGHT, buff=0.15)

            # ── Animate pipeline ──
            self.play(FadeIn(iter_label))
            self.play(FadeIn(data), FadeIn(data_label))
            self.play(GrowArrow(arrow1))
            self.play(FadeIn(model))
            self.play(GrowArrow(arrow2))
            self.wait(0.3)

            # ── Animate dots changing color ──
            dots = data[1]
            green_anims = [dots[i].animate.set_fill(GREEN_DOT) for i in range(it["correct"])]
            red_anims = [dots[i].animate.set_fill(RED_DOT) for i in range(it["correct"], 10)]
            self.play(*green_anims, *red_anims, run_time=1.5)
            self.wait(0.3)

            # ── Show results ──
            self.play(FadeIn(results))
            self.wait(1.5)

            # ── Group everything for cleanup ──
            iter_group = VGroup(iter_label, data, data_label, arrow1, model, arrow2, results)

            # ── Transition to next iteration ──
            if idx < len(iterations) - 1:
                # Text below incorrect box indicating error feedback
                feed_label = Text(
                    "⬇ Más peso a errores", font_size=20, color=RED_DOT
                ).next_to(incorrect_box, DOWN, buff=0.25)

                self.play(FadeIn(feed_label))
                self.wait(1)

                # Fade out everything before next iteration
                self.play(FadeOut(iter_group), FadeOut(feed_label))
            else:
                # Last iteration: fade out before final result
                self.wait(1)
                self.play(FadeOut(iter_group))

            prev_incorrect = it["incorrect"]

        # ═══════════════════════════════════════
        # FINAL RESULT
        # ═══════════════════════════════════════
        final_title = Text("Resultado Final (Combinación)", font_size=32, color=WHITE).shift(UP * 2)
        final_colors = [GREEN_DOT] * 8 + [RED_DOT] * 2
        final_grid = self.create_dot_grid(final_colors)
        final_grid.scale(1.3).move_to(ORIGIN)

        accuracy_label = Text("~80% de precisión", font_size=30, color=GREEN_DOT).next_to(final_grid, DOWN, buff=0.5)

        self.play(FadeIn(final_title))
        self.play(FadeIn(final_grid))
        self.play(FadeIn(accuracy_label))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(final_title), FadeOut(final_grid), FadeOut(accuracy_label), FadeOut(diagram_title))

    def show_intro(self):
        # Title - Grande al incio
        title = Text("Boosting (Ensamble Secuencial)", font_size=48)
        author = Text("Carlos Daniel Agamez", font_size=32, color=BLUE_A).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), Write(author))
        self.wait(1)
        # Se reduce (scale) y se mueve a la esquina, el nombre desaparece
        self.play(
            title.animate.scale(0.7).to_corner(UL),
            FadeOut(author)
        )

        # Definition
        definition_text = (
            "Es un algoritmo de <b>aprendizaje supervisado</b> que\n"
            "construye de forma <span fgcolor='#f39c12'>iterativa</span> un <b>modelo fuerte</b>\n"
            "mediante la combinación de múltiples\n"
            "<span fgcolor='#e74c3c'>estimadores débiles</span> (generalmente árboles de\n"
            "decisión de baja profundidad).\n\n"
            "Su objetivo es minimizar una función de pérdida\n"
            "global, donde cada <span fgcolor='#f1c40f'>nuevo modelo</span> se entrena\n"
            "sobre los <span fgcolor='#e74c3c'>residuos (errores)</span> del modelo\n"
            "acumulado hasta el momento."
        )
        
        # Usamos MarkupText sin justify para que las líneas se centren naturalmente
        definition = MarkupText(definition_text, font_size=32, line_spacing=1.5).move_to(ORIGIN)
        self.play(FadeIn(definition))
        self.wait(4)
        self.play(FadeOut(definition))

        # "In simple words"
        simple_title = Text("En palabras sencillas...", font_size=48, color=BLUE)
        self.play(Write(simple_title))
        self.wait(1) 
        # Importante: Quitamos el título completamente antes de seguir
        self.play(FadeOut(simple_title))
        
        analogy_text = (
            "Es una técnica de <b>aprendizaje en equipo</b> donde\n"
            "muchos modelos pequeños y simples (llamados\n"
            "<i>'árboles de decisión'</i>) trabajan juntos para\n"
            "resolver un problema difícil.\n\n"
            "Lo especial es que no trabajan todos a la vez,\n"
            "sino en <span fgcolor='#f39c12'>orden</span>: cada <span fgcolor='#f1c40f'>nuevo árbol</span> que creamos\n"
            "tiene la misión específica de corregir los\n"
            "<span fgcolor='#e74c3c'>errores</span> que cometió el árbol anterior."
        )
    
        # Asegúrate de usar MarkupText en lugar de Text y aumentamos un poco la fuente
        analogy = MarkupText(analogy_text, font_size=32, line_spacing=1.5).move_to(ORIGIN)
        
        self.play(FadeIn(analogy))
        self.wait(4)
        
        # Cleanup for next section (title and analogy fade out)
        self.play(FadeOut(analogy), FadeOut(title))

    def show_refinement(self):
        # Concept Title
        title = Text("1. Refinamiento Sucesivo", font_size=40, color=GREEN).to_edge(UP)
        self.play(Write(title))

        # Explanation (from presetnacion.md)
        explanation_text = (
            "Los árboles se crean <span fgcolor='#f39c12'>uno por uno</span>.\n"
            "Cuando uno se <span fgcolor='#e74c3c'>equivoca</span>, el siguiente\n"
            "le presta mucha más atención a ese <span fgcolor='#e74c3c'>error</span>\n"
            "específico para intentar <span fgcolor='#2ecc71'>corregirlo</span>."
        )
        explanation = MarkupText(explanation_text, font_size=36, line_spacing=1.5).move_to(ORIGIN)
        self.play(FadeIn(explanation))
        self.wait(3)
        self.play(FadeOut(explanation))

        # ── Setup Layout ──
        # Left: Stack of Trees
        # Right: Function Plot
        
        # Axis for the plot
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": GRAY},
        ).to_edge(RIGHT, buff=1)
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Target Function (Sine wave)
        target_func = lambda x: np.sin(x)
        target_graph = axes.plot(target_func, color=GREEN, stroke_width=4)
        target_label = Text("Objetivo", font_size=20, color=GREEN).next_to(target_graph, UP)

        self.play(Create(axes), Write(axes_labels))
        self.play(Create(target_graph), Write(target_label))
        
        # ── Iteration Loop ──
        # 12 trees in a 3-column grid on the left, faster pacing
        
        iterations = 12
        current_pred_graph = None
        
        # Simplified "weak learner" predictions for visualization
        # Each adds a bit more detail to approximate sine
        def get_learner_func(i):
            if i == 0: return lambda x: 0.5 if x < 3 else -0.5
            if i == 1: return lambda x: 0.5 if (x > 6 and x < 9) else 0
            if i == 2: return lambda x: 0.6 if (x > 0 and x < 1.5) else -0.2
            if i == 3: return lambda x: -0.6 if (x > 3 and x < 4.5) else 0
            if i == 4: return lambda x: 0.3 if (x > 4.5 and x < 6.5) else 0
            if i == 5: return lambda x: -0.3 if (x > 9 and x < 10) else 0.1
            if i == 6: return lambda x: 0.15 * np.sin(x * 2)
            if i == 7: return lambda x: 0.1 * np.sin(x * 3)
            if i == 8: return lambda x: 0.15 if (x > 1.5 and x < 3) else -0.1
            if i == 9: return lambda x: 0.1 * np.cos(x * 1.5)
            if i == 10: return lambda x: -0.15 if (x > 7 and x < 8.5) else 0.05
            if i == 11: return lambda x: 0.08 * np.sin(x * 4)
            return lambda x: 0

        # Accumulate predictions
        accumulated_func = lambda x: 0
        
        trees_group = VGroup()
        colors = [BLUE, TEAL, GOLD, RED_C, PURPLE, MAROON, YELLOW, PINK, GREEN_C, GRAY_B, ORANGE, WHITE]
        
        # Grid config: 3 columns, 4 rows
        grid_cols = 3
        tree_scale = 0.5
        grid_start = UP * 1.6 + LEFT * 5.5  # top-left anchor
        col_spacing = 1.7
        row_spacing = 1.5

        for i in range(iterations):
            # 1. Create Tree
            color = colors[i % len(colors)]
            tree_group = self.create_model_box(f"Árbol {i+1}", color=color)
            tree_group.scale(tree_scale)
            
            # Position in 2-column grid
            row = i // grid_cols
            col = i % grid_cols
            tree_group.move_to(grid_start + RIGHT * col * col_spacing + DOWN * row * row_spacing)
            
            trees_group.add(tree_group)
            
            # Speed: first 3 trees get full animation, rest are faster
            if i < 3:
                # Full animation: tree → arrow → graph update → residuals
                self.play(FadeIn(tree_group, shift=RIGHT), run_time=0.6)
                
                arrow = Arrow(
                    tree_group.get_right(), axes.c2p(5, 0),
                    color=color, stroke_width=2, max_tip_length_to_length_ratio=0.1
                )
                self.play(GrowArrow(arrow), run_time=0.5)
                
                learner = get_learner_func(i)
                prev_func = accumulated_func
                accumulated_func = lambda x, p=prev_func, l=learner: p(x) + l(x)
                new_graph = axes.plot(accumulated_func, color=WHITE, stroke_width=3)
                
                if current_pred_graph:
                    self.play(Transform(current_pred_graph, new_graph), FadeOut(arrow), run_time=1)
                else:
                    current_pred_graph = new_graph
                    self.play(Create(current_pred_graph), FadeOut(arrow), run_time=1)
                
                # Show residuals
                residuals = VGroup()
                for x_val in np.arange(0.5, 9.5, 0.5):
                    p1 = axes.c2p(x_val, accumulated_func(x_val))
                    p2 = axes.c2p(x_val, target_func(x_val))
                    residuals.add(Line(p1, p2, color=RED, stroke_opacity=0.6, stroke_width=2))
                self.play(Create(residuals), run_time=0.4)
                self.wait(0.4)
                self.play(FadeOut(residuals), run_time=0.2)
            else:
                # Fast animation: tree appears + graph updates simultaneously
                learner = get_learner_func(i)
                prev_func = accumulated_func
                accumulated_func = lambda x, p=prev_func, l=learner: p(x) + l(x)
                new_graph = axes.plot(accumulated_func, color=WHITE, stroke_width=3)
                
                self.play(
                    FadeIn(tree_group, shift=RIGHT),
                    Transform(current_pred_graph, new_graph),
                    run_time=0.7
                )
                self.wait(0.2)

        # Final pause
        result_text = Text("¡Ajuste Mejorado!", font_size=24, color=WHITE).next_to(axes, DOWN)
        self.play(Write(result_text))
        self.wait(2)
        
        self.play(FadeOut(trees_group), FadeOut(axes), FadeOut(current_pred_graph), 
                  FadeOut(target_graph), FadeOut(title), FadeOut(axes_labels), FadeOut(target_label), FadeOut(result_text))

    def show_learning_rate(self):
        # Concept Title
        title = Text("2. Control de Velocidad (Learning Rate)", font_size=40, color=ORANGE).to_edge(UP)
        self.play(Write(title))

        # Explanation
        explanation_text = (
            "Avanzamos con <span fgcolor='#f39c12'>pasos pequeños (eta)</span>\n"
            "evita correcciones drásticas por <span fgcolor='#e74c3c'>ruido</span>."
        )
        explanation = MarkupText(explanation_text, font_size=40, line_spacing=1.5).move_to(ORIGIN)
        self.play(FadeIn(explanation))
        self.wait(3)
        self.play(FadeOut(explanation))

        # Formula
        # Separamos componentes para poder manipularlos individualmente
        formula = MathTex(
            r"F_{m}(x)", r"=", r"F_{m-1}(x)", r"+", r"\eta", r"\cdot", r"h_{m}(x)",
            font_size=54
        ).move_to(ORIGIN)
        
        # Colores
        formula[0].set_color(WHITE)
        formula[2].set_color(GRAY)
        formula[4].set_color(ORANGE) # eta
        formula[6].set_color(YELLOW) # hm
        
        self.play(Write(formula))
        self.wait(1)
        
        # Mover formula arriba para explicar abajo
        self.play(formula.animate.shift(UP * 1.5))

        # Detalle de cada término con estilo LaTeX
        explanations = [
            Tex(r"$F_{m}(x)$: El nuevo resultado", font_size=45).set_color(WHITE),
            Tex(r"$F_{m-1}(x)$: Lo que ya sabíamos", font_size=45).set_color(GRAY),
            Tex(r"$h_{m}(x)$: La nueva sugerencia", font_size=45).set_color(YELLOW),
            Tex(r"$\eta$: Learning Rate (amortiguador)", font_size=45).set_color(ORANGE)
        ]
        
        # Grupo para organizar posición
        details_group = VGroup(*explanations).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(formula, DOWN, buff=0.5)

        # Mapeo de términos en la fórmula (índices del MathTex)
        # formula[0] -> Fm(x)
        # formula[2] -> Fm-1(x)
        # formula[6] -> hm(x)
        # formula[4] -> eta
        targets = [formula[0], formula[2], formula[6], formula[4]]

        # Animación secuencial: Sale texto -> Señala fórmula
        for expl, target in zip(explanations, targets):
            self.play(FadeIn(expl))
            self.play(Indicate(target, scale_factor=1.5, color=target.get_color()))
            self.wait(1)

        self.wait(2)
        
        # Limpieza
        self.play(FadeOut(formula), FadeOut(details_group))
        
        # ═══════════════════════════════════════
        # INTERACTIVE DIAGRAM: Learning Rate Comparison
        # ═══════════════════════════════════════

        # ── Persistent Formula at Bottom ──
        lr_formula = MathTex(
            r"F_{m}(x)", r"=", r"F_{m-1}(x)", r"+",
            r"\eta", r"\cdot", r"h_{m}(x)",
            font_size=42
        ).to_edge(DOWN, buff=0.5)
        lr_formula[0].set_color(WHITE)
        lr_formula[2].set_color(GRAY)
        lr_formula[4].set_color(ORANGE)
        lr_formula[6].set_color(YELLOW)
        self.play(FadeIn(lr_formula))

        # ── Target Line (goal = 1.0) ──
        target_height = 3.0  # visual units

        # ════════════════════════════
        # SCENARIO A: High LR (eta=1.0)
        # ════════════════════════════
        scenario_a_label = Text("η = 1.0 (Alto)", font_size=28, color=RED_C).move_to(UP * 2.5 + LEFT * 4)
        self.play(FadeIn(scenario_a_label))

        # Progress bar frame (left side)
        bar_frame_a = Rectangle(
            width=1.2, height=target_height,
            stroke_color=WHITE, stroke_width=1.5, fill_opacity=0
        ).move_to(LEFT * 4 + DOWN * 0.2)
        target_line_a = DashedLine(
            bar_frame_a.get_corner(UL) + LEFT * 0.5,
            bar_frame_a.get_corner(UR) + RIGHT * 0.5,
            color=GREEN, stroke_width=2
        )
        target_text_a = Text("Meta", font_size=16, color=GREEN).next_to(target_line_a, RIGHT, buff=0.15)

        self.play(Create(bar_frame_a), Create(target_line_a), FadeIn(target_text_a))

        # Tree 1 with eta=1.0 → jumps to 1.0 (perfect but aggressive)
        tree_a1 = self.create_model_box("h₁", RED_C).scale(0.4)
        tree_a1.next_to(bar_frame_a, LEFT, buff=0.8).shift(UP * 1)

        self.play(FadeIn(tree_a1, shift=RIGHT), run_time=0.5)
        # Dynamic formula: eta grows BIG and turns RED for high LR
        self.play(
            lr_formula[4].animate.scale(1.5).set_color(RED),
            Indicate(lr_formula[4], scale_factor=1.5, color=RED),
            run_time=0.8
        )

        # Bar fills to 100% immediately
        bar_fill_a = Rectangle(
            width=1.1, height=target_height,
            stroke_width=0, fill_color=RED_C, fill_opacity=0.5
        ).align_to(bar_frame_a, DOWN).align_to(bar_frame_a, LEFT).shift(RIGHT * 0.05)
        self.play(GrowFromEdge(bar_fill_a, DOWN), run_time=0.8)

        # Tree 2 with eta=1.0 → overshoots!
        tree_a2 = self.create_model_box("h₂", RED_C).scale(0.4)
        tree_a2.next_to(tree_a1, DOWN, buff=0.15)
        self.play(FadeIn(tree_a2, shift=RIGHT), run_time=0.5)

        # Wiggle/shake the bar before overshoot (noise effect)
        self.play(Wiggle(bar_fill_a, scale_value=1.1, rotation_angle=0.03 * TAU), run_time=0.8)

        # Bar overshoots to 1.3 (grows past the frame)
        overshoot_bar = Rectangle(
            width=1.1, height=target_height * 1.3,
            stroke_width=0, fill_color=RED_C, fill_opacity=0.5
        ).align_to(bar_frame_a, DOWN).align_to(bar_frame_a, LEFT).shift(RIGHT * 0.05)
        self.play(Transform(bar_fill_a, overshoot_bar), run_time=0.6)

        # Flash the target line RED to signal failure
        self.play(Flash(target_line_a.get_center(), color=RED, flash_radius=0.5, num_lines=12))

        overshoot_text = Text("¡Excede el objetivo!", font_size=20, color=YELLOW).next_to(bar_frame_a, UP, buff=0.1)
        self.play(Write(overshoot_text))
        self.wait(1)

        # ════════════════════════════
        # SCENARIO B: Low LR (eta=0.1)
        # ════════════════════════════
        # Restore eta in formula to small/green for Scenario B
        self.play(lr_formula[4].animate.scale(1/1.5).set_color(GREEN), run_time=0.5)

        scenario_b_label = Text("η = 0.1 (Bajo)", font_size=28, color=GREEN).move_to(UP * 2.5 + RIGHT * 2.5)
        self.play(FadeIn(scenario_b_label))

        # Progress bar frame (right side)
        bar_frame_b = Rectangle(
            width=1.2, height=target_height,
            stroke_color=WHITE, stroke_width=1.5, fill_opacity=0
        ).move_to(RIGHT * 2.5 + DOWN * 0.2)
        target_line_b = DashedLine(
            bar_frame_b.get_corner(UL) + LEFT * 0.5,
            bar_frame_b.get_corner(UR) + RIGHT * 0.5,
            color=GREEN, stroke_width=2
        )
        target_text_b = Text("Meta", font_size=16, color=GREEN).next_to(target_line_b, LEFT, buff=0.15)

        self.play(Create(bar_frame_b), Create(target_line_b), FadeIn(target_text_b))

        # 10 trees with eta=0.1 → controlled growth
        trees_b = VGroup()
        tree_colors_b = [BLUE, TEAL, GOLD, PURPLE, MAROON, YELLOW, PINK, GREEN_C, GRAY_B, ORANGE]

        for step in range(10):
            # Create small tree
            tree_b = self.create_model_box(f"h{step+1}", tree_colors_b[step]).scale(0.3)

            # Position in 2-column grid next to the bar
            row = step // 2
            col = step % 2
            tree_b.move_to(RIGHT * 4.2 + UP * 1.5 + DOWN * row * 0.8 + RIGHT * col * 1.2)
            trees_b.add(tree_b)

            # Fill height for this step
            fill_height = target_height * (step + 1) / 10
            new_fill = Rectangle(
                width=1.1, height=fill_height,
                stroke_width=0, fill_color=GREEN, fill_opacity=0.4
            ).align_to(bar_frame_b, DOWN).align_to(bar_frame_b, LEFT).shift(RIGHT * 0.05)

            if step < 3:
                # Full animation for first 3 — synchronized formula + bar
                self.play(FadeIn(tree_b, shift=LEFT), run_time=0.4)
                if step == 0:
                    bar_fill_b = new_fill
                    self.play(
                        Indicate(lr_formula[4], scale_factor=1.2, color=GREEN),
                        Indicate(lr_formula[6], scale_factor=1.3, color=tree_colors_b[step]),
                        GrowFromEdge(bar_fill_b, DOWN),
                        run_time=0.5
                    )
                else:
                    self.play(
                        Indicate(lr_formula[4], scale_factor=1.2, color=GREEN),
                        Indicate(lr_formula[6], scale_factor=1.3, color=tree_colors_b[step]),
                        Transform(bar_fill_b, new_fill),
                        run_time=0.5
                    )
            else:
                # Fast animation — tree + bar simultaneously
                if step == 0:
                    bar_fill_b = new_fill
                    self.play(FadeIn(tree_b), GrowFromEdge(bar_fill_b, DOWN), run_time=0.3)
                else:
                    self.play(FadeIn(tree_b), Transform(bar_fill_b, new_fill), run_time=0.3)

        # Convergence celebration — flash the target line gold
        self.play(
            Flash(target_line_b.get_center(), color=GOLD, flash_radius=0.6, num_lines=16),
            Indicate(target_line_b, color=GOLD, scale_factor=1.2),
            run_time=0.8
        )

        # Success text with Write animation
        success_text = Text("✓ Preciso y Estable", font_size=20, color=GREEN).next_to(bar_frame_b, UP, buff=0.1)
        self.play(Write(success_text))
        self.wait(2)

        # ── Cleanup ──
        all_lr_elements = VGroup(
            scenario_a_label, bar_frame_a, target_line_a, target_text_a,
            tree_a1, tree_a2, bar_fill_a, overshoot_text,
            scenario_b_label, bar_frame_b, target_line_b, target_text_b,
            trees_b, bar_fill_b, success_text, lr_formula
        )
        self.play(FadeOut(all_lr_elements), FadeOut(title))

    def show_regularization(self):
        # Concept Title
        title = Text("3. Simplicidad (Regularización)", font_size=40, color=PURPLE).to_edge(UP)
        self.play(Write(title))

        # Explanation
        explanation_text = (
            "<b>Árboles sencillos (débiles)</b>\n"
            "para evitar sobreajuste. La <span fgcolor='#f1c40f'>inteligencia</span>\n"
            "viene de la suma, no de uno solo."
        )
        explanation = MarkupText(explanation_text, font_size=40, line_spacing=1.5).move_to(ORIGIN)
        self.play(FadeIn(explanation))
        self.wait(3)
        self.play(FadeOut(explanation))

        # ═══════════════════════════════════════
        # ITERATIVE DIAGRAM: Regularization (Complexity)
        # ═══════════════════════════════════════

        # Target function (smooth sine)
        target_func = lambda x: np.sin(x)

        # ════════════════════════════════════
        # SCENARIO A: Complex Trees → Overfitting
        # ════════════════════════════════════
        scenario_a_label = Text("Árboles Complejos → Memoriza Ruido", font_size=26, color=RED_C).to_edge(UP).shift(DOWN * 0.8)
        self.play(FadeIn(scenario_a_label))

        axes_a = Axes(
            x_range=[0, 10, 1], y_range=[-2, 2, 1],
            x_length=6, y_length=4,
            axis_config={"color": GRAY},
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)
        axes_a_labels = axes_a.get_axis_labels(x_label="x", y_label="y")
        target_graph_a = axes_a.plot(target_func, color=GREEN, stroke_width=3)
        target_lbl_a = Text("Objetivo", font_size=16, color=GREEN).next_to(target_graph_a, UP, buff=0.1)

        self.play(Create(axes_a), Write(axes_a_labels))
        self.play(Create(target_graph_a), FadeIn(target_lbl_a))

        # Noisy learner functions (complex trees overfit noise)
        def noisy_learner(i):
            funcs = [
                lambda x: 0.5 if x < 3 else -0.5,
                lambda x: 0.5 if (x > 6 and x < 9) else 0,
                lambda x: 0.4 * np.sin(x * 3),
                lambda x: 0.3 * np.sin(x * 5),
                lambda x: 0.25 * np.sin(x * 8),
                lambda x: 0.2 * np.sin(x * 10),
                lambda x: 0.15 * np.cos(x * 7),
                lambda x: 0.2 * np.sin(x * 12),
                lambda x: 0.1 * np.cos(x * 15),
                lambda x: 0.15 * np.sin(x * 9),
                lambda x: 0.1 * np.sin(x * 18),
                lambda x: 0.08 * np.cos(x * 20),
                lambda x: 0.12 * np.sin(x * 14),
                lambda x: 0.1 * np.cos(x * 11),
                lambda x: 0.08 * np.sin(x * 22),
                lambda x: 0.06 * np.cos(x * 25),
            ]
            return funcs[i] if i < len(funcs) else (lambda x: 0)

        accumulated_a = lambda x: 0
        pred_graph_a = None
        trees_a = VGroup()

        # Grid config for complex trees: 4 columns, matching refinement style
        grid_cols_a = 4
        tree_scale_a = 0.55
        grid_start_a = UP * 1.6 + LEFT * 6.0  # top-left anchor
        col_spacing_a = 1.35
        row_spacing_a = 1.5

        for i in range(16):
            # Create deep tree visual (complex)
            deep_t = self._create_deep_tree(f"C{i+1}", RED_C).scale(tree_scale_a)
            col = i % grid_cols_a
            row = i // grid_cols_a
            deep_t.move_to(grid_start_a + RIGHT * col * col_spacing_a + DOWN * row * row_spacing_a)
            trees_a.add(deep_t)

            learner = noisy_learner(i)
            prev = accumulated_a
            accumulated_a = lambda x, p=prev, l=learner: p(x) + l(x)
            new_graph = axes_a.plot(accumulated_a, color=WHITE, stroke_width=2.5)

            if i < 3:
                self.play(FadeIn(deep_t, shift=RIGHT), run_time=0.4)
                if pred_graph_a:
                    self.play(Transform(pred_graph_a, new_graph), run_time=0.6)
                else:
                    pred_graph_a = new_graph
                    self.play(Create(pred_graph_a), run_time=0.6)
            else:
                # Fast: tree + graph update together
                if pred_graph_a:
                    self.play(FadeIn(deep_t, shift=RIGHT), Transform(pred_graph_a, new_graph), run_time=0.3)
                else:
                    pred_graph_a = new_graph
                    self.play(FadeIn(deep_t, shift=RIGHT), Create(pred_graph_a), run_time=0.3)

        # Overfitting label
        overfit_text = Text("¡Sobreajuste!", font_size=22, color=YELLOW).next_to(axes_a, DOWN, buff=0.2)
        self.play(Write(overfit_text), Wiggle(pred_graph_a, scale_value=1.05), run_time=1)
        self.wait(1.5)

        # Cleanup Scenario A
        all_a = VGroup(scenario_a_label, axes_a, axes_a_labels, target_graph_a, target_lbl_a,
                       trees_a, pred_graph_a, overfit_text)
        self.play(FadeOut(all_a), run_time=0.8)

        # ════════════════════════════════════
        # SCENARIO B: Simple Trees → Generalization
        # ════════════════════════════════════
        scenario_b_label = Text("Árboles Simples → Generaliza Mejor", font_size=26, color=GREEN).to_edge(UP).shift(DOWN * 0.8)
        self.play(FadeIn(scenario_b_label))

        axes_b = Axes(
            x_range=[0, 10, 1], y_range=[-2, 2, 1],
            x_length=6, y_length=4,
            axis_config={"color": GRAY},
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)
        axes_b_labels = axes_b.get_axis_labels(x_label="x", y_label="y")
        target_graph_b = axes_b.plot(target_func, color=GREEN, stroke_width=3)
        target_lbl_b = Text("Objetivo", font_size=16, color=GREEN).next_to(target_graph_b, UP, buff=0.1)

        self.play(Create(axes_b), Write(axes_b_labels))
        self.play(Create(target_graph_b), FadeIn(target_lbl_b))

        # Smooth learner functions (simple stumps generalize)
        def smooth_learner(i):
            funcs = [
                lambda x: 0.3 if x < 3 else -0.3,
                lambda x: 0.3 if (x > 6 and x < 9) else 0,
                lambda x: 0.2 if (x > 0 and x < 1.5) else -0.05,
                lambda x: -0.2 if (x > 3 and x < 4.5) else 0,
                lambda x: 0.1 * np.sin(x),
                lambda x: 0.15 if (x > 4.5 and x < 6) else 0,
                lambda x: -0.1 if (x > 9 and x < 10) else 0.05,
                lambda x: 0.08 * np.sin(x),
                lambda x: 0.1 if (x > 1.5 and x < 3) else -0.03,
                lambda x: -0.08 if (x > 7 and x < 8) else 0,
                lambda x: 0.05 * np.sin(x),
                lambda x: 0.03 * np.sin(x),
                lambda x: 0.06 if (x > 5 and x < 6.5) else -0.02,
                lambda x: -0.05 if (x > 8 and x < 9.5) else 0,
                lambda x: 0.04 * np.sin(x),
                lambda x: 0.02 * np.sin(x),
            ]
            return funcs[i] if i < len(funcs) else (lambda x: 0)

        accumulated_b = lambda x: 0
        pred_graph_b = None
        trees_b = VGroup()

        # Grid config for simple trees: 4 columns, matching refinement style
        grid_cols_b = 4
        tree_scale_b = 0.55
        grid_start_b = UP * 1.6 + LEFT * 6.0  # top-left anchor
        col_spacing_b = 1.35
        row_spacing_b = 1.5

        for i in range(16):
            stump = self.create_model_box(f"S{i+1}", GREEN).scale(tree_scale_b)
            col = i % grid_cols_b
            row = i // grid_cols_b
            stump.move_to(grid_start_b + RIGHT * col * col_spacing_b + DOWN * row * row_spacing_b)
            trees_b.add(stump)

            learner = smooth_learner(i)
            prev = accumulated_b
            accumulated_b = lambda x, p=prev, l=learner: p(x) + l(x)
            new_graph = axes_b.plot(accumulated_b, color=WHITE, stroke_width=2.5)

            if i < 3:
                self.play(FadeIn(stump, shift=RIGHT), run_time=0.4)
                if pred_graph_b:
                    self.play(Transform(pred_graph_b, new_graph), run_time=0.6)
                else:
                    pred_graph_b = new_graph
                    self.play(Create(pred_graph_b), run_time=0.6)
            else:
                if pred_graph_b:
                    self.play(FadeIn(stump, shift=RIGHT), Transform(pred_graph_b, new_graph), run_time=0.3)
                else:
                    pred_graph_b = new_graph
                    self.play(FadeIn(stump, shift=RIGHT), Create(pred_graph_b), run_time=0.3)

        # Success label
        success_text = Text("✓ Generaliza Correctamente", font_size=22, color=GREEN).next_to(axes_b, DOWN, buff=0.2)
        self.play(Write(success_text))
        self.wait(2)

        # Cleanup
        all_b = VGroup(scenario_b_label, axes_b, axes_b_labels, target_graph_b, target_lbl_b,
                       trees_b, pred_graph_b, success_text)
        self.play(FadeOut(all_b), FadeOut(title))

    def _create_deep_tree(self, label, color):
        """Create a visually complex/deep tree with 4 levels."""
        tree = VGroup()
        # Root
        root = Circle(radius=0.12, color=color, fill_opacity=1).move_to(ORIGIN)
        tree.add(root)
        # Level 1
        l1l = Circle(radius=0.1, color=color, fill_opacity=1).move_to(DOWN * 0.45 + LEFT * 0.5)
        l1r = Circle(radius=0.1, color=color, fill_opacity=1).move_to(DOWN * 0.45 + RIGHT * 0.5)
        tree.add(l1l, l1r, Line(root.get_bottom(), l1l.get_top(), color=color, stroke_width=1.5))
        tree.add(Line(root.get_bottom(), l1r.get_top(), color=color, stroke_width=1.5))
        # Level 2
        l2_nodes = []
        for parent, sign in [(l1l, -1), (l1l, 1), (l1r, -1), (l1r, 1)]:
            child = Circle(radius=0.07, color=color, fill_opacity=0.8).move_to(parent.get_center() + DOWN * 0.4 + RIGHT * sign * 0.25)
            l2_nodes.append(child)
            tree.add(child, Line(parent.get_bottom(), child.get_top(), color=color, stroke_width=1))
        # Level 3 (extra leaves for complexity)
        for j, parent in enumerate(l2_nodes):
            c1 = Circle(radius=0.04, color=color, fill_opacity=0.6).move_to(parent.get_center() + DOWN * 0.3 + LEFT * 0.12)
            c2 = Circle(radius=0.04, color=color, fill_opacity=0.6).move_to(parent.get_center() + DOWN * 0.3 + RIGHT * 0.12)
            tree.add(c1, c2, Line(parent.get_bottom(), c1.get_top(), color=color, stroke_width=0.8))
            tree.add(Line(parent.get_bottom(), c2.get_top(), color=color, stroke_width=0.8))
        # Label
        lbl = Text(label, font_size=14, color=color).next_to(tree, DOWN, buff=0.05)
        tree.add(lbl)
        return tree

    # ── Real World Applications Methods ──

    def show_real_world_intro(self):
        # Paragraph separa las líneas por comas en lugar de \n
        title = Paragraph(
            "¿En dónde se utiliza el Boosting", 
            "en la vida real?", 
            alignment="center", # Debe ir entre comillas
            font_size=45,
            line_spacing=1.2
        ).move_to(ORIGIN) # Esto lo centra en la pantalla

        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))

    def show_fraud_detection(self):
        # 1. Título principal (Bien arriba)
        title = Text("1. Detección de Fraude Bancario", font_size=38, color=RED).to_edge(UP)
        self.play(Write(title))

        # --- SECCIÓN 1: HISTORIAL NORMAL ---
        y_normal = 1.8 # Posición base línea 1
        
        normal_label = Text("Historial Habitual", font_size=20, color=GREEN_A).move_to([-4, y_normal + 0.8, 0])
        line_normal = Line(LEFT * 5, RIGHT * 5, color=GRAY).move_to([0, y_normal, 0])
        
        history = VGroup(
            self.create_transaction("Café", "$5", GREEN, -4, y_normal),
            self.create_transaction("Súper", "$45", GREEN, -1.5, y_normal),
            self.create_transaction("Cine", "$12", GREEN, 1, y_normal),
            self.create_transaction("Gas", "$30", GREEN, 3.5, y_normal)
        )

        self.play(FadeIn(normal_label), Create(line_normal))
        self.play(LaggedStart(*[FadeIn(obj) for obj in history], lag_ratio=0.15))

        # --- SECCIÓN 2: ACTIVIDAD SOSPECHOSA (Más abajo para evitar choques) ---
        y_fraud = -0.8 # Bajamos la línea de fraude
        
        fraud_label = Text("Nuevas Transacciones", font_size=20, color=RED_A).move_to([-4, y_fraud + 1.2, 0])
        line_fraud = Line(LEFT * 5, RIGHT * 5, color=GRAY).move_to([0, y_fraud, 0])
        
        # Añadimos más casos erróneos
        new_txns = VGroup(
            self.create_transaction("Pan", "$2", GREEN, -4, y_fraud),
            self.create_transaction("Reloj Lujo", "$5,000", RED, -1.5, y_fraud),
            self.create_transaction("Cripto", "$8,500", RED, 1, y_fraud),
            self.create_transaction("Giro Ext.", "$2,000", RED, 3.5, y_fraud)
        )
        
        # Rectángulos de alerta para los 3 fraudes
        alerts = VGroup(*[
            SurroundingRectangle(new_txns[i], color=RED, buff=0.1) 
            for i in range(1, 4)
        ])
        
        # AJUSTE: Movemos el warning más a la derecha
        warning = Text("¡INCONSISTENCIAS DETECTADAS!", color=RED, font_size=18, weight=BOLD).move_to([2, y_fraud + 1.0, 0])

        self.play(FadeIn(fraud_label), Create(line_fraud))
        self.play(FadeIn(new_txns[0])) # El caso normal
        self.wait(0.5)
        
        # Aparecen los fraudes
        self.play(LaggedStart(*[FadeIn(new_txns[i]) for i in range(1, 4)], lag_ratio=0.3))
        self.play(Create(alerts), Write(warning))
        self.play(Indicate(alerts, color=RED))
        self.wait(1)

        # --- SECCIÓN 3: DECISIÓN FINAL (Más abajo para evitar solapamiento) ---
        decision_text = Text("Boosting: Riesgo Crítico -> CUENTA BLOQUEADA", font_size=24, color=WHITE)
        decision_box = RoundedRectangle(
            corner_radius=0.1, 
            width=decision_text.width + 0.6, 
            height=decision_text.height + 0.4, 
            fill_color=RED_E, # Rojo oscuro sólido
            fill_opacity=1, 
            stroke_color=WHITE
        ).move_to(DOWN * 2.5)  # AJUSTE: Bajado de 3.3 a 3.5
        
        decision_group = VGroup(decision_box, decision_text).move_to(DOWN * 3.5)  # AJUSTE: Bajado de 3.3 a 3.5

        self.play(FadeIn(decision_group, shift=UP))
        self.wait(5)

        # Salida limpia
        self.play(FadeOut(title, normal_label, line_normal, history, fraud_label, line_fraud, new_txns, alerts, warning, decision_group))

    # Función auxiliar (Asegúrate de copiarla tal cual dentro de la clase)
    def create_transaction(self, label, amount, color, x, y):
        dot = Dot(color=color).scale(1.2).move_to([x, y, 0])
        txt_label = Text(label, font_size=16).next_to(dot, UP, buff=0.15)
        txt_amount = Text(amount, font_size=16, color=color).next_to(dot, DOWN, buff=0.15)
        return VGroup(dot, txt_label, txt_amount)

    def show_recommendation_systems(self):
        # 1. Título
        title = Text("2. Sistemas de Recomendación", font_size=38, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        # Logo Netflix debajo del título principal
        netflix_logo = Text("NETFLIX", color=RED, font="Impact", weight=BOLD).scale(0.8)
        netflix_logo.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(netflix_logo, shift=UP))
        self.wait(0.5)

        # --- FUNCIÓN PARA CREAR PERFIL DE USUARIO ---
        def create_user_profile(name, initial, movies, position):
            user_box = RoundedRectangle(width=3.2, height=4.2, corner_radius=0.2, color=RED_E, fill_opacity=0.15, stroke_width=2)
            user_box.move_to(position)
            
            user_icon = VGroup(
                Circle(radius=0.45, color=WHITE, fill_opacity=1, fill_color=BLUE_D),
                Text(initial, font_size=28, color=WHITE)
            ).move_to(user_box.get_top() + DOWN * 0.7)
            
            user_name = Text(f"Usuario: {name}", font_size=18, weight=BOLD).next_to(user_icon, DOWN, buff=0.25)
            history_title = Text("Visto recientemente:", font_size=14, color=GRAY_A).next_to(user_name, DOWN, buff=0.35)
            
            visto = VGroup(*[
                Text(f"• {movie}", font_size=13) for movie in movies
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(history_title, DOWN, buff=0.25)
            
            return VGroup(user_box, user_icon, user_name, history_title, visto)

        # --- FUNCIÓN PARA CREAR TARJETA DE PELÍCULA ---
        def create_movie_card(movie_name, match_score, pos_y, emoji="🎬"):
            card = RoundedRectangle(width=5.5, height=0.85, corner_radius=0.15, color=GRAY_D, fill_opacity=0.3, stroke_width=2)
            card.move_to([2.8, pos_y, 0])
            name = Text(f"{emoji} {movie_name}", font_size=17).move_to(card.get_left() + RIGHT * 1.8)
            score = Text(f"{match_score}% match", font_size=15, color=GREEN).move_to(card.get_right() + LEFT * 1.2)
            return VGroup(card, name, score)

        # ========== USUARIO 1: JUAN (Fan de Acción) ==========
        perfil_juan = create_user_profile(
            "Juan", "J",
            ["John Wick (Acción)", "Mad Max (Acción)", "Inception (Sci-Fi)", "The Batman (Acción)"],
            LEFT * 4 + DOWN * 0.3
        )
        
        self.play(FadeIn(perfil_juan, shift=RIGHT))
        self.wait(0.5)

        cand_title = Text("Porque viste Acción...", font_size=20, color=RED_A).move_to(RIGHT * 2.8 + UP * 2)
        self.play(Write(cand_title))

        # Candidatos para Juan
        c1 = create_movie_card("Shrek (Comedia)", 15, 0.8, "😂")
        c2 = create_movie_card("The Whale (Drama)", 42, -0.1, "😢")
        c3 = create_movie_card("Top Gun (Acción)", 98, -1.0, "✈️")

        self.play(LaggedStart(FadeIn(c1), FadeIn(c2), FadeIn(c3), lag_ratio=0.25))
        
        # Boosting calculando
        arrow = Arrow(start=perfil_juan[0].get_right(), end=c3.get_left(), color=YELLOW, buff=0.15, stroke_width=6)
        boosting_label = Text("Boosting calculando...", font_size=16, color=YELLOW, slant=ITALIC).next_to(arrow, UP, buff=0.1)
        
        self.play(GrowArrow(arrow), Write(boosting_label))
        self.wait(0.8)

        # Resultado
        rect_win = SurroundingRectangle(c3, color=RED, buff=0.08, stroke_width=4)
        self.play(c1.animate.set_opacity(0.3), c2.animate.set_opacity(0.3), Create(rect_win))
        self.play(Indicate(c3, color=RED, scale_factor=1.08))
        self.wait(1.5)

        # Limpiar para siguiente usuario
        self.play(FadeOut(perfil_juan, cand_title, c1, c2, c3, arrow, boosting_label, rect_win))
        
        # ========== USUARIO 2: MARÍA (Fan de Drama) ==========
        perfil_maria = create_user_profile(
            "María", "M",
            ["The Crown (Drama)", "Breaking Bad (Drama)", "Succession (Drama)", "The Queen's Gambit"],
            LEFT * 4 + DOWN * 0.3
        )
        
        self.play(FadeIn(perfil_maria, shift=RIGHT))
        
        cand_title2 = Text("Porque viste Drama...", font_size=20, color=PURPLE_A).move_to(RIGHT * 2.8 + UP * 2)
        self.play(Write(cand_title2))

        # Candidatos para María
        m1 = create_movie_card("Fast & Furious (Acción)", 22, 0.8, "🚗")
        m2 = create_movie_card("The Godfather (Drama)", 95, -0.1, "🎭")
        m3 = create_movie_card("Mr. Bean (Comedia)", 18, -1.0, "😂")

        self.play(LaggedStart(FadeIn(m1), FadeIn(m2), FadeIn(m3), lag_ratio=0.25))
        
        arrow2 = Arrow(start=perfil_maria[0].get_right(), end=m2.get_left(), color=YELLOW, buff=0.15, stroke_width=6)
        boosting_label2 = Text("Boosting calculando...", font_size=16, color=YELLOW, slant=ITALIC).next_to(arrow2, UP, buff=0.1)
        
        self.play(GrowArrow(arrow2), Write(boosting_label2))
        self.wait(0.8)

        rect_win2 = SurroundingRectangle(m2, color=PURPLE, buff=0.08, stroke_width=4)
        self.play(m1.animate.set_opacity(0.3), m3.animate.set_opacity(0.3), Create(rect_win2))
        self.play(Indicate(m2, color=PURPLE, scale_factor=1.08))
        self.wait(1.5)

        # Limpiar
        self.play(FadeOut(perfil_maria, cand_title2, m1, m2, m3, arrow2, boosting_label2, rect_win2))

        # ========== USUARIO 3: CARLOS (Diverso) ==========
        perfil_carlos = create_user_profile(
            "Carlos", "C",
            ["Stranger Things (Sci-Fi)", "The Office (Comedia)", "Planet Earth (Documental)", "Avatar (Fantasia)"],
            LEFT * 4 + DOWN * 0.3
        )
        
        self.play(FadeIn(perfil_carlos, shift=RIGHT))
        
        cand_title3 = Text("Perfil diverso detectado...", font_size=20, color=TEAL_A).move_to(RIGHT * 2.8 + UP * 2)
        self.play(Write(cand_title3))

        # Candidatos para Carlos
        k1 = create_movie_card("Black Mirror (Sci-Fi)", 87, 0.8, "📺")
        k2 = create_movie_card("Parks & Rec (Comedia)", 79, -0.1, "😄")
        k3 = create_movie_card("Our Planet (Documental)", 85, -1.0, "🌍")

        self.play(LaggedStart(FadeIn(k1), FadeIn(k2), FadeIn(k3), lag_ratio=0.25))
        
        # Boosting analiza los 3
        arrow3 = Arrow(start=perfil_carlos[0].get_right(), end=k1.get_left() + UP*0.5, color=YELLOW, buff=0.15, stroke_width=6)
        boosting_label3 = Text("Analizando preferencias...", font_size=16, color=YELLOW, slant=ITALIC).next_to(arrow3, UP, buff=0.1)
        
        self.play(GrowArrow(arrow3), Write(boosting_label3))
        self.wait(0.8)

        # Todos tienen buen match
        rect_multiple = VGroup(
            SurroundingRectangle(k1, color=TEAL, buff=0.08, stroke_width=3),
            SurroundingRectangle(k2, color=TEAL, buff=0.08, stroke_width=3),
            SurroundingRectangle(k3, color=TEAL, buff=0.08, stroke_width=3)
        )
        
        self.play(Create(rect_multiple))
        self.play(Indicate(VGroup(k1, k2, k3), color=TEAL))
        self.wait(1.5)

        # Mensaje final
        explicacion = Text(
            "Boosting adapta recomendaciones según historial y preferencias únicas", 
            font_size=16, color=WHITE
        ).to_edge(DOWN, buff=0.4)
        
        self.play(Write(explicacion))
        self.wait(3)

        # Salida final (ahora incluye netflix_logo)
        self.play(FadeOut(
            title, netflix_logo, perfil_carlos, cand_title3, 
            k1, k2, k3, arrow3, boosting_label3, rect_multiple, explicacion
        ))

    def show_credit_risk(self):
        # 1. Título
        title = Text("3. Evaluación de Riesgo Crediticio", font_size=38, color=GREEN).to_edge(UP)
        self.play(Write(title))

        # --- PERFIL DEL CLIENTE (Izquierda) ---
        # Ajustamos posición para evitar solapamientos
        perfil_box = RoundedRectangle(width=3.5, height=4.2, corner_radius=0.2, color=GRAY_D, fill_opacity=0.2)
        perfil_box.to_edge(LEFT, buff=0.8).shift(UP * 0.3)
        
        perfil_header = Rectangle(width=3.5, height=0.7, color=GREEN_E, fill_opacity=1).move_to(perfil_box.get_top() + DOWN*0.35)
        header_txt = Text("CLIENTE: ID-402", font_size=20, color=WHITE).move_to(perfil_header)
        
        datos = VGroup(
            Text("• Salario: $3,500", font_size=18),
            Text("• Deudas: $1,200", font_size=18),
            Text("• Historial: Bueno", font_size=18),
            Text("• Edad: 28 años", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(perfil_header, DOWN, buff=0.4)
        
        # Ajuste manual para asegurar que esté dentro de la caja
        datos.set_x(perfil_box.get_left()[0] + 0.4 + datos.width/2) # Alinear a la izquierda con margen
        
        perfil = VGroup(perfil_box, perfil_header, header_txt, datos)
        self.play(FadeIn(perfil, shift=RIGHT))

        # --- BARRA DE SCORE (Abajo - Central) ---
        # Posición más baja para separar del perfil y árboles
        # Hacemos la barra MÁS DELGADA (height=0.4) y la movemos ligeramente
        bar_y = -3.2 
        bar_bg = RoundedRectangle(width=8.5, height=0.4, corner_radius=0.1, color=GRAY_C, fill_opacity=0.2).move_to(DOWN * 3.3)
        bar_label = Text("Credit Score (Probabilidad de Pago)", font_size=18).next_to(bar_bg, UP, buff=0.15)
        
        # Marcadores de la barra
        low_txt = Text("Bajo", font_size=16, color=RED).next_to(bar_bg, LEFT, buff=0.2)
        high_txt = Text("Alto", font_size=16, color=GREEN).next_to(bar_bg, RIGHT, buff=0.2)
        
        # El "Relleno" de la barra (empezamos en 0), explícitamente alineado
        # Height ajustado a 0.3 para encajar en la barra de 0.4
        bar_fill = Rectangle(width=0.01, height=0.3, color=GREEN, fill_opacity=0.9, stroke_width=0)
        # Alineación explícita para evitar glitches
        bar_fill.move_to(bar_bg.get_left() + RIGHT*0.05, aligned_edge=LEFT)
        
        self.play(Create(bar_bg), Write(bar_label), FadeIn(low_txt), FadeIn(high_txt), Create(bar_fill))

        # --- DECISIONES DEL BOOSTING (Derecha - Secuencial) ---
        tree_x = 3.5
        
        def create_decision_box(txt, val, color_val, pos_y):
            box = RoundedRectangle(width=5.0, height=0.9, corner_radius=0.15, color=GRAY_B)
            box.move_to([tree_x, pos_y, 0])
            t = Text(txt, font_size=18).move_to(box.get_left() + RIGHT*1.8)
            v = Text(val, font_size=24, color=color_val, weight=BOLD).move_to(box.get_right() + LEFT*0.7)
            return VGroup(box, t, v)

        # Árbol 1: Analiza Salario
        t1 = create_decision_box("Árbol 1: Salario Alto", "+50%", GREEN, 1.5)
        self.play(FadeIn(t1, shift=LEFT))
        # Animamos la barra creciendo al 50%
        # Usamos update_from_func o transform stretch para evitar problemas de alineación
        self.play(bar_fill.animate.stretch_to_fit_width(4.2).align_to(bar_bg, LEFT).shift(RIGHT*0.05), run_time=1)
        
        # Árbol 2: Analiza Deuda
        t2 = create_decision_box("Árbol 2: Deuda Existente", "-20%", RED, 0.3)
        self.play(FadeIn(t2, shift=LEFT))
        # Retrocede el score
        self.play(bar_fill.animate.stretch_to_fit_width(2.5).align_to(bar_bg, LEFT).shift(RIGHT*0.05), run_time=1)

        # Árbol 3: Analiza Edad/Estabilidad
        t3 = create_decision_box("Árbol 3: Estabilidad Joven", "+40%", GREEN, -0.9)
        self.play(FadeIn(t3, shift=LEFT))
        # Sube al 70%
        self.play(bar_fill.animate.stretch_to_fit_width(6.0).align_to(bar_bg, LEFT).shift(RIGHT*0.05), run_time=1)

        # --- VEREDICTO FINAL ---
        # Ponemos el texto FINAL ARRIBA de la barra, SIN cuadro de fondo
        veredicto_txt = Text("PRÉSTAMO APROBADO (Score: 70/100)", font_size=24, weight=BOLD, color=WHITE)
        veredicto_txt.next_to(bar_label, UP, buff=0.3)
        
        self.play(Write(veredicto_txt))
        self.play(Indicate(veredicto_txt, color=GREEN))
        self.wait(4)

        # Salida
        self.play(FadeOut(title, perfil, t1, t2, t3, veredicto_txt, bar_bg, bar_fill, bar_label, low_txt, high_txt))

    def end(self):
        # Paragraph separa las líneas por comas en lugar de \n
        title = Paragraph(
            "Garacias por su atención", 
            alignment="center", # Debe ir entre comillas
            font_size=45,
            line_spacing=1.2
        ).move_to(ORIGIN) # Esto lo centra en la pantalla

        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))