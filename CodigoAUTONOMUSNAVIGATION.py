import turtle

# Seccion de creacion de funciones



def derecha():
    global contador
    pac.shape("ROVERM.gif")
    pac.showturtle()

    distancia1 = pac1.distance(pac)

    if pac.xcor() <= 400:
        pac.setposition(pac.xcor() + 1, pac.ycor())

    if distancia1 < 4 and pac1.isvisible():
        contador = contador + 1
        pac1.shape("ArUco.gif")
        pac1.hideturtle()

    print("distancia entre el rover y el ArUco: " + str(distancia1))  
    print(f"Coordenadas del rover: ({pac.xcor()}, {pac.ycor()}), Coordenadas objetivo: ({pac1.xcor()}, {pac1.ycor()})")  # Coordenadas del rover y ArUco


def izquierda():
    global contador
    pac.shape("ROVERM.gif")
    pac.showturtle()

    distancia1 = pac1.distance(pac)

    if pac.xcor() >= -400:
        pac.setposition(pac.xcor() - 1, pac.ycor())

    if distancia1 < 4 and pac1.isvisible():
        pac1.shape("ArUco.gif")
        pac1.hideturtle()
        contador = contador + 1

    print("distancia entre el rover y el ArUco: " + str(distancia1))  
    print(f"Coordenadas del rover: ({pac.xcor()}, {pac.ycor()}), Coordenadas objetivo: ({pac1.xcor()}, {pac1.ycor()})")  # Coordenadas del rover y ArUco


def arriba():
    global contador
    pac.shape("ROVERM.gif")
    pac.showturtle()

    distancia1 = pac1.distance(pac)

    if pac.ycor() <= 300:
        pac.setposition(pac.xcor(), pac.ycor() + 1)

    if distancia1 < 4 and pac1.isvisible():
        pac1.shape("ArUco.gif")
        pac1.hideturtle()
        contador = contador + 1

    print("distancia entre el rover y el ArUco: " + str(distancia1))  
    print(f"Coordenadas del rover: ({pac.xcor()}, {pac.ycor()}), Coordenadas objetivo: ({pac1.xcor()}, {pac1.ycor()})")  # Coordenadas del rover y ArUco


def abajo():
    global contador
    pac.shape("ROVERM.gif")
    pac.showturtle()

    distancia1 = pac1.distance(pac)

    if pac.ycor() >= -295:
        pac.setposition(pac.xcor(), pac.ycor() - 1)

    if distancia1 < 4 and pac1.isvisible():
        pac1.shape("ArUco.gif")
        pac1.hideturtle()
        contador = contador + 1

    print("distancia entre el rover y el ArUco: " + str(distancia1))  
    print(f"Coordenadas del rover: ({pac.xcor()}, {pac.ycor()}), Coordenadas objetivo: ({pac1.xcor()}, {pac1.ycor()})")  # Coordenadas del rover y ArUco




# Seccion de ventana
escenario = turtle.Screen()
escenario.bgpic("MARTEESCENARIO.gif")
escenario.setup(800, 600)
escenario.screensize(800, 600)

# Seccion de carga de imagenes
turtle.register_shape("ROVERM.gif")
turtle.register_shape("ArUco.gif")

# Seccion de creacion de objetos
pac = turtle.Turtle()
pac1 = turtle.Turtle()

pac.speed(500)
pac.penup()
pac.setposition(0, 0)
pac.setheading(90)
pac.shape("ROVERM.gif")

import random
pac1.speed(500)
pac1.penup()
coorx= random.randint(-380,380)
coory= random.randint(-280,280)
pac1.setposition(coorx, coory)
pac1.setheading(90)
pac1.shape("ArUco.gif")

x = True
contador = 0

while x == True:    #Algoritmo de busqueda del codigo ArUco

    pac.shape("ROVERM.gif")
    pac.showturtle()

    distancia1 = pac1.distance(pac)

    if distancia1 < 4 and pac1.isvisible():
        contador = contador + 1
        pac1.shape("ArUco.gif")
        pac1.hideturtle()

    dant = pac1.distance(pac)
    arriba()
    dnueva = pac1.distance(pac)
    while dnueva < dant:
        dant = pac1.distance(pac)
        arriba()
        dnueva = pac1.distance(pac)
    abajo()
    dant = pac1.distance(pac)
    abajo()
    dnueva = pac1.distance(pac)
    while dnueva < dant:
        dant = pac1.distance(pac)
        abajo()
        dnueva = pac1.distance(pac)
    arriba()
    dant = pac1.distance(pac)
    izquierda()
    dnueva = pac1.distance(pac)
    while dnueva < dant:
        dant = pac1.distance(pac)
        izquierda()
        dnueva = pac1.distance(pac)
    derecha()
    dant = pac1.distance(pac)
    derecha()
    dnueva = pac1.distance(pac)
    while dnueva < dant:
        dant = pac1.distance(pac)
        derecha()
        dnueva = pac1.distance(pac)
    izquierda()


    if contador == 1:   #Al encontrar al ArUco se rompe el programa
            x = False

escenario.clear()

print("Se encontró al ArUco")
