from turtle import Turtle, colormode,Screen
from random import randint
tim=Turtle()
colormode(255)
def random_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return r,g,b
for _ in range(0,24):
    tim.pencolor(random_color())
    tim.circle(50)
    tim.left(15)
screen=Screen()
screen.exitonclick()