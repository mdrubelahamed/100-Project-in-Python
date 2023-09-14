from turtle import Turtle

PADDLEPOSITIONS1 = [(-580,-20),(-580,0),(-580,20)]
PADDLEPOSITIONS2 = [(580,-20),(580,0),(580,20)]
MOVE_DISTANCE = 20

class Paddle1:

    def __init__(self): 
        self.segments1 = []
        self.create_paddle()
        self.head1 = self.segments1[0]


    def create_paddle(self):
        for position in PADDLEPOSITIONS1:
            self.add_paddle_segment(position)
    

    def add_paddle_segment(self,position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments1.append(new_segment)


    def move_paddle(self):
        for seg in range(len(self.segments1)-1, 0,-1):
            new_x = self.segments1[seg-1].xcor()
            new_y = self.segments1[seg-1].ycor()
            self.segments1[seg].goto(new_x,new_y)

        self.head1.forward(MOVE_DISTANCE)



class Paddle2:

    def __init__(self): 
        self.segments2 = []
        self.create_paddle()
        self.head2 = self.segments2[0]


    def create_paddle(self):
        for position in PADDLEPOSITIONS2:
            self.add_paddle_segment(position)
    

    def add_paddle_segment(self,position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments2.append(new_segment)


    def new_cordinates(self):
        for seg in range(len(self.segments2)-1, 0,-1):
            new_x = self.segments2[seg-1].xcor()
            new_y = self.segments2[seg-1].ycor()
            self.segments2[seg].goto(new_x,new_y)

        self.head2.forward(MOVE_DISTANCE)


    def move_up(self):
         self.head2.setheading(90)
         self.new_cordinates()


    def move_down(self):
         self.head2.setheading(270)
         self.new_cordinates()