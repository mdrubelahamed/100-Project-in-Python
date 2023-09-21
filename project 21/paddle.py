from turtle import Turtle

MOVE_DISTANCE = 20
Y_AXIX_SCREEN = 260

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("blue")
        self.penup()
        self.goto(position)


    def move_up(self):
        if self.ycor() < Y_AXIX_SCREEN:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(),new_y)


    def move_down(self):
        if self.ycor() > -Y_AXIX_SCREEN:
            new_y = self.ycor() - MOVE_DISTANCE         
            self.goto(self.xcor(),new_y)