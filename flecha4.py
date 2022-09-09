from re import L
from manim import *

class fl4(Scene):
    def construct(self):
        f1=Arrow(LEFT*2, 2*RIGHT).scale(0.5)
        self.play(GrowArrow(f1))


        



