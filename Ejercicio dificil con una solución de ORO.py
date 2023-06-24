from manim import *
class p1iii(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
        eq1 =MathTex("\\sqrt{x- \\frac{1}{x}}","+","\\sqrt{1-\\frac{1}{x}}","=","x")\
            .scale(1.5).next_to(ORIGIN,4*UP)
        eq11 =MathTex("x - \\frac{1}{x}","+2\\sqrt{x- \\frac{1}{x}}\\sqrt{1-\\frac{1}{x}}","+1 - \\frac{1}{x}","=","x^2")\
            .scale(1.25).next_to(eq1,DOWN)
        eq111 = MathTex("+2\\sqrt{x- \\frac{1}{x}}\\sqrt{1-\\frac{1}{x}}","+1 - \\frac{1}{x}","+x - \\frac{1}{x}","=","x^2")\
        .scale(1.25).next_to(eq1,DOWN)
        eq13 = MathTex("+2\\sqrt{x- \\frac{1}{x}}\\sqrt{1-\\frac{1}{x}}","+1 - \\frac{1}{x}","- \\frac{1}{x}","+x","=","x^2")\
        .scale(1.25).next_to(eq1,DOWN)
        eq14 = MathTex("+2\\sqrt{x- \\frac{1}{x}}\\sqrt{1-\\frac{1}{x}}","+1 -\\frac{2}{x}","+x","=","x^2")\
        .scale(1.25).next_to(eq1,DOWN)
        eq15 = MathTex("2\\sqrt{x- \\frac{1}{x}}\\sqrt{1-\\frac{1}{x}}","=","x^2","-x","+\\frac{2}{x}","-1")\
        .scale(1.25).next_to(eq14,DOWN)
       
        play(seven_line.animate.to_corner(UR))
        play(FadeIn(eq1))
        framebox0 = SurroundingRectangle(eq1,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “eq1”
        play(Create(#Ejecute el perímetro que te declare anteriormente
            framebox0
            ),
            run_time =2
        )


        wait(15)#wait(15) -- Es para decir "Lo que haremos ahora es elevar toda la ecuación al cuadrado, para ir "quitando", por decirlo así, las raíces cuadradas. Recuerden la regla para el cuadrado de un binomio: el cuadrado del primer término, más el doble producto del primer término por el segundo, más el cuadrado del segundo término.
        play(FadeOut(framebox0))
        play(Write(eq11),run_time =3)
        wait(17)# wait(10) -- Vamos a reagrupar para que se observe con más facilidad como se reducen términos semejantes.
        play(TransformMatchingTex(
            eq11,eq111
        ),
        run_time=3
        )
        wait(2)
        play(TransformMatchingTex(
            eq111,eq13
        ),
        run_time=2
        )
        wait(2)
        play(TransformMatchingTex(
            eq13,eq14
        ),
        run_time=2
        )
        wait(2)
        play(Write(eq15),run_time=3)
        wait(15)# En esta última igualdad se aprecia que hemos dejado en un lado las raices, lo hemos hecho de esa forma para elevar nuevamente al cuadrado y no complicar las cosas con un binomio


        wait(3)
 
        # manim -pqh scene8.py p1iii


from manim import *
class p2ii(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
        eq14 = MathTex("2\\sqrt{x- \\frac{1}{x}}\\sqrt{1-\\frac{1}{x}}","=","x^2","-x","+\\frac{2}{x}","-1")\
        .scale(1.25).next_to(ORIGIN,UP*4)
       
        eq15 = MathTex("4[x-x^{-1}][1-x^{-1}]","=","x^4","-2x^3","-x^2","+\\frac{4}{x^2}","+6x","-\\frac{4}{x}","-3")\
        .scale(1.0).next_to(eq14,DOWN)
        eq16 = MathTex("4(x-1-x^{-1}+x^{-2})","=","x^4","-2x^3","-x^2","+\\frac{4}{x^2}","+6x","-\\frac{4}{x}","-3")\
        .scale(1.0).next_to(eq15,DOWN)
        eq17 = MathTex("4x","-4","-4x^{-1}","+4x^{-2}","=","x^4","-2x^3","-x^2","+\\frac{4}{x^2}","+6x","-\\frac{4}{x}","-3")\
        .scale(1.0).next_to(eq16,DOWN)

        play(seven_line.animate.to_corner(UR))# Mi nombre se desplaza a la esquina superior derecha, aunque estoy pensando ya solo hacer eso una sola vez y ya no desaparecerá la animación por completo. Si no la última línea subirla y seguir trabajando como lo hace MindyourDecisions
        wait(1)
        play(Write(eq14))
        wait(15)# --
        play(Write(eq15),run_time=3)
        wait(1)
        play(Write(eq16),run_time = 3)
        wait(1)
        play(Write(
            eq17),
        run_time = 3
        )
        wait(17) #wait(12) -- Es para decir, recordemos que 4x^-1 es igual a 4 sobre x. Entonces es válido quitarlos para simplificar.
        play(FadeOut(eq17[2]),FadeOut(eq17[10]))
        wait(2)
        play(FadeOut(eq17[3]),FadeOut(eq17[8]))


        wait(3)


        # manim -pqh scene8.py p2ii


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
       
        eq = MathTex("4x","-4","=","x^4","-2x^3","-x^2","+6x","-3")\
        .scale(1.45).next_to(ORIGIN,UP*6)
        eq1 = MathTex("0 =","x^4","-2x^3","-x^2","+6x-4x","-3","+4")\
        .scale(1.45).next_to(eq,DOWN)
        eq2 = MathTex("0 =","x^4","-2x^3","-x^2","+2x","+1")\
        .scale(1.45).next_to(eq1,DOWN)
        eq3 = MathTex("0 = ","(x^2-x-1)(x^2-x-1)")\
        .scale(1.45).next_to(eq2,DOWN)
       
        eq4 = MathTex("0 = ","x^2-x-1")\
        .scale(1.45).next_to(eq3,DOWN)
       
        play(seven_line.animate.to_corner(UR))# Mi nombre se desplaza a la esquina superior derecha, aunque estoy pensando ya solo hacer eso una sola vez y ya no desaparecerá la animación por completo. Si no la última línea subirla y seguir trabajando como lo hace MindyourDecisions
       
        play(Write(
            eq),
        run_time = 3
        )
        wait(15)# Continuamos manipulando la ecuación
        play(Write(
            eq1),
        run_time = 3
        )
        wait(15)
        play(Write(
            eq2),
        run_time = 3
        )
        wait(15)#Lo que haremos en este momento es sacar la raíz cuadrada de este polinomio con el que estamos trabajando.
        play(Write(
            eq3),
        run_time = 3
        )
        wait(10) #¿Qué pasa si dividimos toda la igualdad por x^2-x-1? Lo que conseguiremos es que simplificamos la ecuación
        play(Write(
            eq4),
        run_time = 3
        )
        wait(10) # De acuerdo, ya tenemos una ecuación de segundo grado, podemos emplear la formula cuadrática . Y eso es lo que haremos
 
        wait(3)


        # manim -pqh scene8.py p3i


from manim import *
class p4i(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       
        eq = MathTex("x","=","\\frac{1}{2}","-\\frac{\\sqrt{5}}{2}")\
        .scale(2).next_to(ORIGIN,UP*2)
        eq1 = MathTex("x","=","\\frac{1}{2}","+\\frac{\\sqrt{5}}{2}")\
        .scale(2).next_to(eq,DOWN)
       
        play(seven_line.animate.to_corner(UR))
       
        play(Write(
            eq),
        run_time = 3
        )
        framebox0 = SurroundingRectangle(eq,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “eqz18”
        play(Create(#Ejecute el perímetro que te declare anteriormente
            framebox0
            ),
            run_time =2
        )
        play(FadeOut(framebox0))


        play(Write(
            eq1),
        run_time = 3
        )
        framebox1 = SurroundingRectangle(eq1,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “eqz18”
        play(Create(#Ejecute el perímetro que te declare anteriormente
            framebox1
            ),
            run_time =2
        )
        play(FadeOut(framebox1))
        wait(18) #Para decir : "Lo prometido es deuda, hemos encontrado el valor de las incógnitas que satisfacen esta ecuación.La segunda solución de arriba a abajo es el número áureo, es muy interesante, porque se puede encontrar en algunas obras de arte, en las pirámides de Giza, cajetillas de cigarros, tarjetas de crédito, etcétera. Espero que les haya gustado, consideren suscribirse."
       
 
        wait(3)


        # manim -pqh scene8.py p4i


# NOTAS FINALES


# TransformMatchingTex como el mismo nombre del comando lo implica, une el texto y se aprecia muy elegante, solo que hay que ver si la transformación la hace “ahí mismo” en el mismo renglón o en el renglón de abajo. Todo depende de la estética. Que también se pueden utilizar los otros comandos (para manipular ecuaciones, que son:FadeTransform ) que emplee en esta animación, de nuevo, depende de qué tan satisfecho estás con la animación.


"""

ERRORES DE LOS CUALES ME PERCATÉ QUE COMETÍ EN ESTE VIDEO.

Me percaté de que con el exponente dos, a cada momento decía, esto al CUADRADO, aquello al CUADRADO y fue lo palabra que más dije. Debo “campechanear” en esos casos, el exponente DOS , elevar al CUADRADO; el exponente TRES, elevar al CUBO y así sucesivamente. 

Dejaste en promedio 17 segundos para hablar, NO FUERON SUFICIENTES, mejor deja treinta, más vale a que sobre a que falte (en Manim). 

FIJATE CUALES SON LAS SOLUCIONES QUE SATISFACEN LA ECUACIÓN, HAS BIEN TU TAREA. SI TU FUENTE DEL EJERCICIO ES mindyourdecisions, VE COMPLETO EL VIDEO.

Enlace al video en YouTube: https://www.youtube.com/watch?v=hFUY_rK4k3E

"""