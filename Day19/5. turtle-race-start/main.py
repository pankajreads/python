from turtle import Turtle, Screen
from random import randint
tut=["Red","Blue","Yellow","Green"]
ipos=[250,125,-125,-250]
for i in range(0,4):
    turtle=Turtle()
    turtle.shape("turtle")
    turtle.color(tut[i])
    turtle.penup()
    turtle.setpos(-350,ipos[i])
    tut[i]=turtle
race=True
while race:
    tut[randint(0,3)].forward(randint(10,15))
    if tut[1].xcor()>350 or tut[2].xcor()>350 or tut[3].xcor()>350 or tut[0].xcor()>350:
        race=False
screen=Screen()
screen.exitonclick()