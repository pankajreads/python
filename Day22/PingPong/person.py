from turtle import Turtle
class Person(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.seth(90)
        self.shapesize(1,4)
        self.penup()
        self.goto(x,y)