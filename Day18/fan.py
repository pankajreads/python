import random  
from turtle import Turtle,Screen, colormode
tim=Turtle()
tim.shape("circle")
tim.pensize(10)
colormode(255)
screen=Screen()
walk=True
while walk:
    tim.forward(25)
    tup = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    tim.pencolor(tup)
    tim.pencolor()
    a=[90,180,270,0]
    b=a[random.randint(0,3)]
    tim.right(b)
    
