from pickle import FALSE, TRUE
from manim import *

class negpos(Scene):
    def construct (self):
        l=NumberLine(x_range=[-10,10,1],
        length=12, color=YELLOW, include_numbers=TRUE,
        label_direction=DOWN, font_size=20, 
        numbers_with_elongated_ticks=[0]) #toda es una linea 
        #escrita en partes. Aquí dibujo una recta numérica
        self.add(l)

        f1=Arrow(max_tip_length_to_length_ratio=0.12, 
        stroke_width=0).move_to(UP*3).rotate(-PI/2) #solo cabeza de la flecha
        f2=Arrow(max_tip_length_to_length_ratio=0.12, 
        stroke_width=2).move_to(UP*1).rotate(-PI/2)
        self.play(Transform(f1,f2))
        t1=Text("Cero", color=YELLOW).next_to(f2,UP).scale(0.75)
        self.play(FadeIn(t1))
      

        f3=Arrow(max_tip_length_to_length_ratio=0.12, 
        stroke_width=0,start=LEFT, end=RIGHT, color=BLUE).move_to(UP*1.5)  
        f4=Arrow(max_tip_length_to_length_ratio=0.12, 
        stroke_width=2, start=LEFT,  end=RIGHT, color=BLUE).move_to(UP*1.5+RIGHT*3)  

        f5=Arrow(max_tip_length_to_length_ratio=0.12, 
        stroke_width=0, start=RIGHT, end=LEFT, color=RED).move_to(UP*1.5)
        f6=Arrow(max_tip_length_to_length_ratio=0.12, 
        stroke_width=2,start=RIGHT, end=LEFT, color=RED).move_to(UP*1.5+LEFT*3)

        self.play(Transform(f3,f4), run_time=2)
        t2=Text("Números positivos", color=BLUE).move_to(f4,DOWN).scale(0.5)
        t2j=MathTex(r"\infty ",
        color=BLUE ).next_to(t2, RIGHT).scale(1.25)
        self.play(FadeIn(t2))
        self.play(Transform(f5,f6), run_time=2)
        self.play(Write(t2j))
        t3=Text("Números negativos", color=RED).move_to(f6,DOWN).scale(0.50)
        t3j=MathTex(r"\infty ",
        color=RED ).next_to(t3, LEFT).scale(1.25)
        self.play(FadeIn(t3))
        self.play(Write(t3j))
        self.wait(2)

        self.remove(f1, f2, f3, f4, f5, f6, t1, t2, t3, t2j, t3j)
        self.wait(2)
        


        #segunda parte
        l2=l.copy().move_to(UP*3)
        self.play(Transform(l,l2))
        self.wait(2)

        n1=f3.copy(color=YELLOW).move_to(UP*2)
        self.play(Create(n1))
        self.wait(2)














       




       




     




    