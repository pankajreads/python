from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()  # Initialize Turtle

        self.score = 0  # Current game score
        self.color("white")  # Text color

        # Read high score from file
        with open("./high_score.txt") as file:
            content = file.read().strip()  # Remove spaces/newlines
            self.hscore = int(content) if content.isdigit() else 0  # Safe conversion

        self.penup()  # Don't draw lines
        self.hideturtle()  # Hide turtle cursor
        self.goto(0, 260)  # Position at top of screen

        self.update_score()  # Display initial score

    def update_score(self):
        self.clear()  # Clear previous text

        # Display current score and high score
        self.write(f"Score: {self.score} High Score {self.hscore}",
                   align="center",
                   font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1  # Increase current score

        # Check if new high score is achieved
        if self.score > self.hscore:
            self.hscore = self.score

            # Save new high score to file
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.hscore))

        self.update_score()  # Refresh display

    def game_over(self):
        self.goto(0, 0)  # Move to center

        # Display game over message
        self.write("GAME OVER",
                   align="center",
                   font=("Arial", 20, "bold"))