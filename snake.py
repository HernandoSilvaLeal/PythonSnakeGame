from pickle import NEWOBJ_EX
from turtle import Turtle, Screen

import time

#Creacion del tablero del juego

screen = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("#000000")
screen.title("Prográmate Snake Game")
screen.tracer(0)

#Construir cuerpo serpiente
starting_position = [(0,0),(-20, 0),(-40,0)] 

#Almaceno los segmentos de la serpiente
segments = []

for position in starting_position:
    snake_segment = Turtle("square")
    snake_segment.color ("#FFFFFF")
    snake_segment.penup()
    snake_segment.goto (position)
    segments.append(snake_segment)

#Animacion Serpiente

game_is_one = True

while game_is_one == True:
    screen.update()
    time.sleep(1)

    for seg_num in range(len(segments)-1,0,-1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

    # for segment in segments:
    #     segment.forward(20)

screen.exitonclick()

