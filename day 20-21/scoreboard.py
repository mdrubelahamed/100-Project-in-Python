from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        