from turtle import Screen, Turtle
from person import Person
from ball import Ball
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

right = Person(380, 0)
left = Person(-380, 0)

def up(p):
    p.forward(20)

def d(p):
    p.backward(20)

screen.listen()
screen.onkey(lambda: up(right), "Up")
screen.onkey(lambda: d(right), "Down")
screen.onkey(lambda: up(left), "w")
screen.onkey(lambda: d(left), "s")

ball=Ball()
game = True
while game:
    screen.update()
    ball.forward(5)
    ball.bounce()
    time.sleep(0.03)
    if ball.distance(right)<19:
            ball.seth(180-(ball.heading()))
    if ball.distance(left)<19:
            ball.seth(180-(ball.heading()))
screen.exitonclick()