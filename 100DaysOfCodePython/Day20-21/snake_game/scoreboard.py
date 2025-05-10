from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)


    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

