from typing_extensions import runtime
from manim import *

class inv(Scene):
    def construct (self):

        t=Text("""        Mi escultura es como el grito del 
        canto primigenio y del cómo suena la locura 
        para mirar a través de esa ventana y acariciar 
        los excesos del lenguaje de los eros. 
        Salamandras matutinas ansiosas de mirar, de 
        mirar... y quizás hablar. """, font="lobster two",slant=ITALIC, font_size= 50).move_to(UP)

        self.play(AddTextLetterByLetter(t), runtime=(8))
        self.wait(1)


        t1=Text("-Eduardo Beristain", font="karumbi", font_size= 100).move_to(RIGHT+DOWN*2)
        self.play(AddTextLetterByLetter(t1))
        self.wait(3)
        self.remove(t,t1)

        img=ImageMobject("beris.jpg").move_to(LEFT*5)
        self.play(FadeIn(img))

        t2=Text("""          Los invito a la inauguración de una 
           exposición de mi obra.
           Lugar: Casa de la Cultura de Azcapotzalco
           Dirección: Av. Azcapotzalco 605 
           frente al jardín Hidalgo
           Día: Viernes 26 de agosto de 2022
           Hora: 6 p.m. """, font=" lobster two", font_size=45 ).move_to(RIGHT*2)
        self.play(GrowFromEdge(t2,LEFT))
        self.wait(10)
        self.remove(img,t2  )


        i1=ImageMobject("1.jpg").move_to(RIGHT*3+UP*2.5).scale(1.25)
        i2=ImageMobject("2.jpg").move_to(UP*2.5).scale(1.25)
        i3=ImageMobject("3.jpg").move_to(LEFT*3 +UP*2.5).scale(1.25)
        i4=ImageMobject("4.jpg").move_to(RIGHT*3).scale(1.25)
        i5=ImageMobject("5.jpg").scale(1.25)
        i6=ImageMobject("6.jpg").move_to(LEFT*3).scale(1.25)
        i7=ImageMobject("7.jpg").move_to(DOWN*2.5).scale(1.25)
        
        self.play(GrowFromEdge(i1, DOWN))
        self.play(GrowFromEdge(i2, DOWN))
        self.play(GrowFromEdge(i3, DOWN))
        self.play(GrowFromEdge(i4, DOWN))
        self.play(GrowFromEdge(i5, DOWN))
        self.play(GrowFromEdge(i6, DOWN))
        self.play(GrowFromEdge(i7, DOWN))
        self.wait(2)
        self.remove(i1,i2,i3,i4,i5,i6,i7)

        img2=ImageMobject("beris2.jpeg").scale(1.3)
        self.add(img2)
        t3=Text("""  Les esperamos.

            atte: Eduardo Beristain""", font="karumbi", font_size=80).move_to(RIGHT*2)
        self.play(AddTextLetterByLetter(t3))
        self.wait(2)

        


        



        



        

