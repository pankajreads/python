from turtle import Turtle,Screen, colormode
from random import randint
timmy=Turtle()
timmy.shape("turtle")
ang=360
colormode(255)
timmy.pensize(5)
for i in range(3,10):
    tup = ( randint(0,255), randint(0,25),  randint(90,255))
    timmy.pencolor(tup)
    timmy.pencolor()
    for j in range(i):
        timmy.forward(100)
        timmy.right(ang/i)
            
print("")
screen=Screen()
screen.exitonclick()