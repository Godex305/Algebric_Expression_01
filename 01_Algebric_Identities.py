from manim import *
config.pixel_height=1080
config.pixel_width=1920
config.frame_height=9
config.frame_width=16



class Slide1Intro(Scene):
    def construct(self):
        plane=NumberPlane()
        #self.add(plane)
        title = Text('Algebric Expressions',font_size=72)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
class Slide2AimAndWorking(Scene):
    def construct(self):
        aim = Tex("Aim: To determine the expansion of the Algebric expression ","$(a+b)^2$").scale(0.8)
        self.play(Write(aim))
        self.wait(1)
        self.play(aim.animate.to_corner(UL))
        self.add(aim)
        self.wait(3)

        consider = Text("Consider,").scale(0.6).move_to([-6.5,3,0])
        self.play(Write(consider))
        step1 = MathTex("(a+b)^2=","(a+b)(a+b)")
        step1[0].move_to([-4.1,2,0])
        self.play(Write(step1[0]))
        self.wait(0.5)
        step1[1].next_to(step1[0],RIGHT)
        self.play(Write(step1[1]))
        self.wait(0.5)

        step2=MathTex("=","a","(a+b)","+","b","(a+b)")
        step2.move_to([-1.1,1,0])
        self.play(Write(step2))
        self.wait(0.5)
        self.play(Indicate(step2[1]))
        self.wait(0.3)
        self.play(Indicate(step2[2]))
        self.wait(0.3)
        self.play(Indicate(step2[3]))
        self.wait(0.3)
        self.play(Indicate(step2[4]))
        self.wait(0.3)
        self.play(Indicate(step2[5]))
        self.wait(0.3)
        step3 = MathTex("=aa","+ab","+ba","+bb").move_to([-1.2,0,0])
        self.play(Write(step3[0]))
        self.wait(0.3)
        self.play(Write(step3[1]))
        self.wait(0.3)
        self.play(Write(step3[2]))
        self.wait(0.3)
        self.play(Write(step3[3]))
        self.wait(0.3)
        step4=MathTex("=a^2","+ab","+ab","+b^2").move_to([-1.2,-1,0])
        self.play(Write(step4[0]))
        self.wait(0.3)
        self.play(Write(step4[1]))
        self.wait(0.3)
        self.play(Write(step4[2]))
        self.wait(0.3)
        self.play(Write(step4[3]))
        self.wait(0.3)

        step5=MathTex("=a^2","+2ab","+b^2").move_to([-1.6,-2,0])
        self.play(Write(step5[0]))
        self.wait(0.3)
        self.play(Write(step5[1]))
        self.wait(0.3)
        self.play(Write(step5[2]))
        self.wait(0.3)
        self.play(FadeOut(*self.mobjects))
class Slide3ConclusionSlide(Scene):
    def construct(self):
        conclusion = Text("Conclusion:").scale(0.8).move_to([-6,4,0])
        self.play(Write(conclusion))
        Identity1=Tex("$(a+b)^2=a^2+2ab+b^2$")
        Identity1.shift(UP)
        self.play(Identity1.animate.move_to([0,3,0]))
        self.wait(5)
        example = Tex("Example: Use the above identity to simplify ","$(5x+3)^2$.").scale(0.9)
        example.move_to([-2,2,0])
        self.play(Write(example))
        solution = Tex("Solution:").scale(0.9)
        solution.move_to([-6.5,1,0])
        self.play(Write(solution))

        ex_step1=MathTex("(5x+3)^2 = (5x)^2 + 2\\times 5x \\times 3 + (3)^2")
        ex_step2=MathTex("= 25x^2 + 15x + 9")
        group = VGroup(ex_step1,ex_step2)
        group.arrange(RIGHT,buff=0.4)
        group.scale(0.8)
        self.play(Write(group))
        self.play(FadeOut(*self.mobjects))
    
class Slide4OutroSlide(Scene):
    def construct(self):
        title = Text('Thanks for Watching',font_size=72)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Slide0Thumbnail(Scene):
    def construct(self):
        Heading = Text("Algebric Expressions").scale(1.5)
        Topic = Tex("Expansion of ","$(a+b)^2$")
        Heading.shift(UP)
        Topic.shift(DOWN)
        self.add(Heading,Topic)