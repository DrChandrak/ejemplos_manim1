from manim import *

config.pixel_height=1152
config.pixel_width=2048
config.frame_height=16
config.frame_width=9

class logo(Scene):
    def construct(self):
        self.camera.background_color="#000033"
        c=Circle(radius=3, color="#FFFFFF").move_to(LEFT*2.5).scale(0.25)
        self.add(c)
        
        t=Text("Visual_math1.0", font="lobster two", slant=ITALIC, font_size=60, t2c={'[11:14]':YELLOW}).move_to(LEFT*2.5).scale(0.25)
        t2=Text("Matemáticas en movimiento", font="lobster two",slant=ITALIC, font_size=30).next_to(t, RIGHT*2)

        self.add(t)
        self.add(t2)

