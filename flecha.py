from manim import *
from manim.mobject.geometry.tips import ArrowTriangleTip,\
                                        ArrowSquareTip, ArrowSquareFilledTip,\
                                        ArrowCircleTip, ArrowCircleFilledTip

class flecha(Scene):
    def construct(self):
        f1=Arrow(tip_shape=ArrowTriangleTip)
    
        self.add(f1)


