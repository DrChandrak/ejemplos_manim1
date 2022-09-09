from manim import *

class wlcom(Scene):
    def construct (self):
        a=Text("Welcome", color=BLUE, font_size=50).move_to(UP*2+LEFT*3)
        b=Text("Accueillir", color=YELLOW, font_size=50).move_to(UP*3)
        c=Text("Bem-vindo", color=PINK, font_size=50).move_to(UP*2+RIGHT*3)
        d=Text("いらっしゃいませ", color=GREEN, font_size=50).move_to(DOWN*2+LEFT*4)
        e=Text("Herzlich willkommen", color=RED, font_size=50).move_to(DOWN*3)
        f=Text("Siyakwamukela", color=PURPLE, font_size=50).move_to(DOWN*2+RIGHT*4)
        g=Text("Bienvenidos", font_size=90)

        self.play(AddTextLetterByLetter(a))
        self.play(AddTextLetterByLetter(b))
        self.play(AddTextLetterByLetter(c))
        self.play(AddTextLetterByLetter(d))
        self.play(AddTextLetterByLetter(e))
        self.play(AddTextLetterByLetter(f))
        self.play(FadeIn(g))
        self.wait(2)

        





