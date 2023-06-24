
 #De acuerdo voy a poner el código por escenas, tengamos presente que Python es muy mamón con el indentado, ni te pases, ni lo omitas. Bueno, a lo que voy  en cuanto a que voy por escenas es que voy renderizando una escena a la vez. En vez de todas de un sopetón. Conforme a tengo mis escenas en mi editor de video es como las voy a poner aquí. A efecto de que quiera hacerlo más escalable en cualquier momento.


from manim import *
 
class hola(Scene):
    def construct(self):
        #ESCENA 1
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =30
            )
        play = self.play 
        wait = self.wait
        add = self.add
        #Las tres líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       
        line0 = Line([0,0,0],[2,0,0])#Declaramos las líneas, teniendo en cuenta (obviamente) a nuestro sistema de coordenadas o plano cartesiano.
        line1 = Line([2,0,0],[2,2,0])
        l1 = MathTex("l = 1").next_to(line0,DOWN)#Te declaro l = 1, y lo pondrás debajo de line0
        l2 = MathTex("l = 1").next_to(line1,RIGHT)
        line2 = Line([2,2,0],[0,2,0])
        line3 = Line([0,2,0],[0,0,0])
        line4 = Line([2,2,0],[0,0,0])
       #Voy a declarar las líneas que conformarán el ángulo
        line6 = Line([0.25,0,0],[0.25,0.25,0])
        line7 = Line([0.25,0.25,0],[0,0.25,0])
        theta = MathTex(r"\theta ")\
            .scale(0.7).next_to(line0,UP)
        grp = Group(line0,line1,line2,line3,line4,line6,line7,theta,l1,l2)#Este comando es super chingón porque nos permite mover, girar a TODO lo que está dentro del grupo, como si fuera uno solo.
        play(seven_line.animate.to_corner(UR))
        play(Create(line0))
        play(Create(line1))
        play(Create(line2))
        play(Create(line3))
        play(FadeIn(l1),FadeIn(l2))
        play(Create(line4))
        play(FadeIn(line6),FadeIn(line7))
        play(Create(theta))
       
       
        play(grp.animate.move_to(
            UP*2 +
            LEFT*3
        ))# Aquí le estamos ordenando que el cuadrado y la línea (que ahora son uno SOLO) que se vayan UPER- LEFT (UL) de la pantalla.
        #NO HE PODIDO HACER LA PUTA COPIA, VOY A DECIRLE QUE LO HAGA DE NUEVO.
       
        play(FadeOut(line2), FadeOut(line3),FadeOut(line7),FadeOut(l1),FadeOut(l2))#Vas a desaparecer todo lo que está en los paréntesis. AL MISMO TIEMPO.
        hip =MathTex("HIP = ?").next_to(line4, LEFT)
        c_o = MathTex("C.O=1").next_to(line1, RIGHT)
        c_a = MathTex("C.A=1").next_to(line0, DOWN)
        play(Write(hip),Write(c_o),Write(c_a))
        wait(2)#Te esperas 2 segundos
        t1 = MathTex("HIP^2","=","C.O^2","+","C.A^2")\
            .scale(0.80)
        play(t1.animate.move_to(
            UP*2 +
            RIGHT*4
        ))
        t2 =  MathTex("HIP = \\sqrt{C.O^2 + C.A^2}")\
            .scale(0.80).next_to(t1,DOWN)
       
        play(Write(t2))
        wait(2)
        t3 =  MathTex("HIP = \\sqrt{1^2 + 1^2}")\
            .scale(0.80).next_to(t2,DOWN)
        t4 =  MathTex("HIP = \\sqrt{2}")\
            .scale(0.80).next_to(t3,DOWN)
        play(Write(t3))
        play(Write(t4))
        wait(3)
        sin = MathTex("sin(\\theta)={C.O\\over HIP} =")\
            .scale(0.8)
        sqrt = MathTex("\\frac{1}{\\sqrt{2}},  ")\
            .scale(0.8).next_to(sin, RIGHT)
        grp2 = Group(sin,sqrt) #Hice el grupo porque estaba batallando mucho para poner las raíces. Entonces decidí declarar dos expresiones, las pongo una a lado de otra. Después los vuelvo una sola con “grp2”.
       
        play(grp2.animate.move_to(
            1.5*DOWN +
            LEFT*5
        ))
        wait()
        framebox1 = SurroundingRectangle(grp2, buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “grp2”
        self.play(
        Create(framebox1), #Ejecute el perímetro que te declare anteriormente
                )
        wait()
        play(FadeOut(framebox1))#Desaparece


        cos = MathTex("cos(\\theta)={C.A\\over HIP} =")\
            .scale(0.8)
        sqrt1 = MathTex("\\frac{1}{\\sqrt{2}},")\
            .scale(0.8).next_to(cos, RIGHT)
        grp2 = Group(cos,sqrt1)
       
        play(grp2.animate.move_to(
            1.5*DOWN +
            LEFT
        ))
        wait()
        framebox2 = SurroundingRectangle(grp2, buff = .1)
        self.play(
        Create(framebox2), #Ejecute el perímetro que te declare anteriormente
                )
        wait()
        play(FadeOut(framebox2))


        tan = MathTex("tan(\\theta)={C.O\\over C.A} =")\
            .scale(0.8)
        sqrt2 = MathTex("\\frac{1}{1}}")\
            .scale(0.8).next_to(tan, RIGHT)
        grp3 = Group(tan,sqrt2)
       
        play(grp3.animate.move_to(
            1.5*DOWN +
            3*RIGHT
        ))
        framebox3 = SurroundingRectangle(grp3, buff = .1)
        self.play(
        Create(framebox3), #Ejecute el perímetro que te declare anteriormente
                )
        wait()
        play(FadeOut(framebox3))
        wait(3)
       
   
        # manim -pql scene4.py hola


#ESCENA 2 
from manim import *
 
class hola(Scene):
    def construct(self):
 #Pongo las 3 líneas de arriba porque recordemos que las escenas se hacen por separado. Ya las he juntado en el editor de video. 


#ESCENA 2
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =32
            ).next_to(ORIGIN, 9*DOWN + RIGHT)
        l0 = Text("Antes de continuar con la verificación en calculadora ...",font_size =34).next_to(ORIGIN, 9*UP) 


        l1 = MarkupText(
            f'PREGUNTA: ¿CUÁL ES EL VALOR DE  <span fgcolor="{YELLOW}">THETA</span>?', color=WHITE, font_size =34).next_to(l0,DOWN)
        l2 = Text("Te reto a que pauses el video y lo investigues.", font_size = 34).next_to(l1,DOWN)
       
        l3 = MarkupText(
            f'<span fgcolor="{RED}">PISTA: </span> ¿Cuántos grados tiene el ÁNGULO RECTO?', color=WHITE, font_size =34).next_to(l2,DOWN)
       
        self.play(Write(seven_line))
        self.play(Write(l0))
        self.wait()
        self.play(Write(l1))
        self.play(Write(l2))
        self.wait(2)
        self.play(Write(l3))
   
        self.wait(3)

#ESCENA 3
#Aparece la verificación en calculadora.

#ESCENA 4
#”Para ejercicios y notas, ve a la descripción del video.”

#Enlace al video en YouTube: https://www.youtube.com/watch?v=WBecdA1nT8o