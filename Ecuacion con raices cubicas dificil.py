from manim import *
class p1ii(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       
        eq =MathTex("\\sqrt[3]{x}","+","\\sqrt[3]{x-16}","=","\\sqrt[3]{x-8}")\
            .scale(1.25).next_to(ORIGIN,7*UP)
        eq1 = MathTex("\\sqrt[3]{x} = ","\\sqrt[3]{x-8}","-","\\sqrt[3]{x-16}")\
            .scale(1.25).next_to(eq,DOWN)
        eq2 = MathTex("1 = ","\\frac{\\sqrt[3]{x-8}}{\\sqrt[3]{x}}","-","\\frac{\\sqrt[3]{x-16}}{\\sqrt[3]{x}}")\
            .scale(1.25).next_to(eq1,DOWN)
        eq3 = MathTex("1 = ","\\sqrt[3]{\\frac{x-8}{x}}","-","\\sqrt[3]{\\frac{x-16}{x}}")\
            .scale(1.25).next_to(eq2,DOWN)


        eq4 = MathTex("1 = ","\\sqrt[3]{1 - \\frac{8}{x}}","-","\\sqrt[3]{1 - \\frac{16}{x}}")\
            .scale(1.25).next_to(eq2,DOWN)
       
        eq5 = MathTex("\\sqrt[3]{1 - \\frac{8}{x}}","=","w")\
            .scale(1.25).next_to(eq,DOWN*3)
        eq6 = MathTex("\\sqrt[3]{1 - \\frac{16}{x}}","=","z")\
            .scale(1.25).next_to(eq5,DOWN)


        eq7 = MathTex("1 - \\frac{8}{x}","=","w^3")\
            .scale(1.25).next_to(eq,DOWN*0.5)
       
        eq8 = MathTex("-\\frac{8}{x}","=","w^3-1")\
            .scale(1.25).next_to(eq,DOWN*0.5)


        eq9 = MathTex("-\\frac{8}{w^3 -1}","=","x")\
            .scale(1.25).next_to(eq8,DOWN*0.5)


        eq10 = MathTex("\\frac{8}{1-w^3 }","=","x")\
            .scale(1.25).next_to(eq9,DOWN)


        framebox0 = SurroundingRectangle(eq,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “c_o1”
       


        play(seven_line.animate.to_corner(UR))
       
        play(Write(
            eq),
        run_time = 3
        )
        self.play(
        Create(framebox0), #Ejecute el perímetro que te declare anteriormente
        )
        wait(2)
        play(FadeOut(framebox0))


        play(Write(
            eq1),
        run_time = 3
        )


        play(Write(
            eq2),
        run_time = 3
        )


        play(Write(
            eq3),
        run_time = 3
        )


        play(TransformMatchingTex(
            eq3,eq4
        ),
        run_time=3
        )


        play(FadeOut(eq),FadeOut(eq1),FadeOut(eq2),FadeOut(eq3))
       


        play(eq4.animate.move_to(
            UP*2
        ))


        play(Write(
            eq5),
        run_time = 3
        )


        play(Write(
            eq6),
        run_time = 3
        )


        play(FadeOut(eq4),FadeOut(eq6))


        play(eq5.animate.move_to(
            UP*2
        ))


        play(TransformMatchingTex(
            eq5,eq7
        ),
        run_time=2
        )


        play(TransformMatchingTex(
            eq7,eq8
        ),
        run_time=3
        )
       
        play(Write(
            eq9),
        run_time = 3
        )


        play(Write(
            eq10),
        run_time = 3
        )
       
        wait(3)


        #En este caso es mejor lo SENCILLO, escribir las ecuaciones como si se escribieran en una libreta. Sin transformaciones innecesarias.


        # manim -pqh scene9.py p1ii


       


from manim import *
class p2(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       
        eq = MathTex("\\sqrt[3]{1 - \\frac{16}{x}}","=","z")\
            .scale(1.25).next_to(ORIGIN,UP*7)
        #play(seven_line.animate.to_corner(UR))


        eq1 = MathTex("1 - \\frac{16}{x}","=","z^3")\
            .scale(1.25).next_to(eq,DOWN)


        eq2 = MathTex("-\\frac{16}{x}","=","z^3-1")\
            .scale(1.25).next_to(eq,DOWN)


        eq3 = MathTex("-\\frac{16}{z^3 -1}","=","x")\
            .scale(1.25).next_to(eq2,DOWN)


        eq4 = MathTex("\\frac{16}{1-z^3 }","=","x")\
            .scale(1.25).next_to(eq3,DOWN)
       
        play(Write(
            eq),
        run_time = 3
        )




        play(Write(
            eq1
        ),
        run_time=3
        )


        play(TransformMatchingTex(
            eq1,eq2
        ),
        run_time=3
        )


        play(Write(
            eq3),
        run_time = 3
        )


        play(Write(
            eq4),
        run_time = 3
        )
       
        wait(3)


        # manim -pqh scene9.py p2


from manim import *
class p3i(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       
        eq = MathTex("\\frac{16}{1-z^3 }","=","x",",","\\frac{8}{1-w^3 }","=","x")\
            .scale(1.25).next_to(ORIGIN,UP*7)
        #play(seven_line.animate.to_corner(UR))




        eq2 = MathTex("\\frac{16}{1-z^3 }","=","\\frac{8}{1-w^3 }")\
            .scale(1.25).next_to(eq,DOWN*2)


        line1= Text("Ahora despejaremos a w / Now we will isolate w")\
            .scale(0.6).next_to(eq2,2*DOWN)


        eq3 = MathTex("w","=","\\sqrt[3]{\\frac{z^3+1}{2}}")\
            .scale(1.25).next_to(line1,DOWN)


        play(Write(
            eq),
        run_time = 3
        )




        play(Write(
            eq2),
        run_time = 3
        )


        play(FadeIn(line1))


        play(Write(
            eq3),
        run_time = 3
        )
   
        wait(3)


        # manim -pqh scene9.py p3i


from manim import *
class p4(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       
        eq = MathTex("1","=","w","-","z")\
            .scale(1.25).next_to(ORIGIN,UP*7)
        #play(seven_line.animate.to_corner(UR))


        line_1 = Text("Recordemos que: / Let remember that:")\
            .scale(0.7).next_to(eq,UP)


        eq1 = MathTex("1+z","=","\\sqrt[3]{\\frac{z^3+1}{2}}")\
            .scale(1.25).next_to(eq,DOWN)


        line_2 = Text("Simplificamos e igualamos a cero: / We simplify and equate to zero:")\
            .scale(0.6).next_to(eq1,DOWN)


        eq2 = MathTex("z^3 +6z^2 +6z+ 1 = 0")\
            .scale(1.25).next_to(line_2,DOWN)


       


        play(Write(
            line_1),
            run_time = 2
            )
       
        play(Write(
            eq),
        run_time = 3
        )


        play(Write(
            eq1),
        run_time = 3
        )


        play(Write(
            line_2),
            run_time = 2
            )


        play(Write(
            eq2),
        run_time = 3
        )


        wait(3)


        # manim -pqh scene9.py p4  




from manim import *
class p5(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       
        line_1 = Text("Trabajamos con la primera solución/ We work with the first solution")\
            .scale(0.6).next_to(ORIGIN,UP*8)


        eq = MathTex("z","=","-1")\
            .scale(1.25).next_to(line_1,DOWN)
        #play(seven_line.animate.to_corner(UR))


        line_2 = Text("Recordemos que :/Remember that:")\
            .scale(0.7).next_to(eq,DOWN)


        eq1 = MathTex("z","=","\\sqrt[3]{1 - \\frac{16}{x}}")\
            .scale(1.25).next_to(line_2,DOWN)


        line_3 = Text("Sustituyendo y despejando x / Substituting and solving for x")\
            .scale(0.6).next_to(eq1,DOWN)


        eq2 = MathTex("x=8")\
            .scale(1.25).next_to(line_3,DOWN)


        framebox1 = SurroundingRectangle(eq2,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “c_o1”
       


 
        play(Write(
            line_1),
            run_time = 2
            )
       
        play(Write(
            eq),
        run_time = 3
        )


        play(Write(
            line_2),
            run_time = 2
            )


        play(Write(
            eq1),
        run_time = 3
        )


        play(Write(
            line_3),
            run_time = 2
            )


        play(Write(
            eq2),
        run_time = 3
        )


        self.play(
        Create(framebox1), #Ejecute el perímetro que te declare anteriormente
        )
        wait(2)
        play(FadeOut(framebox1))


        wait(1)


        # manim -pqh scene9.py p5      




from manim import *
class p6i(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       
        line_1 = Text("Trabajamos con la segunda solución/ We work with the second solution")\
            .scale(0.6).next_to(ORIGIN,UP*9)


        eq = MathTex("z","=","-\\frac{5}{2}","-\\frac{\\sqrt{21}}{2}")\
            .scale(1.25).next_to(line_1,DOWN)
        #play(seven_line.animate.to_corner(UR))


        line_3 = Text("Sustituyendo y despejando x / Substituting and solving for x")\
            .scale(0.6).next_to(eq,DOWN)


        eq2 = MathTex("x=","\\frac{16}{56+12\\sqrt{21}}","\\approx","0.144")\
            .scale(1.25).next_to(line_3,DOWN)


        framebox1 = SurroundingRectangle(eq2,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “c_o1”


        play(seven_line.animate.to_corner(UR))


        play(Write(
            line_1),
            run_time = 2
            )
       
        play(Write(
            eq),
        run_time = 3
        )


        play(Write(
            line_3),
            run_time = 2
            )


        play(Write(
            eq2),
        run_time = 3
        )


        self.play(
        Create(framebox1), #Ejecute el perímetro que te declare anteriormente
        )
        wait(2)
        play(FadeOut(framebox1))


        wait(1)


        # manim -pqh scene9.py p6i      




from manim import *
class p7i(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       
        line_1 = Text("Trabajamos con la tercera solución/ We work with the third solution")\
            .scale(0.6).next_to(ORIGIN,UP*9)


        eq = MathTex("z","=","\\frac{\\sqrt{21}}{2}","-\\frac{5}{2}")\
            .scale(1.25).next_to(line_1,DOWN)
        #play(seven_line.animate.to_corner(UR))


        line_3 = Text("Sustituyendo y despejando x / Substituting and solving for x")\
            .scale(0.6).next_to(eq,DOWN)


        eq2 = MathTex("x=","\\frac{16}{56-12\\sqrt{21}}","\\approx","15.855")\
            .scale(1.25).next_to(line_3,DOWN)


        framebox1 = SurroundingRectangle(eq2,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “c_o1”


        play(seven_line.animate.to_corner(UR))
 
        play(Write(
            line_1),
            run_time = 2
            )
       
        play(Write(
            eq),
        run_time = 3
        )


        play(Write(
            line_3),
            run_time = 2
            )


        play(Write(
            eq2),
        run_time = 3
        )
       
        self.play(
        Create(framebox1), #Ejecute el perímetro que te declare anteriormente
        )
        wait(2)
        play(FadeOut(framebox1))


        wait(1)


        # manim -pqh scene9.py p7i  


        #SI PUDIERA HACER DE NUEVO ESTE PROYECTO, EXPLICARÍA MEJOR CADA PASO (SIEMPRE Y CUANDO TENGO ESPACIO SUFICIENTE Y AL EXPLICAR NO SE VUELVA ALGO ENGORROSO).
        #De ahí en fuera me gustó, le metí mucha pasión y esfuerzo. Desde la resolución del problema (por propio mérito, no me lo "fusilé" de ningún lugar) hasta mostrarlo con mis amigos en redes sociales.


        #Puebla de Zaragoza a 07 de septiembre de 2022

        """
        Enlace al video en YouTube de esta animación: https://www.youtube.com/watch?v=TG1F02qRc-c
        """

