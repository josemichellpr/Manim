#De acuerdo voy a poner el código por escenas, tengamos presente que Python es muy mamón con el indentado, ni te pases, ni lo omitas. Bueno, a lo que voy  en cuanto a que voy por escenas es que voy renderizando una escena a la vez. En vez de todas de un sopetón. Conforme a tengo mis escenas en mi editor de video es como las voy a poner aquí. A efecto de que quiera hacerlo más escalable en cualquier momento.


from manim import *
 
class p1(Scene):
    def construct(self):
        #ESCENA 1
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =30
            )# Mi pequeña marca de agua
        play = self.play
        wait = self.wait
        add = self.add
        #Las tres líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
        d= Dot([1.5,0,0])# Un puntito para ubicarnos mejor y acomodar un texto que se pone abajo del punto.
        line00 = Line([0,0,0],[1.5,0,0])#Declaramos las líneas, teniendo en cuenta (obviamente) a nuestro sistema de coordenadas o plano cartesiano.
        line0 = Line([1.5,0,0],[3,0,0])
        line1 = Line([3,0,0],[1.5,2.6,0])
        line2 = Line([1.5,2.6,0],[0,0,0])  
        line3 = Line([1.5,2.6,0],[1.5,0,0])
     
        a = Arc(0.5, 120*DEGREES, 60*DEGREES,arc_center=[3,0,0],color=RED) #Mucho OJO porque este arco es una chingonería. El primer argumento es el radio del arco, el segundo es desde donde comienza a trazar el arco, el tercero es el arco propiamente que tiene 60°, el cuarto es el centro o el origen del arco, el quinto es el color, obviamente. 
        theta = MathTex(r"\theta ")\
            .scale(0.6).next_to(a,(1/6)*UP + (1/3)*LEFT)
        text1 = MathTex("l = 1").next_to(d,DOWN)#Te declaro l = 1, y lo pondrás debajo de “d”, (el punto).
        text2 = MathTex("l = 1").next_to(line1,RIGHT)
        text3 = MathTex("l = 1").next_to(line2,LEFT)
        grp = Group(line00,line0, line1,line2,text1,text2,text3,line3,a,theta,d)#Este comando es super chingón porque nos permite mover, girar a TODO lo que está dentro del grupo, como si fuera uno solo.
       
        play(seven_line.animate.to_corner(UR))
       
        play(Create(line00))
        play(Create(line0))
        play(Create(line1))
        play(Create(line2))
        play(Create(line3))
        add(d)
        play(FadeIn(text1),FadeIn(text2),FadeIn(text3))
        play(Write(a))
        play(Write(theta))
       
        play(grp.animate.move_to(
           ORIGIN
        ))# Aquí le estamos ordenando que el triángulo y la línea y todo lo que está dentro de “grp” .Se vayan al ORIGEN de la pantalla.


       
        self.wait(1)
       
        play(grp.animate.move_to(
            UP +
            LEFT*4
        ))
        play(FadeOut(line00),FadeOut(line2),FadeOut(text1),FadeOut(text2),FadeOut(text3))#Vas a desaparecer todo lo que está en los paréntesis. AL MISMO TIEMPO.
   
        wait(1)


        hip =MathTex("HIP = 1").next_to(line1, RIGHT)
        c_o = MathTex("C.O=?").next_to(line3, LEFT)
        c_a = MathTex("C.A=0.5").next_to(line0, DOWN)
        c_o1 = MathTex("C.O = {\\sqrt{3}\\over{2}}").next_to(line3, LEFT)
        play(Write(hip),Write(c_o),Write(c_a))


        t1 = MathTex("HIP^2","=","C.O^2","+","C.A^2")\
            .scale(0.80)
        play(t1.animate.move_to(
            UP*2 +
            RIGHT*3
        ))
        t2 = MathTex("C.O^2","=","HIP^2","-","C.A^2")\
            .scale(0.80).next_to(t1,DOWN)


       
        t21 = MathTex("C.O = \\sqrt{HIP^2 - C.A^2}")\
            .scale(0.80).next_to(t2,DOWN)
       
        play(Write(t2))
        play(Write(t21))
        wait(3)
        t3 =  MathTex("C.O = \\sqrt{1^2 - 0.5^2}")\
            .scale(0.80).next_to(t21,DOWN)
        t4 =  MathTex("C.O = \\sqrt{0.75}")\
            .scale(0.80).next_to(t3,DOWN)
        t5 = MathTex("C.O = {\\sqrt{3}\\over{2}}")\
            .scale(0.8).next_to(t4, DOWN)
        play(Write(t3))
        play(Write(t4))
        play(Write(t5))
        wait(2)
        play(FadeOut(c_o))
        play(FadeIn(c_o1))
        wait(1)
        sin = MathTex("sin(\\theta)={C.O\\over HIP} =")\
            .scale(0.9)
        sqrt = MathTex("\\sqrt{3}\\over{2}")\
            .scale(0.9).next_to(sin, RIGHT)
       
        grp2 = Group(sin,sqrt).next_to(ORIGIN, 4*DOWN + LEFT)#Hice el grupo porque estaba batallando mucho para poner las raíces. Entonces decidí declarar dos expresiones, las pongo una a lado de otra. Después los vuelvo una sola con “grp2”.
       
        play(FadeIn(grp2))
        wait(1)


        #Vamos a crear el sombreado


        framebox0 = SurroundingRectangle(c_o1,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “c_o1”
        self.play(
        Create(framebox0), #Ejecute el perímetro que te declare anteriormente
                )
        framebox1 = SurroundingRectangle(hip,buff = .1)
        self.play(
        Create(framebox1), #Ejecute el perímetro que te declare anteriormente
                )
       
        framebox2 = SurroundingRectangle(grp2,buff = .1)
        self.play(
        Create(framebox2), #Ejecute el perímetro que te declare anteriormente
                )
           
        wait(2)
        play(FadeOut(framebox0),FadeOut(framebox1),FadeOut(framebox2))
        play(FadeOut(grp2))
       
        #SIGUIENTE SOMBREADO
        cos = MathTex("cos(\\theta)={C.A\\over HIP} =")\
            .scale(0.9)
        sqrt1 = MathTex("{0.5\\over 1}","=","{1\\over 2}")\
            .scale(0.9).next_to(cos, RIGHT)
            #Aguas con dejar espacio entre \\ y over. Lo correcto es SIN ESPACIO.
        grp3 = Group(cos,sqrt1).next_to(ORIGIN, 4*DOWN + 2*LEFT)
        play(FadeIn(grp3))


        framebox01 = SurroundingRectangle(c_a,buff = .1)
        self.play(
        Create(framebox01), #Ejecute el perímetro que te declare anteriormente
                )
        framebox11 = SurroundingRectangle(hip,buff = .1)
        self.play(
        Create(framebox11), #Ejecute el perímetro que te declare anteriormente
                )
       
        framebox21 = SurroundingRectangle(grp3,buff = .1)
        self.play(
        Create(framebox21), #Ejecute el perímetro que te declare anteriormente
                )
           
       
        wait(2)
        play(FadeOut(framebox01),FadeOut(framebox11),FadeOut(framebox21))
        play(FadeOut(grp3))


        #SIGUIENTE SOMBREADO
        tan = MathTex("tan(\\theta)={C.O\\over C.A} =")\
            .scale(0.9)
        sqrt2 = MathTex("\\sqrt{3}")\
            .scale(0.9).next_to(tan, RIGHT)
       
        grp4 = Group(tan,sqrt2).next_to(c_a, 1.5*DOWN)
        play(FadeIn(grp4))


        framebox011 = SurroundingRectangle(c_o1,buff = .1)
        self.play(
        Create(framebox011), #Ejecute el perímetro que te declare anteriormente
                )
        framebox111 = SurroundingRectangle(c_a,buff = .1)
        self.play(
        Create(framebox111), #Ejecute el perímetro que te declare anteriormente
                )
       
        framebox211 = SurroundingRectangle(grp4,buff = .1)
        self.play(
        Create(framebox211), #Ejecute el perímetro que te declare anteriormente
                )
           
       
        wait(2)
        play(FadeOut(framebox011),FadeOut(framebox111),FadeOut(framebox211))
        play(FadeOut(grp4))


        wait(3)


         # manim -pql scene5.py p1




         # sqrt2 = MathTex("{{2\\sqrt{3}}\\over 2}")\
            #.scale(0.9).next_to(tan, RIGHT) # Interesante porque vuelve todo la cantidad fraccionaria con un radical.


#SEGUNDA ESCENA


from manim import *
 
class p2(Scene):
    def construct(self):
#Pongo las 3 líneas de arriba porque recordemos que las escenas se hacen por separado. Ya las he juntado en el editor de video. 


        #ESCENA 2
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add
        #Las dos líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =32
            ).next_to(ORIGIN, 9*DOWN + RIGHT)
        l0 = Text("Antes de continuar con la verificación en calculadora ...",font_size =34).next_to(ORIGIN, 9*UP) #
        l1 = MarkupText(
            f'PREGUNTA: ¿CUÁL ES EL VALOR DE  <span fgcolor="{YELLOW}">THETA</span>?', color=WHITE, font_size =34).next_to(l0,DOWN)
        l2 = Text("Te reto a que pauses el video y lo investigues.", font_size = 34).next_to(l1,DOWN)
       
        l3 = MarkupText(
            f'<span fgcolor="{RED}">PISTA: </span> ¿Cómo se llama el triángulo en el que todos sus lados son iguales?', color=WHITE, font_size =30).next_to(l2,DOWN)
       
        self.play(Write(seven_line))
        self.play(Write(l0))
        self.wait()
        self.play(Write(l1))
        self.play(Write(l2))
        self.wait(2)
        self.play(Write(l3))
   
        self.wait(3)


       # manim -pql scene5.py p2



#TERCERA ESCENA → Son las verificaciones en WOLFRAM

#CUARTA ESCENA
from manim import *
 
class p3(Scene):
    def construct(self):
        #ESCENA 4
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add
        #Las dos líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =32
            ).next_to(ORIGIN, 8*DOWN + RIGHT)
        l0 = Text("RESPUESTA ",font_size =40).next_to(ORIGIN, 9*UP) # CON ESTOS COMANDOS LOGRAMOS QUE "lingotes" SEA AMARILLO, HACIENDO ALUSIÓN A QUE EL LINGOTE ES DE ORO.
        l1 = MarkupText(
            f'Hemos elegido un triángulo  <span fgcolor="{YELLOW}">equilátero</span>, porque cualquiera ', color=WHITE, font_size =36).next_to(l0,3*DOWN)
        l2 = Text("de sus ángulos interiores es igual a 60°.", font_size = 36).next_to(l1,DOWN)
       
       
       
        self.play(Write(seven_line))
        self.play(Write(l0))
        self.wait()
        self.play(Write(l1))
        self.play(Write(l2))
       
        self.wait(2)
       
   
        self.wait(3)


       # manim -pql scene5.py p3


"""
¿Sabes qué me dio problemas en este código y me retrasó un par de horas? HACER UNA ESCALA. 
Al principio estaba bien emocionado de que la escala se veía muy pro, porque al aprendiente le permitía ver mejor, sin esforzarse la vista. Pero cuando quise poner texto al lado de la figura con la escala ya aplicada, fue un dolor de cabeza. Concluí en que era mejor QUITAR LA ESCALA.  
Espero dominar más MANIM, para ver cómo solucionar el problema. Pero ME GUSTO BASTANTE EL VIDEO YA TERMINADO. 

"""

#QUINTA ESCENA
#”Para ejercicios y notas, ve a la descripción del video.”

#Enlace al video en YouTube: https://www.youtube.com/watch?v=A1gkEYgjHfE