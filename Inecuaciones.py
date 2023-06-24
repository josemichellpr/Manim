from manim import *
class p1i(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.


        play(seven_line.animate.to_corner(UR))
       
        eq = MathTex("x-5<2x-6")\
            .scale(1.35).next_to(ORIGIN,UP*8)
       


        line_1= Text("Sumamos 5 a la inecuación (abajo).",font="Comic Sans MS")\
            .scale(0.7).next_to(eq,DOWN*1.5)# OJO cómo se pone el tipo de FUENTE


        line_1.set_color(TEAL) #Aquí le ponemos COLOR  a todo el texto de su respectivo.
 
        eq1 = MathTex("x<2x-1")\
            .scale(1.25).next_to(line_1,DOWN)


        line_2= Text("Restamos 2x.",font="Comic Sans MS")\
            .scale(0.7).next_to(eq1,DOWN*1.5)# OJO cómo se pone el tipo de FUENTE


        line_2.set_color(TEAL)#Aquí le ponemos COLOR  a todo el texto de su respectivo.
 
        eq2 = MathTex("-x<-1")\
            .scale(1.25).next_to(line_2,DOWN)


        line_3= Text("Multiplicamos por -1 la inecuación y la desigualdad cambia de signo.",font="Comic Sans MS")\
            .scale(0.6).next_to(eq2,DOWN*1.5)


        line_3.set_color(TEAL)#Aquí le ponemos COLOR  a todo el texto de su respectivo.
 
        eq3 = MathTex("x>1")\
            .scale(1.35).next_to(line_3,DOWN)


        framebox0 = SurroundingRectangle(eq,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “eq”
       
       
        play(Write(
            eq),
        run_time = 3
        )
        play(Create(
            framebox0),
            run_time=2
            ) #Ejecute el perímetro que te declare anteriormente


        play(FadeOut(framebox0))
 
        play(Write(
            line_1
        ),
        run_time=2
        )


        wait(1)
 
        play(Write(
            eq1
        ),
        run_time=1
        )
 
        play(Write(
            line_2),
        run_time = 2
        )


        wait(1)
 
        play(Write(
            eq2),
        run_time = 1
        )


        play(Write(
            line_3),
        run_time = 2
        )


        wait(1)


        play(Write(
            eq3),
        run_time = 1
        )
       
        wait(3)
 
        # manim -pqh projectinec.py p1i




class p1plot(Scene):
    def construct(self):
        # Vamos a pedirle a Manim que haga una RECTA NUMÉRICA
        l0 = NumberLine(
            x_range=[0, 11, 1],
            length=12, #Este comando es para que tan ancha será la RECTA NUMÉRICA
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )


        line_1= Text("Visualización en la recta numérica")\
            .scale(0.8).next_to(ORIGIN,4*UP)
       




        dot_at_1 = Dot(l0.n2p(1),color=YELLOW)#Declaramos un punto en el objeto número uno de la recta numérica (comenzamos a contar desde el cero).
       
        A= Arrow(dot_at_1,7*RIGHT)#Declaramos una flecha para que exprese el sentido de los valores que puede tomar la inecuación.


        self.play(Write(line_1))
        self.play(Create(l0),run_time=3)
        self.play(Create(dot_at_1))
        self.play(Create(A),run_time=2)


        self.wait(2)


        #manim -pqh projectinec.py p1plot


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


        play(seven_line.animate.to_corner(UR))#Lleva mi marca a la esquina derecha
       
        eq = MathTex("5x-12>3x-4")\
            .scale(1.35).next_to(ORIGIN,UP*8)
       
        line_1= Text("Sumamos 12 a la inecuación (abajo).",font="Comic Sans MS")\
            .scale(0.7).next_to(eq,DOWN*1.5)# OJO cómo se pone el tipo de FUENTE


        line_1.set_color(TEAL)#Aquí le ponemos COLOR  a todo el texto de su respectivo.
 
        eq1 = MathTex("5x>3x+8")\
            .scale(1.25).next_to(line_1,DOWN)


        line_2= Text("Restamos 3x.",font="Comic Sans MS")\
            .scale(0.7).next_to(eq1,DOWN*1.5)# OJO cómo se pone el tipo de FUENTE


        line_2.set_color(TEAL)#Aquí le ponemos COLOR  a todo el texto de su respectivo.
 
        eq2 = MathTex("2x>8")\
            .scale(1.25).next_to(line_2,DOWN)


        line_3= Text("Dividimos la inecuación por 2 o multiplicamos por 1/2 (es lo mismo).",font="Comic Sans MS")\
            .scale(0.6).next_to(eq2,DOWN*1.5)# OJO cómo se pone el tipo de FUENTE


        line_3.set_color(TEAL)#Aquí le ponemos COLOR  a todo el texto de su respectivo.
 
        eq3 = MathTex("x>4")\
            .scale(1.35).next_to(line_3,DOWN)


        framebox0 = SurroundingRectangle(eq,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “eqz18”
       
       
        play(Write(
            eq),
        run_time = 3
        )
        play(Create(
            framebox0),
            run_time=2
            ) #Ejecute el perímetro que te declare anteriormente


        play(FadeOut(framebox0))
 
        play(Write(
            line_1
        ),
        run_time=2
        )


        wait(1)
 
        play(Write(
            eq1
        ),
        run_time=1
        )
 
        play(Write(
            line_2),
        run_time = 2
        )


        wait(1)
 
        play(Write(
            eq2),
        run_time = 1
        )


        play(Write(
            line_3),
        run_time = 2
        )


        wait(1)


        play(Write(
            eq3),
        run_time = 1
        )
       
        wait(3)
 
        # manim -pqh projectinec.py p2ii


class p2plot(Scene):
    def construct(self):
        # Vamos a pedirle a Manim que haga una RECTA NUMÉRICA
        l0 = NumberLine(
            x_range=[0, 11, 1],
            length=12,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )


        line_1= Text("Visualización en la recta numérica")\
            .scale(0.8).next_to(ORIGIN,4*UP)
       


        dot_at_4 = Dot(l0.n2p(4),color=YELLOW)
        #dot_at_1_UP=
        A= Arrow(dot_at_4,7*RIGHT)


        self.play(FadeIn(line_1))
        self.play(Create(l0),run_time=3)
        self.play(Create(dot_at_4))
        self.play(Create(A),run_time=2)


        self.wait(2)


        #manim -pqh projectinec.py p2plot


class p3ii(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.


       
       
        eq = MathTex("2x","-\\frac{5}{3}",">","\\frac{x}{3}","+10")\
            .scale(1).next_to(ORIGIN,UP*8)
       
        line_1= Text("Restamos x/3 a la inecuación y al mismo tiempo sumamos 5/3.",font="Comic Sans MS")\
            .scale(0.6).next_to(eq,DOWN*1.5)# OJO cómo se pone el tipo de FUENTE


        line_1.set_color(TEAL)#Aquí le ponemos COLOR  a todo el texto de su respectivo.
 
        eq1 = MathTex("2x","-\\frac{x}{3}",">","\\frac{5}{3}","+10")\
            .scale(1).next_to(line_1,DOWN*0.5)


        line_2= Text("Simplificamos hasta las mínimas expresiones.",font="Comic Sans MS")\
            .scale(0.7).next_to(eq1,DOWN*1)# OJO cómo se pone el tipo de FUENTE


        line_2.set_color(TEAL)#Aquí le ponemos COLOR  a todo el texto de su respectivo.
 
        eq2 = MathTex("\\frac{5x}{3}",">","\\frac{35}{3}")\
            .scale(1).next_to(line_2,DOWN*0.5)


        line_3= Text("Multiplicamos por 3/5 la inecuación.",font="Comic Sans MS")\
            .scale(0.6).next_to(eq2,DOWN*1)# OJO cómo se pone el tipo de FUENTE


        line_3.set_color(TEAL)#Aquí le ponemos COLOR  a todo el texto de su respectivo.
 
        eq3 = MathTex("x>7")\
            .scale(1).next_to(line_3,DOWN*0.5)

        framebox0 = SurroundingRectangle(eq,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “eqz18”
       
       
        play(Write(
            eq),
        run_time = 3
        )
        play(Create(
            framebox0),
            run_time=2
            ) #Ejecute el perímetro que te declare anteriormente


        play(FadeOut(framebox0))
 
        play(Write(
            line_1
        ),
        run_time=2
        )


        wait(1)
 
        play(Write(
            eq1
        ),
        run_time=2
        )
 
        play(Write(
            line_2),
        run_time = 2
        )


        wait(1)
 
        play(Write(
            eq2),
        run_time = 3
        )


        play(Write(
            line_3),
        run_time = 3
        )


        wait(1)


        play(Write(
            eq3),
        run_time = 3
        )
       
        wait(3)
 
        # manim -pqh projectinec.py p3ii


class p3plot(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range=[0, 11, 1],
            length=12,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )


        line_1= Text("Visualización en la recta numérica")\
            .scale(0.8).next_to(ORIGIN,4*UP)
       


        dot_at_7 = Dot(l0.n2p(7),color=YELLOW)
        #dot_at_1_UP=
        A= Arrow(dot_at_7,7*RIGHT)


        self.play(FadeIn(line_1))
        self.play(Create(l0),run_time=3)
        self.play(Create(dot_at_7))
        self.play(Create(A),run_time=2)


        self.wait(2)


        #manim -pqh projectinec.py p3plot


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
  
        eq = MathTex("(x-1)^2","-7",">","(x-2)^2")\
            .scale(1.35).next_to(ORIGIN,UP*8)
       
        line_1= Text("Extenderemos ambos lados de la inecuación.",font="Comic Sans MS")\
            .scale(0.7).next_to(eq,DOWN*1.5)
        line_1.set_color(TEAL)
 
        eq1 = MathTex("x^2-2x+1-7",">","x^2-4x+4")\
            .scale(1).next_to(line_1,DOWN)


        line_2= Text("Restamos el término cuadrático (x^2).",font="Comic Sans MS")\
            .scale(0.7).next_to(eq1,DOWN*1.5)
        line_2.set_color(TEAL)
 
        eq2 = MathTex("-2x-6",">","-4x+4")\
            .scale(1).next_to(line_2,DOWN)


        line_3= Text("Manipulamos la inecuación como en los ejemplos anteriores y nos resulta:",font="Comic Sans MS")\
            .scale(0.6).next_to(eq2,DOWN*1.5)
        line_3.set_color(TEAL)
 
        eq3 = MathTex("x>5")\
            .scale(1.35).next_to(line_3,DOWN)


        framebox0 = SurroundingRectangle(eq,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “eqz18”
       
       
        play(Write(
            eq),
        run_time = 3
        )
        play(Create(
            framebox0),
            run_time=2
            ) #Ejecute el perímetro que te declare anteriormente


        play(FadeOut(framebox0))
 
        play(Write(
            line_1
        ),
        run_time=2
        )


        wait(1)
 
        play(Write(
            eq1
        ),
        run_time=2
        )
 
        play(Write(
            line_2),
        run_time = 2
        )


        wait(1)
 
        play(Write(
            eq2),
        run_time = 3
        )


        play(Write(
            line_3),
        run_time = 3
        )


        wait(1)


        play(Write(
            eq3),
        run_time = 3
        )
       
        wait(3)
 
        # manim -pqh projectinec.py p4i


class p4plot(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range=[0, 11, 1],
            length=12,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )


        line_1= Text("Visualización en la recta numérica")\
            .scale(0.8).next_to(ORIGIN,4*UP)
       


        dot_at_5 = Dot(l0.n2p(5),color=YELLOW)
        #dot_at_1_UP=
        A= Arrow(dot_at_5,7*RIGHT)


        self.play(FadeIn(line_1))
        self.play(Create(l0),run_time=3)
        self.play(Create(dot_at_5))
        self.play(Create(A),run_time=2)


        self.wait(2)


        #manim -pqh projectinec.py p4plot


class p5iii(Scene):
    def construct(self):
        #Esto es un bosquejo -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =20
            )
       
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
  
       
        eq = MathTex("\\frac{x+3}{3}","-\\frac{4}{x+2}",">","\\frac{x}{3}")\
            .scale(1).next_to(ORIGIN,UP*8)
       
        line_1= Text("Multiplicamos por 3 a la inecuación.",font="Comic Sans MS")\
            .scale(0.6).next_to(eq,DOWN*1.5)
        line_1.set_color(TEAL)
 
        eq1 = MathTex("x+3","-\\frac{12}{x+2}",">","x")\
            .scale(1).next_to(line_1,DOWN)


        line_2= Text("Restamos x+3 ( o sumamos -x-3).",font="Comic Sans MS")\
            .scale(0.6).next_to(eq1,DOWN*1.5)
        line_2.set_color(TEAL)
 
        eq2 = MathTex("-\\frac{12}{x+2}",">","-3")\
            .scale(1).next_to(line_2,DOWN)


        grp = Group(line_2,eq2)
        #En la línea de arriba, declaramos un grupo para posteriormente poder girarlo en el próximo comando.


        line_3= Text("Invertimos ambos miembros y la inecuación cambia de signo:",font="Comic Sans MS")\
            .scale(0.6).next_to(ORIGIN,UP*4)
        line_3.set_color(TEAL)
 
        eq3 = MathTex("\\frac{x+2}{-12}","<","-\\frac{1}{3}")\
            .scale(1).next_to(line_3,DOWN)


        line_4 = Text("Multiplicamos por -12 y se cambia de nuevo el signo.",font="Comic Sans MS")\
            .scale(0.5).next_to(eq3,DOWN*1.5)
        line_4.set_color(TEAL)


        eq4 = MathTex("x+2>4")\
            .scale(1).next_to(line_4,DOWN)


        line_5 =Text("Finalizamos con la siguiente inecuación:",font="Comic Sans MS")\
            .scale(0.5).next_to(eq4,DOWN*1.5)
        line_5.set_color(TEAL)


        eq5 = MathTex("x>2")\
            .scale(1).next_to(line_5,DOWN)


        framebox0 = SurroundingRectangle(eq,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “eqz18”
       
        play(seven_line.animate.to_corner(UR))


        play(Write(
            eq),
        run_time = 3
        )
        play(Create(
            framebox0),
            run_time=2
            ) #Ejecute el perímetro que te declare anteriormente


        play(FadeOut(framebox0))
 
        play(Write(
            line_1
        ),
        run_time=2
        )


        wait(1)
 
        play(Write(
            eq1
        ),
        run_time=2
        )
 
        play(Write(
            line_2),
        run_time = 2
        )


        wait(1)
 
        play(Write(
            eq2),
        run_time = 3
        )


        #Desde aquí comienza una maniobra chingona para que se vea más pro que con una simple presentación en Power Point
        play(FadeOut(eq),FadeOut(line_1),FadeOut(eq1))


       #Declaramos un grupo para que los podamos mover. Fíjate cómo lo movemos a "eq". Es decir a la posición de "eq". Es genial.
        play(grp.animate.move_to(
            eq
        ))


        play(Write(
            line_3),
        run_time = 3
        )


        wait(1)


        play(Write(
            eq3),
        run_time = 3
        )


        play(Write(
            line_4),
        run_time = 3
        )


        wait(1)


        play(Write(
            eq4),
        run_time = 3
        )


        play(Write(
            line_5),
        run_time = 3
        )


        wait(1)


        play(Write(
            eq5),
        run_time = 3
        )
       
        wait(3)
 
        # manim -pqh projectinec.py p5iii




class p5plot(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range=[0, 11, 1],
            length=12,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )


        line_1= Text("Visualización en la recta numérica")\
            .scale(0.8).next_to(ORIGIN,4*UP)
       


        dot_at_2 = Dot(l0.n2p(2),color=YELLOW)
        #dot_at_1_UP=
        A= Arrow(dot_at_2,7*RIGHT)


        self.play(FadeIn(line_1))
        self.play(Create(l0),run_time=3)
        self.play(Create(dot_at_2))
        self.play(Create(A),run_time=2)


        self.wait(2)


        #No va a a aparecer en el video, por problemática la numberline.


        #manim -pql projectinec.py p5plot


class intro(Scene):
    def construct(self):
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', font_size =20
            )
        seven_line.to_corner(UR)# Este solo me funcionó cuando es IMAGEN (no VIDEO)
        # (Abajo) Vamos a declarar las ecuaciones que queremos que Manim "pinte" en la pantalla
        eq = MathTex("x-5<2x-6")
        eq1 = MathTex("5x-12>3x-4")
        eq2 = MathTex("2x","-\\frac{5}{3}",">","\\frac{x}{3}","+10")
        eq3 = MathTex("(x-1)^2","-7",">","(x-2)^2")
        eq4 = MathTex("\\frac{x+3}{3}","-\\frac{4}{x+2}",">","\\frac{x}{3}")


        eqgroup = Group(eq,eq1,eq2,eq3,eq4).arrange(DOWN*0.5, buff=1) #Un grupo para que Manim automáticamente las acomode a cómo uno se lo diga.
        self.add(seven_line) #El comando "add" es para que solamente pinte en pantalla como IMAGEN.
        self.add(eqgroup)

        #manim -pqh projectinec.py intro

        #08 de septiembre de 2022


        #Algunas escenas tienen por ejemplo p5i- Porque a veces Manim, sin razón alguna aparente, NO QUIERE ejecutar los nuevos arreglos que hiciste a un código. Para no estar peleando, lo que hacemos es cambiar ligeramente el nombre a la escena. Por eso aparecen esos carácteres extras.


        #Lo que voy a ADOPTAR es que voy a mover la primera expresión matemático hasta arriba con el metodo toedge (UP), o algo así y pongo mi marca en tamaño veinte. Y así se agrega una nueva "capa" de seguridad a mi trabajo.

        # Enlace al video en YouTube: https://www.youtube.com/watch?v=GpcsGpoo0ew

