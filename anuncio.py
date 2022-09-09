
from manim import *

class Anuncio(Scene):
    def construct (self):
        self.camera.background_color="#000033"
        tx1=Text("""\t\tUna nueva forma de comprender
        y visualizar las matemáticas 
        se está construyendo en el mundo.""", color="#FFFF00")
        self.play(FadeIn(tx1))
        self.wait()
        self.play(tx1.animate.shift(UP*2.5))
        self.wait()

        tx2=Text("""\t\tA través de la animación
        matemática, usando 
        Python y Manim.""", color="#FFFF00")
        self.play(Write(tx2))
        self.wait(1)
        self.play(tx2.animate.shift(DOWN*2.5))
        self.wait(1)

        self.remove(tx1, tx2)
        self.wait()

        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))

        tx3=Text("""\t\tManim es una librería
        escrita en Python que
        permite hacer animación matemática""", color="#FFFF00")
        self.play(FadeIn(tx3))
        self.wait()
        self.play(tx3.animate.shift(UP*2.5))
        self.wait()

        tx4=Text("""\t\tEstudiantes de todos los niveles
        podrán visualizar aspectos
        difíciles de explicar y lograr
        una  mejor comprensión de ellas.""", color="#FFFF00")
        self.play(Write(tx4))
        self.wait()
        self.play(tx4.animate.shift(DOWN*2.5))
        self.wait()

        self.remove(tx3, tx4)
        self.wait()

        tx5=Text("Ejemplos de lo que se puede hacer con manim:", 
        color="#FFFF00").move_to(UP*3.5).scale(0.5)
        self.play(FadeIn(tx5))

        t=Triangle(color=ORANGE, fill_opacity=1)
        self.play(t.animate.shift(LEFT*3.5) )

        f=MathTex(r"\\A=\frac{b\cdot h}{2}") 
        self.play(Write(f))
        self.wait()

        f2=MathTex(r"\\P=\ L\ +\ L\ +\ L").move_to(RIGHT*4)
        self.play(Write(f2))
        self.wait()
        self.remove(t,f,f2)

        eje=Axes(x_range=(-3,3), y_range=(-3,3))
        curva=eje.plot(lambda x:(x+2)*x*(x-2)/2, color="#FFFF00")
        area=eje.get_area(curva, x_range=(-2,2))
        self.play(Create(eje), runtime=(5))
        self.play(Create(curva), runtime=(5))
        self.play(FadeIn(area), runtime=(3))
        self.wait(3)
        self.remove(eje, curva, area)

        



