from manim import *

class flecha(Scene):
    def construct(self):
        left_group = VGroup()
        # As buff increases, the size of the arrow decreases.
        for buff in np.arange(0, 2.2, 0.20): #comienzo, final e incremento
            left_group += Arrow(buff=buff, start=2 * LEFT, end=2 * RIGHT)
        # Required to arrange arrows.
        left_group.arrange(UP)
        left_group.move_to(4 * LEFT)

        middle_group = VGroup()
        # As max_stroke_width_to_length_ratio gets bigger,
        # the width of stroke increases.
        for i in np.arange(0, 5, 0.5):
            middle_group += Arrow(max_stroke_width_to_length_ratio=i)
        middle_group.arrange(DOWN)

        UR_group = VGroup()
        # As max_tip_length_to_length_ratio increases,
        # the length of the tip increases.
        for i in np.arange(0, 0.3, 0.1):
            UR_group += Arrow(max_tip_length_to_length_ratio=i)
        UR_group.arrange(DOWN)
        UR_group.move_to(4 * RIGHT + 2 * UP)

        DR_group = VGroup()
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareFilledTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleFilledTip)
        DR_group.arrange(DOWN)
        DR_group.move_to(4 * RIGHT + 2 * DOWN)

        self.add(left_group, middle_group, UR_group, DR_group)






         


