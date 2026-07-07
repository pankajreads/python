from turtle import Turtle
from random import randint, choice

class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initialize Turtle class

        # Random color for food (adds variety)
        self.color(choice(["red", "green", "blue"]))

        self.shape("circle")  # Food is circular
        self.penup()  # Prevent drawing lines while moving
        self.speed("fastest")  # Fast rendering (no animation delay)

        # Place food at random grid position (aligned with snake movement)
        self.goto(20 * randint(-13, 13), 20 * randint(-13, 13))