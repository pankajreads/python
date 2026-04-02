from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.seth(45)
        self.penup()  
    def bounce(self):
        if self.ycor() <-280 or self.ycor()>280:
            self.seth(360-(self.heading()))
        
