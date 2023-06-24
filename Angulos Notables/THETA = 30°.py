 
from manim import *
class p1i(Scene):
    def construct(self):
       #PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
        c = Circle(radius=3,stroke_opacity=0.4,color=BLUE)
       
        line00 = Line([0,0,0],[1.5,0,0])#Declaramos las líneas, teniendo en cuenta (obviamente) a nuestro sistema de coordenadas o plano cartesiano.
        line0 = Line([1.5,0,0],[3,0,0])
        line1 = Line([3,0,0],[1.5,2.6,0])
        line2 = Line([1.5,2.6,0],[0,0,0])  
        line3 = Line([1.5,2.6,0],[1.5,0,0])
#Las CINCO líneas declaradas anteriormente, son las que conforman el triángulo equilátero que está dentro del círculo.
        a = Arc(0.5, 0*DEGREES, 60*DEGREES,arc_center=[0,0,0],color=RED)
#Mucho OJO porque este arco es una chingonería. El primer argumento es el radio del arco, el segundo es desde donde comienza a trazar el arco, el tercero es el arco propiamente que tiene 60°, el cuarto es el centro o el origen del arco, el quinto es el color, obviamente. 
        a11 = Arc(0.5, 180*DEGREES, -60*DEGREES,arc_center=[3,0,0],color=RED)
        a1 = Arc(0.7, -90*DEGREES, -30*DEGREES,arc_center=[1.5,2.6,0],color=GREEN)
# El arco declarado arriba es VERDE, es el de BETA.
       theta = MathTex(r"\theta =")\
            .scale(0.6).next_to(a,(1/6)*UP + (1/3)*RIGHT)
        val = DecimalNumber(60,num_decimal_places = 0,unit="^\\circ",font_size=28).next_to(theta, (1/4)*RIGHT)
# “val” (arriba) es para declarar 60° (ángulo IZQUIERDO)
        theta1 = MathTex(r"\theta =")\
            .scale(0.6).next_to(a11,(1/6)*UP +(3/2)*LEFT)
        val1 = DecimalNumber(60,num_decimal_places = 0,unit="^\\circ",font_size=28).next_to(theta1, (1/4)*RIGHT)
# “val1” (arriba) es para declarar 60° (ángulo DERECHO)
        Beta = MathTex(r"\beta ")\
            .scale(0.6).next_to(a1,(1/4)*DOWN)
        line6 = Line([1.375,0,0],[1.375,0.125,0])
        line7 = Line([1.375,0.125,0],[1.5,0.125,0])
# Las dos líneas declaradas anteriormente son para el pequeño cuadrado que representa el ángulo recto.
        brace_down = Brace(line00,DOWN)
        brace_right = Brace(line3,RIGHT)
 
        line_vector = line2.get_unit_vector()
        normal_vector = rotate_vector(line_vector,-PI/2)
        brace_left = Brace(line2,normal_vector,color=RED)
# Las tres líneas declaradas anteriormente son NADA MÁS para el corchete de la HIPOTENUSA.
        hip =MathTex("HIP = 1").next_to(brace_left, LEFT)
        c_a = MathTex("C.A=0.5").next_to(brace_down, DOWN)
        c_o = MathTex("C.O = {\\sqrt{3}\\over{2}}").next_to(brace_right, RIGHT)
     
       
        #DE AHORA EN ADELANTE, LOS COMANDOS.


        play(seven_line.animate.to_corner(UR))
        play(Create(c))
        wait(1)
        play(Create(line00))
        play(Create(line0))
        play(Create(line1))
        play(Create(line2))
        play(Create(line3))
       
        play(Create(a),Create(a11))#Son los 2 arcos de 60°, cada uno.
     
        play(Write(line6),Write(line7))#Es el pequeño cuadrado de 90°.
        play(Write(theta),Write(theta1))#Son theta en los arcos ROJOS.
        play(Write(val),Write(val1))
        wait(3)
        play(FadeOut(line0),FadeOut(line1),FadeOut(theta1),FadeOut(val1),FadeOut(a11))#Vas a desaparecer todo lo que está en los paréntesis. AL MISMO TIEMPO  
        wait(1)
        play(Create(a1))# El arco VERDE, es el de BETA.
        play(Write(Beta))
        play(FadeOut(c))#Desaparece el círculo
        wait(2)
        play(FadeIn(brace_down),FadeIn(brace_right),FadeIn(brace_left))
        play(Write(hip),Write(c_o),Write(c_a))
        wait(2)
        play(FadeOut(val),FadeOut(theta))
        play(FadeOut(Beta))
        play(FadeOut(brace_down),FadeOut(brace_left),FadeOut(brace_right))
        play(FadeOut(hip),FadeOut(c_o),FadeOut(c_a))
        wait(1)
        grp = Group(line00,line2,line3,a,a1,line6,line7)
#En la línea de arriba, declaramos un grupo para posteriormente poder girarlo en el próximo comando.
        play(grp.animate.rotate(-PI/2))
              
        wait(3)
 
# manim -pqh scene6.py p1i



#SEGUNDA ESCENA

from manim import *
class p2(Scene):
    def construct(self):
       #SEGUNDA ESCENA. Tuve que hacer esta escena APARTE ya que se estaba volviendo engorroso para la máquina procesar todas las animaciones y para mí, ya que se vuelve un poco complejo ya que Manim se pierde un poco cuando le das comandos como “scale” o que gire (se vuelve complejo en este momento para mí, ubicar a Manim cuando la figura se hace más grande o gira.). Por eso lo hice así.
#       EN APARIENCIA, NO SE COPIARON LOS PARÉNTESIS MÁS ABAJO. PERO SI LO HICIERON, SOLO QUE SON NEGROS. 
          seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{BLUE}">JMPR</span>', color=WHITE, font_size =30
            )
        play = self.play
        wait = self.wait
        add = self.add    
        #Las TRES líneas de arriba, son para no estar declarando a cada rato "self.play" o "self.wait". Es como para automatizarlo.
       
       
        line00 = Line([0,0,0],[2.6,0,0])#Declaramos las líneas, teniendo en cuenta (obviamente) a nuestro sistema de coordenadas o plano cartesiano.
       
        line1 = Line([2.6,0,0],[0,1.5,0])  
        line2 = Line([0,1.5,0],[0,0,0])
        a = Arc(0.5, 270*DEGREES, 60*DEGREES,arc_center=[0,1.5,0],color=RED)
       
        a1 = Arc(0.7, 180*DEGREES, -30*DEGREES,arc_center=[2.6,0,0],color=GREEN)
   
        Beta = MathTex(r"\beta =")\
            .scale(0.6).next_to(a1,2*LEFT)
        val = DecimalNumber(30,num_decimal_places = 0,unit="^\\circ",font_size=28).next_to(Beta, (1/4)*RIGHT)
        line6 = Line([0.125,0,0],[0.125,0.125,0])
        line7 = Line([0.125,0.125,0],[0,0.125,0])
#Las dos líneas de arriba son es el pequeño cuadrado que representa el ángulo recto.
        brace_down = Brace(line00,DOWN)
 
        line_vector = line1.get_unit_vector()
        normal_vector = rotate_vector(line_vector,-PI/2)
        brace_right = Brace(line1,normal_vector,color=RED)
# Las tres líneas declaradas anteriormente son NADA MÁS para el corchete de la HIPOTENUSA.
 
        brace_left = Brace(line2,LEFT)
 
       
        hip =MathTex("HIP = 1")\
            .scale(0.7).next_to(line2,7*RIGHT+(1/4)*UP)
       
        c_a = MathTex("C.A={\\sqrt{3}\\over{2}}")\
            .scale(0.7).next_to(brace_down, DOWN)
        c_o = MathTex("C.O = 0.5")\
            .scale(0.7).next_to(brace_left,LEFT)
     
   
        #DESDE AQUÍ LOS COMANDOS DE EJECUCIÓN
        play(seven_line.animate.to_corner(UR))
        wait(1)
        play(Create(line00))
       
        play(Create(line1))
        play(Create(line2))
       # Las tres pequeñas líneas que conforman el triángulo rectángulo
son las declaradas anteriormente.  
    
        play(Write(line6),Write(line7))#Es el pequeño cuadrado de 90°.
     
        play(Create(a1))#Ángulo verde, BETA
        play(Create(a))
        wait(2)
        play(Write(Beta))
        play(Write(val))
   
        wait(1)
        play(FadeIn(brace_down),FadeIn(brace_right),FadeIn(brace_left))
        wait(1)
        play(Write(hip),Write(c_o),Write(c_a))
        wait(2)
     
       
        grp = Group(line00,line1,line2,a,a1,line6,line7,Beta,val,brace_left,brace_right,brace_down,hip,c_o,c_a)
#Este grupo (arriba) es para poder mover todo lo que está dentro, como uno solo. 
        play(grp.animate.move_to(
            UP*1.5 +
            LEFT*4
        ))
        wait(2)


        #Aquí vienen las funciones trigonométricas
#FUNCIÓN SENO
        sin = MathTex("\\sin\\beta","=","{C.O\\over HIP}","=")\
                .scale(0.9)
        sqrt = MathTex("1\\over{2}")\
                .scale(0.9).next_to(sin, RIGHT)
        grp2 = Group(sin,sqrt).next_to(ORIGIN,3.5*UP+(1/4)*RIGHT)
#Junto “sin” y “sqrt” porque si quiero poner todo en “sin” por alguna razón no se representa bien “sqrt”. Por eso los he puesto por separado y los junto en “grp2”
        play(FadeIn(grp2))
        
        wait(1)


# AQUÍ VIENEN LOS SOMBREADOS
# PRIMERA TANDA DE SOMBREADOS
 
        framebox0 = SurroundingRectangle(c_o,buff = .1)#Estamos declarando uno de esos rectángulos amarillos, que rodean. En este caso, le ordenó que rodee a “c_o1”
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
       
#FUNCIÓN COSENO                   
        cos = MathTex("\\cos\\beta={C.A\\over HIP} =")\
            .scale(0.9)
        sqrt1 = MathTex("\\sqrt{3}\\over{2}")\
            .scale(0.9).next_to(cos, RIGHT)
            #Aguas con dejar espacio entre \\ y over. Lo correcto es SIN ESPACIO.
        grp3 = Group(cos,sqrt1).next_to(grp2,DOWN)      
        play(FadeIn(grp3))  
        wait(1)


        #SOMBREADO
# SEGUNDA TANDA DE SOMBREADOS


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
       
       
       #FUNCIÓN TANGENTE
        tan = MathTex("\\tan\\beta={C.O\\over C.A} =")\
            .scale(0.9)
        sqrt2 = MathTex("1\\over\\sqrt{3}")\
            .scale(0.9).next_to(tan, RIGHT)
       
        grp4 = Group(tan,sqrt2).next_to(grp3,DOWN)
        play(FadeIn(grp4))
        wait(1)


#TERCERA TANDA DE SOMBREADOS
 
        framebox011 = SurroundingRectangle(c_o,buff = .1)
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


        wait(3)



#TERCERA ESCENA → Aparece la calculadora de Wolfram

#CUARTA ESCENA → “Échale un vistazo a la descripción del video [...]”

# Enlace al video en YouTube: https://www.youtube.com/watch?v=UGr9k07cnfY