from turtle import Turtle
class Snake:
    def __init__(self):
        self.body = []
        self.direction="Right"
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            s = Turtle()
            s.color("white")
            s.shape("square")
            s.penup()
            s.setheading(0)
            s.goto(-20 * i, 0)
            self.body.append(s)

    def move(self):
        if self.direction == "UP":
            self.body[0].setheading(90)
        elif self.direction == "DOWN":
            self.body[0].setheading(270)
        elif self.direction == "LEFT":
            self.body[0].setheading(180)
        elif self.direction == "RIGHT":
            self.body[0].setheading(0)

        for i in range(len(self.body)-1, 0, -1):
            x = self.body[i-1].xcor()
            y = self.body[i-1].ycor()
            self.body[i].goto(x, y)

        self.body[0].forward(20)

    def increase_snake(self):
        s = Turtle()
        s.shape("square")
        s.color("white")
        s.penup()

        last = self.body[-1]
        s.goto(last.position())

        self.body.append(s)