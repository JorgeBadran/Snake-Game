from tkinter import mainloop
import turtle
import time
import random 

postpone = 0.1

#Marker
#Marcador

score = 0
high_score = 0


#Window configuration
#Configuracion de la ventana

window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('black')
window.setup(600, 600)
window.tracer()


#Snake had
#Cabeza de serpiente

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.penup()
head.goto(0,0)
head.direction = 'stop'
head.color('#FFFFFF')

#Food
#Comida

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.penup()
food.goto(0,100)
food.color('red')

#Segments / Snake Body
#Segmentos / Curpo de Serpiente

segments = []

#Text
#Texto

text = turtle.Turtle()
text.speed(0)
text.color("#FFFFFF")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write("Score: 0    High Score: 0", align = "Center", font = ("courier", 24, "normal"))   



#Functions
#Funciones

def up():
    head.direction = 'up'

def down():
    head.direction = 'down'

def left():
    head.direction = 'left'

def right():
    head.direction = 'right'




def mov():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
        
#Keyboard
#Teclado

window.listen()
window.onkeypress(up, 'Up')
window.onkeypress(down, 'Down')
window.onkeypress(left, 'Left')
window.onkeypress(right, 'Right')



while True:
    window.update()
    
    #Edge Collisions
    #Colisiones Borde

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hide Segments
        #Esconder Segmentos

        for segments in segments:
            segments.goto(2000,2000)

        #clear segment list
        #limpiar lista del segmento

        segments.clear()

        #Reset Bookmark
        #Resetear Marcador

        score = 0
        text.clear()
        text.write("Score: {}    High Score: {}".format(score, high_score) , align = "Center", font = ("courier", 24, "normal"))


    #Food Collisions
    #Colisiones de Comida

    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)
 
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape('square')
        new_segments.color('#D4CCCC')
        new_segments.penup()
        segments.append(new_segments)

        #Increase Marker
        #Aumentar Marcador

        score += 10
        if score > high_score:
            high_score = score

            text.clear()
            text.write("Score: {}    High Score: {}".format(score, high_score) , align = "Center", font = ("courier", 24, "normal"))

    #Move Snake Body
    #Mover Cuerpo de la Serpiente

    totalSeg = len(segments)
    for index in range(totalSeg -1, 0, -1, ):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    mov()
    time.sleep(postpone)


   

