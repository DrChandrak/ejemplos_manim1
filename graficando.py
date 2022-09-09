from typing_extensions import runtime
from manim import *

class Graficando(Scene):
    def construct (self):
        eje=Axes(x_range=(-3,3), y_range=(-3,3))
        curva=eje.plot(lambda x:(x+2)*x*(x-2)/2, color=BLUE)
        area=eje.get_area(curva, x_range=(-2,2))
        self.play(Create(eje), runtime=(5))
        self.play(Create(curva), runtime=(5))
        self.play(FadeIn(area), runtime=(3))
        self.wait(3)
