from manim import *

class logo(Scene):
    def construct(self):
        self.camera.background_color="#000033"
        c=Circle(radius=3, color="#FFFFFF")
        self.add(c)
        
        t=Text("Visual_math1.0", font="lobster two", slant=ITALIC, font_size=60, t2c={'[11:14]':YELLOW})
    
        self.add(t)