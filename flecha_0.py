from manim import *

class flecha(Scene):
    def construct(self):
        f1=Arrow(start=[0,0,0], end=[1,0,0], buff=1)
        self.add(f1)

        