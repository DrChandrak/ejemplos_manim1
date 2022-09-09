from manim import*
class n2p(Scene):

    def construct (self):
        number_line = NumberLine(x_range=[-10,10,1]).number_to_point(0)
        self.add(number_line)

        #number_line.number_to_point(0).array([0., 0., 0.])
        #number_line.number_to_point(1)
        #array([1., 0., 0.])
        #number_line.number_to_point([1,2,3])
        #array([[1., 0., 0.],[2., 0., 0.],[3., 0., 0.]])