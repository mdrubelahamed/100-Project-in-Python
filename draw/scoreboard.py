from turtle import Turtle
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        with open("draw/snake_data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.create_scoreboard()

    def create_scoreboard(self):
        self.clear()
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.goto(-30,270)
        self.pendown()
        self.write(f"Score: {self.score}     Higherst Score: {self.high_score}", align="center", font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.create_scoreboard()
        
    def save_highest_score(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("draw/snake_data.txt", mode="w") as file:
                file.write(str(self.high_score))
                
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER!", align="center", font=FONT)