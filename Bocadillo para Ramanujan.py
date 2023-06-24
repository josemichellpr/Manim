from manim import *
class p2i(Scene):
    def construct(self):
        # -- PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       # A continuación la primera ecuación del sistema de ec.
        eq1 =MathTex("x","+","\\sqrt{y}","=","11")\
            .scale(2).next_to(ORIGIN,5*UP)
#A continuación la segunda ecuación del sistema de ec.
        eq2 = MathTex("\\sqrt{x}","+","y","=","7")\
            .scale(2).next_to(eq1,DOWN)
#(abajo) el uno para identificar a la primera ecuación
        uno = MarkupText(
            f' <span fgcolor="{YELLOW}">(1)</span>', font_size = 45
            ).next_to(eq1,RIGHT)
        dos = MarkupText(
            f' <span fgcolor="{YELLOW}">(2)</span>', font_size = 45
            ).next_to(eq2,RIGHT)
        p1 = Text(" Vamos a despejar x de (2)",font_size =34).next_to(eq2,DOWN)
# “eq22” es el primer despeje que aparece en el video y la primera escena.
        eq22 = MathTex("\\sqrt{x}","=","7","-","y")\
            .scale(1.4).next_to(p1,DOWN)
# “eq222” es el segundo despeje que aparece en el video y la primera escena.
        eq222 =  MathTex("x","=","(7-y)^2","=","y^2","-14y","+49")\
            .scale(1.4).next_to(eq22,DOWN)
       
        play(seven_line.animate.to_corner(UR))
        play(Write(eq1))
        play(FadeIn(uno))
        play(Write(eq2))
        play(FadeIn(dos))
        wait(2)
        play(Write(p1))
        wait(2)
        play(FadeOut(dos))
# TransformMatchingTex como el mismo nombre del comando lo implica, une el texto y se aprecia muy elegante, solo que hay que ver si la transformación la hace “ahí mismo” en el mismo renglón o en el renglón de abajo. Todo depende de la estética. Que también se pueden utilizar los otros comandos (para manipular ecuaciones, que son:FadeTransform ) que emplee en esta animación, de nuevo, depende de qué tan satisfecho estás con la animación.
        play(TransformMatchingTex(
            eq2,eq22
        ),
        run_time=3
        )
        play(Write(eq222))
        wait(3)
 
        # manim -pql scene7.py p2i



#SEGUNDA ESCENA

from manim import *
class p3ii(Scene):
    def construct(self):
        #Esto es un bosquejo -- 2DA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
     
        eq222 =  MathTex("x","=","y^2-14y +49")\
            .scale(1.5).next_to(ORIGIN,UP*8)
        eqz =  MathTex("(","y^2-14y+49",")","+","\\sqrt{y}","=","11")\
            .scale(1.25).next_to(eq222,DOWN)
        uno =  MarkupText(
            f' <span fgcolor="{YELLOW}">(1)</span>', color=WHITE, font_size =38
            ).next_to(eqz,RIGHT)
        eqz1 = MathTex("y^2-14y+49","+","\\sqrt{y}","=","11")\
            .scale(1.25).next_to(eqz,DOWN)
        eqz11 = MathTex("y^2-14y+49","-","11","=","-","\\sqrt{y}")\
            .scale(1.25).next_to(eqz,DOWN)
        eqz111 = MathTex("y^2-14y+38","=","-","\\sqrt{y}")\
            .scale(1.25).next_to(eqz,DOWN)
        eqz14 = MathTex("(y^2-14y+38)^2","=","(","-","\\sqrt{y}",")^2")\
            .scale(1.25).next_to(eqz111,DOWN)
        eqz15 = MathTex("y^4-28y^3+272y^2-1064y+1444","=","y")\
            .scale(1.25).next_to(eqz14,DOWN)
        eqz16 = MathTex("y^4-28y^3+272y^2-1065y+1444","=","0")\
            .scale(1.25).next_to(eqz15,DOWN)
       
        play(seven_line.animate.to_corner(UR))
        wait(2)
        play(Write(eq222))
        wait(2)
 # (abajo) eqz es la segunda ecuación que aparece en la segunda escena y la escribo como en partes para poder hacer la sustitución que se aprecia en el video (cuando se introduce el valor de x algebraico en el paréntesis)    play(Write(eqz[0]),Write(eqz[2]),Write(eqz[3]),Write(eqz[4]),Write(eqz[5]),Write(eqz[6]))
        play(FadeIn(uno))
   
        play(Transform(eq222[2],eqz[1]))    
        play(FadeTransform(
            eqz,eqz1
        ),
        run_time=3
        )
        play(FadeIn(eqz))
        play(TransformMatchingTex(
            eqz1,eqz11
        ),
        run_time=3
        )
        play(FadeTransform(
            eqz11,eqz111
        ),
        run_time=3
        )
       
        play(Write(eqz14))
        play(Write(eqz15))
        play(Write(eqz16))
        wait(3)


# TransformMatchingTex como el mismo nombre del comando lo implica, une el texto y se aprecia muy elegante, solo que hay que ver si la transformación la hace “ahí mismo” en el mismo renglón o en el renglón de abajo. Todo depende de la estética. Que también se pueden utilizar los otros comandos (para manipular ecuaciones, que son:FadeTransform ) que emplee en esta animación, de nuevo, depende de qué tan satisfecho estás con la animación.
 
        # manim -pql scene7.py p3ii
       

#TERCERA ESCENA

from manim import *
class p4ii(Scene):
    def construct(self):
        #Esto es un bosquejo -- TERCERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
        eqz16 = MathTex("y^4-28y^3+272y^2-1065y+1444","=")\
            .scale(1.25).next_to(ORIGIN,UP*8)
        eqz17 = MathTex("(y-4)","(y^3-24y^2+176y-361)","=","0")\
            .scale(1.25).next_to(eqz16,DOWN)
        eqz18 = MathTex("y","=","4")\
            .scale(1.25).next_to(eqz17,DOWN)
        eq2 = MathTex("\\sqrt{x}","+ (","4",") =","7")\
            .scale(2).next_to(eqz18,DOWN)
        dos = MarkupText(
            f' <span fgcolor="{YELLOW}">(2)</span>', color=WHITE, font_size = 40
            ).next_to(eq2,RIGHT)
        eq21 = MathTex("\\sqrt{x}","+ ","4"," =","7")\
            .scale(2).next_to(eqz18,DOWN)
        eq211 = MathTex("\\sqrt{x}","=","7", "-", "4")\
            .scale(2).next_to(eqz18,DOWN)
        eq213 = MathTex("\\sqrt{x}","=", "3")\
            .scale(2).next_to(eq211,DOWN)
        eq214 = MathTex("x","=", "9")\
            .scale(2).next_to(eq211,DOWN)
       
     
    # (abajo) es la línea de código para que aparezca “elaborado por JMPR” y se vaya a la esquina por eso dice “to corner UPPER RIGHT”   
        play(seven_line.animate.to_corner(UR))
        play(FadeIn(eqz16))
        play(Write(eqz17))
        wait(2)
        play(Write(eqz18))  
        framebox0 = SurroundingRectangle(eqz18,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “eqz18”
        self.play(
        Create(framebox0), #Ejecute el perímetro que te declare anteriormente
        )
#(abajo) Escribo en partes la ecuación para poder hacer una SUSTITUCIÓN como me enseñó el profe Fabian Arenas.
        play(Write(eq2[0]),Write(eq2[1]),Write(eq2[3]),Write(eq2[4]))
        play(FadeIn(dos))


      
        play(Transform(eqz18[2],eq2[2]))# Con esta línea le ordenamos que haga la sustitución tan genial que se ve donde baja el cuatro hacía el paréntesis. 


        play(FadeOut(framebox0))# se desaparece el recuadro amarillo que usamos para REMARCAR.
        play(FadeOut(dos)) # se quita el dos que acompaña la ec.
       
        play(FadeTransform( # con esta animación se quita el paréntesis del cuatro
            eq2,eq21
        ),
        run_time=2
        )
        play(FadeOut(eqz18[2])) # ESTE FUE UN SÚPER AS DE LA MANGA QUE ME SAQUÉ, PORQUE NO MAS NO SE DEJABA LA CONDENADA ANIMACIÓN, es decir, el cuatro (4) que se baja al paréntesis en esa sustitución tan chingona NO SE QUERÍA QUITAR, ahi se quedaba como “huevo de perro” por eso primero le ordenó que se quite y en la línea de código de abajo ya que continúe con la manipulación de la citada igualdad. 


        play(TransformMatchingTex(
            eq21,eq211
        ),
        run_time=3
        )
#(abajo)YA LAS DEMÁS ANIMACIONES TRANSCURREN CON NORMALIDAD.


        play(Write(eq213))
        wait(2)
        play(FadeTransform(
            eq213,eq214
        ),
        run_time=2
        )
        framebox1 = SurroundingRectangle(eq214,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “eq214”
        self.play(
        Create(framebox1), #Ejecute el perímetro que te declare anteriormente
        )
        wait(2)
        play(FadeOut(framebox1))
        wait(3)
 
        # manim -pql scene7.py p4ii

        # Enlace al video en YouTube: https://www.youtube.com/watch?v=605QpLMyIBk&t=10s

