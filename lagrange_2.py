
from manim import *


class Lagrangiano(Scene):
    def construct(self):
        
        F = MathTex(
                "\\mathbf{F}" , color=YELLOW
                )
        eq = MathTex(
                "\\ = \\"
                )
        
        m = MathTex(
                "m", color=YELLOW
                )


        a = MathTex(
                "\\mathbf{a}", color=BLUE
                )
        

        
 
        
        ddt = MathTex(
                "{ \\mathrm{d} \\over \\mathrm{d} t }"
                ).scale(2)
        
        eq.next_to(F, RIGHT)
        m.next_to(eq, RIGHT)
        a.next_to(m, .2*RIGHT)
                
        
        group = Group(F, eq, m,a).shift(LEFT).shift(UP)
        group.scale(2)
        
        dvdt = MathTex(
                "{ \\mathrm{d} \\mathbf{v} \\over \\mathrm{d} t }",
                tex_to_color_map = {"\\mathbf{v}": BLUE}
                )
        dvdt.scale(2).next_to(m, RIGHT)
        v = dvdt.get_part_by_tex("\\mathbf{v}")
        d = dvdt.get_part_by_tex("\\mathrm{d}")
            
        ddt.move_to(dvdt)
        
        grad = MathTex("- \\nabla U ( \\mathbf{x} )  ", tex_to_color_map={"U": WHITE,"\\mathbf{x}": BLUE}).scale(1.5)
        newF = MathTex(
                "\\mathbf{F}" , color=YELLOW
                ).scale(1.5)
        neweq = MathTex("=").scale(1.5)
        newF.next_to(F, 8*DOWN)
        neweq.next_to(newF,RIGHT)
        grad.next_to(neweq, RIGHT)
        
        
        
        
        
        self.play(Write(F))
        #self.add_sound("summer.mp3")
        self.wait()
        self.play(Write(eq))
        self.play(Write(m))
        self.play(Write(a))
        self.wait(1)
        self.play(ReplacementTransform(a, dvdt))
        self.wait(1)
        self.play(CyclicReplace(dvdt, m))
        self.wait(1)
        self.play(ApplyMethod(m.next_to, dvdt,RIGHT), ApplyMethod(v.next_to, m, .2*RIGHT),
                  ApplyMethod(d.shift, RIGHT*.01))
        mv = Group(m,v)
        self.wait(1)
        p = MathTex("\\mathbf{p}", color=BLUE).move_to(mv).scale(2.1)
        self.play(ReplacementTransform(mv, p))
        self.play(ApplyMethod(p.next_to, d, RIGHT*.3))
        self.wait(1)
        self.play(GrowFromCenter(neweq), FadeIn(newF, 2*LEFT), FadeIn(grad, 2*RIGHT))
        dpdt = Group(dvdt, p)
        self.wait(1)
        self.play(ApplyMethod(grad.next_to, eq, LEFT*2), FadeOut(F, 10*LEFT),
                  ApplyMethod(dpdt.scale, 1.5/2) , FadeOut(newF, 10*LEFT), 
                  FadeOut(neweq,20*DOWN) )
        newtons_law = Group(grad, eq, dpdt)
        self.play(ApplyMethod(newtons_law.shift, RIGHT))
        newton_text = MathTex(
                "\\text{Segunda ley de Newton", color=RED
                ).scale(2).next_to(newtons_law, UP*2)
        self.play(Write(newton_text))    
        box = Group(newtons_law, newton_text)
        self.play(ApplyMethod(box.scale, .3))
        self.play(ApplyMethod(box.shift, 1.5*UP+ 4.35*LEFT))
        
        lag_0 = MathTex(
                "\\text{Lagrangiano} \\ = \\ \\text{Energía cinética} - \\text{Energía Potencial} ",
                tex_to_color_map={"\\text{Energía Cinética}": BLUE, "\\text{Energía Potencial}": WHITE,
                                  "\\text{Lagrangiano}": YELLOW}
                )
        
        lag = MathTex(
                "\\mathcal{L} \\ = \\ \\frac{1}{2} {m} \\mathbf{v} ^2 \\ -  \\ U( \\mathbf{x} )",
                tex_to_color_map = {"\\mathcal{L}": YELLOW,"\\mathbf{v}": BLUE, 
                                    "\\mathbf{x}": BLUE}
                ).scale(2)
        lag_text = MathTex("\\text{Lagrangiano}", color=RED).next_to(lag, UP*2).scale(2)
        
        
        dummyLHS = MathTex("\\mathcal{L}", color=YELLOW).shift(UP*.2).scale(1.5)
        
        keq = MathTex("\\ = \\").next_to(dummyLHS, 2*RIGHT).scale(1.5)
        
        dummy = MathTex(
                "\\frac{1}{2} {m} \\mathbf{v} ^2",
                tex_to_color_map = {"\\mathbf{v}": BLUE 
                                    }
                ).next_to(keq, 2*RIGHT).scale(1.5) 
        
        dummypot = MathTex("\\ -  \\ U( \\mathbf{x} )",
                              tex_to_color_map={"\\mathbf{x}": BLUE}).next_to(dummy, 2*RIGHT).scale(1.5)
        
        

        
        eqGroup = Group(dummyLHS, keq, dummy, dummypot).move_to(ORIGIN).shift(UP*.5)
        
        summation = MathTex("\\mathcal{L} \\ = \\ \\frac{1}{2} m \\sum_{k=1}^3 \\mathbf{v} _k^2\\ -  \\ U( \\mathbf{x} )", 
                   tex_to_color_map = {"\\mathbf{v}" :BLUE, "\\mathbf{x}": BLUE,
                                       "\\mathcal{L}": YELLOW}).move_to(dummy).scale(1.5)
        
        self.play(Write(lag_0))
        self.wait(2)
        self.play(ReplacementTransform(lag_0, lag))
        self.wait(1)
        self.play(Write(lag_text))
        self.wait(1.5)
        lag_box = Group(lag, lag_text)
        self.play(ApplyMethod(lag_box.match_width, box), ApplyMethod(lag_box.match_height, box))
        self.play(ApplyMethod(lag_box.next_to, box, 7*RIGHT))
        el_eqns = MathTex(
                "{\\mathrm{d} \\over \\mathrm{d} t}",
                "{\\partial", "\\mathcal{L}", "\\over", "\\partial", "\\dot{\\mathbf{x}}", "_i}",
                "\\ = \\", 
                "{\\partial", "\\mathcal{L}", "\\over", "\\partial", "\\mathbf{x}", "_i }"
                
                ).set_color_by_tex("\\mathcal{L}", YELLOW).set_color_by_tex("\\mathbf{x}", BLUE)
        el_eqns.set_color_by_tex("\\dot{\\mathbf{x}}", BLUE).scale(2).shift(DOWN)
        el_text= MathTex("\\text{Ecuación de Euler-Lagrange}", color=RED).scale(2).next_to(el_eqns,2*UP)
        self.play(Write(el_eqns))
        self.wait(1.5)
        xdot = el_eqns.get_part_by_tex("\\dot{\\mathbf{x}}")
        vee = MathTex("\\mathbf{v}", color=BLUE).scale(2.2).move_to(xdot).shift(DOWN*.1)
        self.play(ReplacementTransform(xdot, vee))
        explain = Text(" Para cada componente vectorial $i$", color=YELLOW)
        explain.next_to(el_eqns, 2*DOWN)
        self.play(Write(explain))
        self.wait(1.5)
        self.play(Write(el_text), FadeOut(explain, DOWN))
        self.wait(1.5)
        el_box = Group(el_eqns, el_text,vee)
        self.play(ApplyMethod(el_box.match_width, box), ApplyMethod(el_box.match_height, box))
        self.play(ApplyMethod(el_box.next_to, lag_box, 7*RIGHT))
        bgroup = Group(box, lag_box, el_box)
        self.wait(1)
        self.play(TransformFromCopy(lag, eqGroup))
        self.wait(1.5)
        self.play(ReplacementTransform(eqGroup, summation), FadeOut(dummypot))
        self.wait(3)
        el_1 = MathTex("{\\partial", "\\mathcal{L}", "\\over", "\\partial", "\\mathbf{v}", "_i}" ,
                          "\\ = \\"
                          ).set_color_by_tex("\\mathcal{L}", YELLOW).set_color_by_tex("\\mathbf{v}", BLUE).scale(1.2)
        el_1.next_to(summation, 3.5*DOWN).shift(3*LEFT)
        
        rhs = MathTex("m" ,"\\mathbf{v}", "_i}").set_color_by_tex("\\mathbf{v}", BLUE).scale(1.2)
        rhs.next_to(el_1, RIGHT)
        self.play(TransformFromCopy(el_eqns, el_1 ))
        self.wait(1)
        self.play(Write(rhs))
        self.wait(2)
        mom = MathTex("\\mathbf{p} _i",tex_to_color_map={"\\mathbf{p}": BLUE}).scale(1.2).move_to(rhs)
        self.play(ReplacementTransform(rhs, mom))
        derivt = MathTex("\\frac{\\mathrm{d}}{\\mathrm{d} t}").scale(1.2).next_to(el_1,LEFT)
        pdot = MathTex("{\\mathrm{d} \\mathbf{p} _i \\over \\mathrm{d} t }",
                          tex_to_color_map={"\\mathbf{p}":BLUE}).move_to(mom).scale(1.2)
        self.wait(1)
        self.play(FadeIn(derivt, LEFT), ReplacementTransform(mom, pdot))
        self.wait(1.5)
        derivx = MathTex("{\\partial", "\\mathcal{L}", "\\over", "\\partial", "\\mathbf{x}", "_i }"
                
                ).set_color_by_tex("\\mathcal{L}", YELLOW).set_color_by_tex("\\mathbf{x}", BLUE)
        derivx.next_to(summation, 3.5*DOWN).shift(2.5*RIGHT).scale(1.2)
        dU = MathTex(
                " = - { \\partial U \\over \\partial \\mathbf{x} _i}",
                tex_to_color_map={"\\mathbf{x}": BLUE}).scale(1.2)
        dU.next_to(derivx, RIGHT)
        self.play(TransformFromCopy(el_eqns,derivx))
        self.wait(1)
        self.play(Write(dU))
        self.wait(1.5)
        gp = Group(derivt, el_1, pdot, derivx, dU)
        self.play(ReplacementTransform(summation, lag), ApplyMethod(gp.shift, 2*UP))
        brace = Brace(gp, 3*DOWN)
        eqText= brace.get_text("Estas son iguales, según las ecuaciones de Euler-Lagrange")
        self.wait(1)
        self.play(GrowFromCenter(brace), Write(eqText))
        self.wait(3)
        equality = MathTex(
                "- { \\partial U \\over \\partial", "\\mathbf{x}", "_i} \\ = \\", 
                "{\\mathrm{d}", "\\mathbf{p}", "_i \\over \\mathrm{d} t}"
                ,
                tex_to_color_map={"\\mathbf{p}": BLUE, "\\mathbf{x}": BLUE}
                ).scale(2)
        self.play(FadeOut(brace, DOWN), FadeOut(eqText, DOWN),
                  ReplacementTransform(gp, equality))
        equality_text = Text("Como una ecuación vectorial", color=YELLOW)
        equality_text.next_to(equality, 4*DOWN).scale(1.3)
        self.play(Write(equality_text))
        final = MathTex(
                "-\\nabla U(", "\\mathbf{x}", ") \\ = \\ ","{\\mathrm{d}", 
                "\\mathbf{p}", "\\over \\mathrm{d} t}",
                tex_to_color_map={"\\mathbf{p}": BLUE, "\\mathbf{x}": BLUE}
                ).scale(2)
        self.wait(1.5)
        self.play(FadeOut(equality_text, DOWN), ReplacementTransform(equality, final))
        square = Rectangle(color=YELLOW)
        square.surround(final)
        self.wait(1.5)
        self.play(Write(square))
        g = Group(square, final)
        n2 = Text(" $2^{da}$ ley de Newton", color=RED).next_to(g, UP).shift(DOWN*.5).scale(1.5)
        self.play(ApplyMethod(g.shift, DOWN), Write(n2) )
        self.wait(5)
        CONFIG = {"include_sound": True}

