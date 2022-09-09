from manim import *

import numpy as np

class Grafica2(Scene):
        def construct(self):
            eje= Axes(x_range=[-1,5,1], y_range=[-2,2,1])
            f=lambda x: np.sin(x*PI )* x/2
            plot=eje.get_graph(f, color=BLUE)
            area=eje.get_area(plot, x_range=[1,3])
            self.add(eje)
            self.wait()
            self.play(Create(plot))
            self.play(DrawBorderThenFill(area))
            self.wait()