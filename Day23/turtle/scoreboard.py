FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.color("orange")
        self.write(f"Score{self.score}",align="left",font=FONT)
    def increase(self):
        self.clear()
        self.score+=1
        self.write(f"Score{self.score}",align="left",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)