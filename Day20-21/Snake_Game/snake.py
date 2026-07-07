from turtle import Turtle

class Snake:
    def __init__(self):
        self.body = []  # List to store all snake segments
        self.direction = "RIGHT"  # Initial direction (⚠️ fixed case)
        self.create_snake()  # Create starting snake

    def create_snake(self):
        # Create 3 starting segments
        for i in range(3):
            s = Turtle()
            s.color("white")  # Snake color
            s.shape("square")  # Each segment is square
            s.penup()  # Prevent drawing lines
            s.setheading(0)  # Facing right
            s.goto(-20 * i, 0)  # Position segments in a row
            self.body.append(s)  # Add segment to body list

    def move(self):
        # Set direction of head based on current direction
        if self.direction == "UP":
            self.body[0].setheading(90)
        elif self.direction == "DOWN":
            self.body[0].setheading(270)
        elif self.direction == "LEFT":
            self.body[0].setheading(180)
        elif self.direction == "RIGHT":
            self.body[0].setheading(0)

        # Move body: each segment follows the one in front
        for i in range(len(self.body) - 1, 0, -1):
            x = self.body[i - 1].xcor()
            y = self.body[i - 1].ycor()
            self.body[i].goto(x, y)

        # Move head forward
        self.body[0].forward(20)

    def increase_snake(self):
        # Add new segment at the position of the last segment
        s = Turtle()
        s.shape("square")
        s.color("white")
        s.penup()

        last = self.body[-1]  # Get last segment
        s.goto(last.position())  # Place new segment at same spot

        self.body.append(s)  # Add to snake body