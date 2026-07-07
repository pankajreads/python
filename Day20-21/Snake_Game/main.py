from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

# Create screen
screen = Screen()
screen.bgcolor("Black")  # Set background color
screen.setup(width=600, height=600)  # Set screen size
screen.title("Snake Game")  # Title of window
screen.tracer(0)  # Turn off auto screen updates (manual control)

# Create game objects
snake = Snake()
f = Food()
score = Scoreboard()

# ------------------ COLLISION FUNCTIONS ------------------

# Check if snake head touches food
def collision_food(body, f):
    if f.distance(body[0]) < 15:  # Distance between head and food
        return True
    else:
        return False

# Check collision with wall or itself
def collison_wall(body):
    # Wall collision (boundary check)
    if body[0].xcor() > 280 or body[0].xcor() < -280 or body[0].ycor() > 280 or body[0].ycor() < -280:
        return True
    
    # Self collision (head touches body)
    for i in range(1, len(body)):
        if body[0].distance(body[i]) < 1:
            return True
    
    return False

# ------------------ CONTROL FUNCTIONS ------------------

# Move up (prevent reverse direction)
def w():
    if snake.direction != "DOWN":
        snake.direction = "UP"

# Move down
def s():
    if snake.direction != "UP":
        snake.direction = "DOWN"

# Move left
def a():
    if snake.direction != "RIGHT":
        snake.direction = "LEFT"

# Move right
def d():
    if snake.direction != "LEFT":
        snake.direction = "RIGHT"

# Listen to keyboard inputs
screen.listen()
screen.onkey(w, "Up")
screen.onkey(s, "Down")
screen.onkey(a, "Left")
screen.onkey(d, "Right")

# ------------------ GAME LOOP ------------------

game = True
while game:
    screen.update()  # Refresh screen
    time.sleep(0.1)  # Control game speed

    # Check wall or self collision
    if collison_wall(snake.body):
        game = False
        score.game_over()  # Show game over text
        screen.bgcolor("Gray")  # Change background

    snake.move()  # Move snake forward

    # Check if snake eats food
    if collision_food(snake.body, f):
        snake.increase_snake()  # Increase snake length
        f.hideturtle()  # Hide old food
        score.increase_score()  # Increase score
        f = Food()  # Create new food

# Exit when clicked
screen.exitonclick()