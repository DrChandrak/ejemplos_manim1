from manim import *

class colors(Scene):
    def construct(self):
        texto0 = Text("Curso de Manim - PURPLE", color=PURPLE).move_to(UP * 3.5)
        texto1 = Text("Curso de Manim - YELLOW", color=YELLOW).move_to(UP * 2.5)
        texto2 = Text("Curso de Manim - BLUE", color=BLUE).move_to(UP * 1.5)
        texto3 = Text("Curso de Manim - GREEN", color=GREEN).move_to(UP * 0.5)
        texto4 = Text("Curso de Manim - GRAY", color=GRAY).move_to(DOWN * 0.5)
        texto5 = Text("Curso de Manim - RED", color=RED).move_to(DOWN * 1.5)
        texto6 = Text("Curso de Manim - ORANGE", color=ORANGE).move_to(DOWN * 2.5)
        texto7 = Text("Curso de Manim - PINK", color=PINK).move_to(DOWN * 3.5)
        self.play(Write(texto0))
        self.play(Write(texto1))
        self.play(Write(texto2))
        self.play(Write(texto3))
        self.play(Write(texto4))
        self.play(Write(texto5))
        self.play(Write(texto6))
        self.play(Write(texto7))
        self.wait(3)

class colors2(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        self.camera.background_color=color1
        texto1 = Text("Pitágoras", color=color2).move_to(UP * 2).scale(2)
        texto2 = Text("Pitágoras").move_to(UP * 0.5).scale(1.5)
        texto2.set_color(color3)
        texto3 = Text("Pitágoras", color=color4).move_to(DOWN)
        texto4 = Text("Pitágoras", color=BLUE).move_to(DOWN * 2).scale(0.75)
        texto5 = Text("Pitágoras", color=WHITE).move_to(DOWN * 3).scale(0.5)
        self.play(Write(texto1))
        self.play(Write(texto2))
        self.play(Write(texto3))
        self.play(Write(texto4))
        self.play(Write(texto5))
        self.wait(3)

class colors3(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        texto1=Text("Pitágoras").scale(2).set_color_by_gradient(color1, color2)
        self.play(Write(texto1))
        self.wait(3)
        texto2 = Text("Pitágoras").scale(2).set_color_by_gradient(color1, color2,color3, color4)
        self.play(Write(texto2))
        self.wait(3)

class colors4(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        texto1=MarkupText(f'curso de <span fgcolor="{color4}">manim</span>', color=color2).move_to(UP*2).scale(2)
        self.play(Write(texto1))
        self.wait(2)
        texto2=Text("curso manim", t2c={'[3:5]':color4}).scale(2).move_to(UP*0.5) 
        self.play(Write(texto2))
        self.wait(2)
        texto3=Text("0123456789", t2c={'[1:5]':color4}).scale(2).move_to(DOWN)
        self.play(Write(texto3))
        self.wait(2)
        texto4=Text("0123456789", t2c={'[5:-2]':color4}).scale(2).move_to(DOWN*2.5)
        self.play(Write(texto4))
        self.wait(2)

        a=Text("hola wey")
        self.add(a)
        self.wait(2)

    
