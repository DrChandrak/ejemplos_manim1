

from manim import *

class vlogo(Scene):
    def construct(self): 
        self.camera.background_color="#000033" # este codigo cambia el fondo
        c=Circle(radius=3, color="#FFFFFF") # este código da el radio y el color en hexadecimal
        self.play(DrawBorderThenFill(c), run_time=2) # Dibuja el borde, lo rellena en 2 segundos
        
        t=Text("Visual_math1.0", font="lobster two", 
        slant=ITALIC, font_size=60, t2c={'[11:14]':YELLOW}) # tamaño de fuentes y tipo. 
        self.play(AddTextLetterByLetter(t), run_time=2) 
        # Se añade el texto letra por letra en 2 segundos
        gr=VGroup(c,t) # defino un mobject grupal para moverlo en conjunto
        gr2=gr.copy().move_to(LEFT*4).scale(0.5)#c opio, muevo y reduzco el conjunto
        self.play(Transform(gr,gr2),run_time=2 ) # se transforma de gr a gr2
        t2=Text("Matemáticas en movimiento", 
        slant=ITALIC, font_size=40).next_to(gr2) # añado texto, fuente, tipo y forma
        self.play(AddTextLetterByLetter(t2)) # escribe letra por letra
        self.wait()
        
        






