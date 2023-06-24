
from manim import *
 
class p1i(Scene):
    def construct(self):


 #De acuerdo voy a poner el código por escenas, tengamos presente que Python es muy mamón con el indentado, ni te pases, ni lo omitas. Bueno, a lo que voy  en cuanto a que voy por escenas es que voy renderizando una escena a la vez. En vez de todas de un sopetón. Conforme a tengo mis escenas en mi editor de video es como las voy a poner aquí. A efecto de que quiera hacerlo más escalable en cualquier momento.
 
 #PRIMERA ESCENA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{GREEN}">JMPR</span>', color=WHITE, font_size =32
            ).next_to(ORIGIN, 9*DOWN + RIGHT)
        l1 = MarkupText(
            f'Un grupo minero compró 1 excavadora y 2 volquetes por 5  <span fgcolor="{YELLOW}">lingotes</span>', color=WHITE, font_size =32).next_to(ORIGIN, 9*UP) # CON ESTOS COMANDOS LOGRAMOS QUE "lingotes" SEA AMARILLO, HACIENDO ALUSIÓN A QUE EL LINGOTE ES DE ORO.
        l2 = Text("y después, al mismo precio por unidad, compró 2 excavadoras y 3 volquetes", font_size =30).next_to(l1,DOWN)
        l3 = Text("por 8 lingotes. Hallar el precio de la excavadora y del volquete,", font_size =32).next_to(l2,DOWN)
        l4 = Text("respectivamente.", font_size =32).next_to(l3,DOWN)
        self.play(Write(seven_line))
        self.play(Write(l1))
        self.play(Write(l2))
        self.play(Write(l3))
        self.play(Write(l4))
        self.wait(3)



#SEGUNDA ESCENA
    #SEGUNDA ESCENA
        seven_line = Text("Elaborado por: JMPR").next_to(ORIGIN, 7*DOWN + RIGHT)\
            .scale(0.5)# Interesante cómo se utiliza 7*DOWN + RIGHT
        first_line = Text("Convertiremos, al lenguaje algebraico, esta situación.")\
            .scale(0.80).next_to(ORIGIN,7*UP)
        tex1 = Text("x = Precio de volquete", font_size=30).next_to(first_line,DOWN) #Te declaro un texto, dale cierto   tamaño a la fuente y ponlo abajo de la "first_line"
        tex2 = Text("y = Precio de excavadora", font_size=30).next_to(tex1,RIGHT) #Te declaro un texto, dale cierto   tamaño a la fuente y ponlo abajo de la "tex_1"
        eqx = MathTex("x +2y = 5")\
                .scale(1.5) #Te declaro una igualdad y ponla DOS unidades ABAJO del ORIGEN.
        eqy = MathTex("2x +3y = 8")\
                .scale(1.5).next_to(eqx,DOWN) #Te declaro una igualdad y ponla  DEBAJO de eqx.
        self.play(Write(seven_line)) #Elaborado por : JMPR
        self.play(Write(first_line))#Renderiza "first_line"
        tex1.generate_target() #Generando el target para tex1 ()
        tex1.target.shift(3*LEFT)#Te vas a mover tres unidades a la izquierda (obvio)
   
        self.play(MoveToTarget(tex1))#Ejecuta el target para "tex1" = "x = Bloc de 30 centavos" se mueva a la izquierda.
        self.play(FadeIn(tex2))#Escribe --> "y = Precio de excavadora"
        self.play(FadeIn(eqx,eqy))
        self.wait(3)
 
        #ME AGRADA

#TERCERA ESCENA
"""
Es donde sale “TENGAMOS PRESENTES NUESTRAS FÓRMULAS” y aparecen ambas fórmulas. Acto seguido aparece: un a_{11} y “Subíndice izquierdo: RENGLÓN”, “Subíndice derecho: COLUMNA” y por último : “Si tienes dificultad para orientarte, recuerda el sentido de tu columna vertebral”
PERO ESTA ESCENA TRES, LA CORTE DE OTRO VIDEO Y ASÍ MISMO LA PUSE EN EL EDITOR DE VIDEO. DE TAL FORMA QUE NO HAY CÓDIGO COMO TAL. MÁS QUE ESTÁ EN EL VIDEO DE LA MINERA (el código).
"""

#CUARTA ESCENA
 
 
        #ÉNFASIS EN RENGLONES Y COLUMNAS
        eqx = MathTex("x +2y = 5").next_to(ORIGIN,9*UP) #Te declaro una igualdad y ponla nueve unidades ARRIBA del ORIGEN.
        eqy = MathTex("2x +3y = 8").next_to(eqx,2*DOWN) #Te declaro una igualdad y ponla  DEBAJO de eqx.
        l1 = Text("Renglón UNO (1)", font_size=30).next_to(eqx,2*RIGHT)
        l2 = Text("Renglón DOS (2)",font_size=30).next_to(eqy,2*RIGHT)
        l3 =Text("Con respecto a las COLUMNAS (de izquierda a derecha):", font_size=28).next_to(eqy,2*DOWN)
        l4 = Text("La primera corresponde a:   ").next_to(l3,DOWN)
        m1 = MathTex("a_{11} ,  a_{21}").next_to(l4, RIGHT)
        l5 =Text ("La segunda corresponde a:").next_to(l4,DOWN)
        m2 = MathTex("a_{12} , a_{22}").next_to(l5, RIGHT)
        l6 =Text("La tercera son las CONSTANTES:").next_to(l5,DOWN)
        m3 = MathTex("c_{1} , c_{2}").next_to(l6, RIGHT) #MathTex("c_1 , c_2") --> Cuando intentaba correr el programa, así (sin los corchetes) NO ME LO PERMITÍA. Tener presente.
        self.play(Write(eqx),Write(eqy)) # Escribe las ecuaciones  "0.3x +0.8y = 350"; "x +y = 1000"
        framebox = SurroundingRectangle(eqx, buff = .1) #Vas a poner un perímetro que rodee eqx
        self.play(
        Create(framebox), #Ejecute el perímetro que te declare anteriormente
            )
        self.play(Write(l1))
        framebox1 = SurroundingRectangle(eqy, buff = .1) #Vas a poner un perímetro que rodee eqy que es -10
        self.play(
        Create(framebox1), #Ejecute el perímetro que te declare anteriormente
            )
        self.play(Write(l2))
       
        self.play(Write(l3))#"Con respecto a las COLUMNAS (de izquierda a derecha
        self.play(Write(l4), Write(m1))#"La primera corresponde a:   "
        self.play(Write(l5), Write(m2))#"La segunda corresponde a:   "
        self.play(Write(l6), Write(m3))
        self.wait(3)


#QUINTA ESCENA
#EJEMPLO DE UBICACIÓN RENGLÓN COLUMNA
        seven_line = MarkupText(
            f'ELABORADO POR <span fgcolor="{GREEN}">JMPR</span>', color=WHITE, font_size =32
            ).next_to(ORIGIN, 9*DOWN + RIGHT)
       
        l1 = Text("EJEMPLO").next_to(ORIGIN,10*UP)
        nota = Text("Nota: Cuando se omite el signo, este es POSITIVO",font_size=24).next_to(l1,DOWN)
        eqx = MathTex("+1","x", "+2","y", "=", "5").next_to(nota,3*DOWN) #Te declaro una igualdad y ponla a TRES unidades DEBAJO de l1.
        eqy = MathTex("+2","x", "+3","y", "=", "8").next_to(eqx,DOWN) #Te declaro una igualdad y ponla  DEBAJO de eqx.
        self.play(Write(seven_line))
        self.play(Write(l1))# Escribe --> "EJEMPLO"
        self.play(Write(nota))
        self.play(Write(eqx),Write(eqy)) #Escribe las ecuaciones ORIGINALES
 
        framebox = SurroundingRectangle(eqx[0], buff = .1) #Vas a poner un perímetro que rodee el elemento 0 de eqx que es +0.3
        self.play(
        Create(framebox), #Ejecute el perímetro que te declare anteriormente
                )
        l2 = MathTex("a_{11}").next_to(eqy,4*DOWN)\
                .scale(3)
        self.play(Write(l2))
        self.wait(2)
        self.play(FadeOut(l2,framebox))#Desaparece l2 y el perímetro “framebox”
 
 
        framebox1 = SurroundingRectangle(eqx[2], buff = .1)
        self.play(
        Create(framebox1), #Ejecute el perímetro que te declare anteriormente
                )
        l3 = MathTex("a_{12}").next_to(eqy,4*DOWN)\
                .scale(3)
        self.play(Write(l3))
        self.wait(2)
        self.play(FadeOut(l3,framebox1))
 
        framebox2 = SurroundingRectangle(eqx[5], buff = .1)
        self.play(
        Create(framebox2), #Ejecute el perímetro que te declare anteriormente
                )
        l4 = MathTex("c_1").next_to(eqy,4*DOWN)\
                .scale(3)
        self.play(Write(l4))
        self.wait(2)
        self.play(FadeOut(l4,framebox2))
        self.wait(2)
 
        framebox3 = SurroundingRectangle(eqy[0], buff = .1)
        self.play(
        Create(framebox3),
                )
        l5 = MathTex("a_{21}").next_to(eqy,4*DOWN)\
                .scale(3)
        self.play(Write(l5))
        self.wait(2)
        self.play(FadeOut(l5,framebox3))
        self.wait(2)
 
        framebox4 = SurroundingRectangle(eqy[2], buff = .1)
        self.play(
        Create(framebox4), #Ejecute el perímetro que te declare anteriormente
                )
        l6 = MathTex("a_{22}").next_to(eqy,4*DOWN)\
                .scale(3)
        self.play(Write(l6))
        self.wait(2)
        self.play(FadeOut(l6,framebox4))
        self.wait(2)
 
        framebox5 = SurroundingRectangle(eqy[5], buff = .1)
        self.play(
        Create(framebox5), #Ejecute el perímetro que te declare anteriormente
                )
        l7 = MathTex("c_2").next_to(eqy,4*DOWN)\
                .scale(3)
        self.play(Write(l7))
        self.wait(2)
        self.play(FadeOut(l7,framebox5))
        self.wait(2)


        #QUEDÓ CASI PERFECTO PARA LOS "lingotes"

#SEXTA ESCENA

        seven_linei = MarkupText(
            f'ELABORADO POR <span fgcolor="{GREEN}">JMPR</span>', color=WHITE, font_size =32
            ).next_to(ORIGIN, 9*UP + LEFT)


        sixth_line = Text("Recomiendo que primero se encuentre el valor del determinante")\
                .scale(0.7).next_to(ORIGIN, 5*UP)
        seven_line =Text("(el denominador de AMBAS fórmulas)").next_to(sixth_line,DOWN)
        det = MathTex("Determinante = a_{11} a_{22} - a_{12} a_{21}").next_to(ORIGIN,2*DOWN)
        eight_line = Text("Sustitución").next_to(det,DOWN)
        det1 = MathTex("=" ,"(+1)(+3)-(+2)(+2)", "=", "3 -4", "=","-1").next_to(eight_line,DOWN)
        self.play(Write(seven_linei))
        self.play(Write(sixth_line),Write(seven_line)) #Escribe -> "Recomiendo que primero se encuentre el valor del determinante"
        self.wait(3)
        self.play(Write(det))
        self.play(Write(eight_line))#Escribe --> "Sustitución"
        self.play(Write(det1))#Escribe --> "=" ,"(1)(2)-(3)(4)", "=", "2-12", "=","-10"
        framebox2 = SurroundingRectangle(det1[5], buff = .1) #Vas a poner un perímetro que rodee el elemento 5 de det1 que es -10
        self.play(
        Create(framebox2), #Ejecute el perímetro que te declare anteriormente
            )
        self.wait(3)

#SÉPTIMA ESCENA

nine_line = Text("Sustitución y resultado").next_to(ORIGIN,9*UP)
        eqx1 = MathTex("x = {a_{22} c_1 - a_{12} c_2\\over a_{11} a_{22} - a_{12} a_{21}}" ).next_to(nine_line,3*DOWN)#Despeje para X
           
eqx2 = MathTex("=","{a_{22} c_1 - a_{12} c_2\\over-1}","=","{(+3)(+5)-(+2)(+8)\\over -1}","=","{15-16\\over-1}","=","{-1\\over-1}","=","1").next_to(eqx1,DOWN)
        ten_line = Text("INTERPRETACIÓN: Cada volquete cuesta 1 LINGOTE.",font_size=28).next_to(eqx2,2*DOWN)
        self.play(Write(nine_line))
        self.play(Write(eqx1))
        self.wait(2)
        self.play(Write(eqx2))
        self.wait(3)
        framebox = SurroundingRectangle(eqx2[9], buff = .1) #Vas a poner un perímetro que rodee el elemento 7 de eqx2 que es 900
        self.play(
        Create(framebox), #Ejecute el perímetro que te declare anteriormente
            )
        self.play(Write(ten_line))#Redacta la interpretación
        self.wait(3)

#OCTAVA ESCENA

            nine_line = Text("Sustitución y resultado").next_to(ORIGIN,9*UP)
            eqx1 = MathTex("y = {a_{11} c_2 - a_{21} c_1\\over a_{11} a_{22} - a_{12} a_{21}}").next_to(nine_line,3*DOWN)#Despeje para Y
            eqx2 = MathTex("=","{a_{11} c_2 - a_{21} c_1\\over-1}","=","{(+1)(+8)-(+2)(+5)\\over -1}","=","{8-10\\over-1}","=","{-2\\over-1}","=","2").next_to(eqx1,DOWN)
            ten_line = Text("INTERPRETACIÓN: Cada excavadora cuesta 2 LINGOTES.", font_size=30).next_to(eqx2,2*DOWN)
            self.play(Write(nine_line))
            self.play(Write(eqx1))
            self.wait(2)
            self.play(Write(eqx2))
            self.wait(3)
            framebox = SurroundingRectangle(eqx2[9], buff = .1) #Vas a poner un perímetro que rodee el elemento 5 de det1 que es -10
            self.play(
            Create(framebox), #Ejecute el perímetro que te declare anteriormente
            )
            self.play(Write(ten_line))
            self.wait(3)


# https://www.youtube.com/watch?v=LjehT-bBKdA
