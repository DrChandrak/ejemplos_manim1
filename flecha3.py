
from manim import *

class fl3(Scene):
    def construct(self):
        f1=Triangle(color=WHITE, fill_opacity=1).rotate(30*DEGREES).scale(0.15)
        f2=Arrow(np.array([2, 0, 0]), np.array([4, 0, 0]))
        self.play(Transform (f1,f2))



