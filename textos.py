from manim import *

class lec1(Scene):
    def construct(self):
        text1=Text("Hola mundo")
        self.add(text1)
        self.wait(3)

class lec2(Scene):
    def construct(self):
        text2=Text("Curso de manim")
        self.add(text2)
        self.wait(4)
        self.remove(text2)
        self.wait(4)


class lec3(Scene):
    def construct(self):
        tex3=Text("Otro curso de manim")
        self.play(FadeIn(tex3))
        self.wait(2)
        self.play(FadeOut(tex3))
        self.wait(2)
        self.play(Write(tex3))
        self.wait(2)

class lec4(Scene):
    def construct(self):
        cuadric=NumberPlane()
        self.add(cuadric)
        self.wait(5)
        text4=Text("Teorema").move_to(RIGHT+UP)
        text5=Text("Lema").move_to(LEFT+DOWN)
        self.add(text4, text5)
        self.wait(4)

class lec5(Scene):
    def construct(self):
        cuadric=NumberPlane()
        self.add(cuadric)
        self.wait(5)
        text6=Text("A").move_to(RIGHT+UP)
        text7=Text("B").move_to(LEFT+DOWN)
        text8=Text("C").move_to(LEFT*2.5)
        text9=Text("D").move_to(DOWN*3.2)
        self.add(text6, text7, text8,text9)
        self.wait(4)


class lec6(Scene):
    def construct(self):
        cuadric=NumberPlane()
        self.add(cuadric)
        self.wait(5)
        text6=Text("A").move_to(np.array([2,2,0]))
        text7=Text("B").move_to(np.array([-2,-2,0]))
        text8=Text("C").move_to(np.array([-3.5,0,0]))
        text9=Text("D").move_to([0,-2.8,0])
        self.add(text6, text7, text8,text9)
        self.wait(4)

        
class lec7(Scene):
    def construct(self):
        text10=Text("aprendiendo manim").move_to(UP)
        text11=Text("conociendo el código").move_to(DOWN)
        text12=Text("primeros pasos").move_to(UP)
        self.play(FadeIn(text10))
        self.wait(3)
        self.play(Transform(text10, text11))
        self.wait(3)
        self.play(Transform(text10, text12))


