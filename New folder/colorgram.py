import colorgram
from turtle import Turtle
color=colorgram.extract('new.jpg',9)
tim=Turtle()
tim.dot()
tim.pensize(5)
for i in color:
    tim.forward(20)
    tim.left(90)
    tim.forward(5)
    tim.left(90)
    tim.forward(20)
    tim.right(90)
    tim.forward(5)