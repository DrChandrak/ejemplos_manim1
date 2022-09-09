from manim import  * 

class wl2(Scene):
    def construct(self):
        textos=Tex("Welcome",
        "Accueillir", 
        "Bem-vindo", 
        "いらっしゃいませ", 
        "willkommen",  
        "Siyakwamukela", 
        "Bienvenidos" )
        animations=[AddTextLetterByLetter(textos[0], UP*2+LEFT*3, color=BLUE, font_size=50),
        AddTextLetterByLetter(textos[1], UP*3, color=YELLOW, font_size=50),
        AddTextLetterByLetter(textos[2], UP*2+RIGHT*3, color=PINK, font_size=50),
        AddTextLetterByLetter(textos[3], DOWN*2+LEFT*4, color=GREEN, font_size=50),
        AddTextLetterByLetter(textos[4], DOWN*3, color=RED, font_size=24),
        AddTextLetterByLetter(textos[5], DOWN*2+RIGHT*4, color=PURPLE, font_size=50),
        FadeIn(textos[6], UP*3, color=YELLOW, font_size=90)]

        self.play(AnimationGroup(*animations, lag_ratio=0.5))
        self.wait(2)

