from turtle import Turtle

PADDLEPOSITIONS1 = [(-580,-20),(-580,0),(-580,20)]
PADDLEPOSITIONS2 = [(580,-20),(580,0),(580,20)]


class Paddle1:

    def __init__(self): 
        self.segments1 = []
        self.create_paddle()

    def create_paddle(self):
        for position in PADDLEPOSITIONS1:
            self.add_paddle_segment(position)
    

    def add_paddle_segment(self,position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments1.append(new_segment)


class Paddle2:

    def __init__(self): 
        self.segments1 = []
        self.create_paddle()

    def create_paddle(self):
        for position in PADDLEPOSITIONS2:
            self.add_paddle_segment(position)
    

    def add_paddle_segment(self,position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments1.append(new_segment)
