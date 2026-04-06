from turtle import Screen, Turtle
from person import Person
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)
scoreboard=Scoreboard()

right = Person(360, 0)
left = Person(-360, 0)

def up(p):
    if p.ycor() <260:
        p.forward(20)

def d(p):
    if p.ycor()>-260:
        p.backward(20)

screen.listen()
screen.onkey(lambda: up(right), "Up")
screen.onkey(lambda: d(right), "Down")
screen.onkey(lambda: up(left), "w")
screen.onkey(lambda: d(left), "s")
speed=5
ball=Ball()
game = True
while game:
    screen.update()
    ball.forward(speed)
    #detect collision with walls
    if ball.ycor() <-280 or ball.ycor()>280:
        ball.bounce()
    time.sleep(0.03)
    #detect collision with person
    if ball.distance(left) < 45 and ball.xcor() < -340 and( ball.heading() > 90 or ball.heading() >270):
        speed += 0.5
        ball.seth(180 - ball.heading())
        ball.forward(10)

    if ball.distance(right) < 45 and ball.xcor() > 340 and (ball.heading() < 90 or ball.heading() > 270):
        speed += 0.5
        ball.seth(180 - ball.heading())
        ball.forward(10)
    if ball.xcor()>380:
        ball.goto(0,0)
        scoreboard.increase_lscore()
        ball.seth(180-(ball.heading()))
    if ball.xcor()<-380:
        ball.goto(0,0)
        scoreboard.increase_rscore()
        ball.seth(180-(ball.heading()))

    if scoreboard.l_score >= 10 or scoreboard.r_score >= 10:
        game = False
        scoreboard.game_over()
screen.exitonclick()