from turtle import Turtle
from random import choice ,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 0.1

class CarManager(Turtle):
    def __init__(self):
        self.all=[]
        self.speed=2
    def create_car(self):
        randam_chance=randint(1,10)
        if randam_chance==1:
            car=Turtle()
            car.penup()
            car.color(choice(COLORS))
            car.shape("square")
            car.shapesize(1,2)
            car.goto(300,randint(-230,230))
            self.all.append(car)
    def move(self):
        for car in self.all:
            car.backward(self.speed)
        
