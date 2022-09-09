from manim import *

class flecha2(Scene):
    def construct(self):
        arr = Arrow(np.array([-2, 0, 0]), np.array([-1, 0, 0]))
        #self.add(arr)
        self.play(Create(arr), run_time=2)


