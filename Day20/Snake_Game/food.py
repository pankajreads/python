from turtle import Turtle
from random import randint, choice

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color(choice(["red", "green", "blue"]))
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.goto(20 * randint(-13, 13), 20 * randint(-13, 13))