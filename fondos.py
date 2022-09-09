from manim import *

class fond1(Scene):
    def construct(self):
        self.camera.background_color="#000033"
        t1=Text("Esta es una prueba", color="#FFFF00")
        t2=Text("Esta es otra prueba").move_to(DOWN)
        self.play(Write (t1))
        self.play(Write (t2))
