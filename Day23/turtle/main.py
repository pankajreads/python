import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

carm=CarManager()
player=Player()
score=Scoreboard()

screen.onkey(player.move,"Up")
screen.listen()
screen.onkey(player.backward(10),"Down")
screen.listen()
# screen.onkey(player.left,"left")
# screen.listen()
# screen.onkey(player.right,"Right")
# screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    carm.create_car()
    carm.move()
    for car in carm.all:
        if car.distance(player)<20:
            game_is_on=False
            score.game_over()
    if player.ycor()>=235:
        score.increase()
        player.goto(0,-280)
        carm.speed+=0.1
screen.exitonclick()