from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from random import randint,choice
import time
screen=Screen()
screen.bgcolor("Black")
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
f=Food()
score=Scoreboard()

def collision_food(body,f):
    if f.distance(body[0])<15:
        return True
    else:
        return False
def collison_wall(body):
   if body[0].xcor() > 280 or body[0].xcor() < -280 or body[0].ycor() > 280 or body[0].ycor() < -280:
        return True
   for i in range(1,len(body)):
        if body[0].distance(body[i]) <1 :
            return True
   return False
def w():
    if snake.direction != "DOWN":
        snake.direction = "UP"

def s():
    if snake.direction != "UP":
        snake.direction = "DOWN"

def a():
    if snake.direction != "RIGHT":
        snake.direction = "LEFT"

def d():
    if snake.direction != "LEFT":
        snake.direction = "RIGHT"
screen.listen()
screen.onkey(w, "Up")
screen.onkey(s, "Down")
screen.onkey(a, "Left")
screen.onkey(d, "Right")
game=True
while game:
    if collison_wall(snake.body):
        game=False
        score.game_over()
        screen.bgcolor("Gray")
    screen.update()
    snake.move()
    time.sleep(0.1)
    if collision_food(snake.body,f):
        snake.increase_snake()
        f.hideturtle()
        score.increase_score()
        f=Food()
 
screen.exitonclick()