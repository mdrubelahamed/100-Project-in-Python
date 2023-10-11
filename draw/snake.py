from turtle import Turtle

STARTING_POSITON = [(0, 0), (-20, 0), (-40, 0)]

class Snake():  
    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0]


    def create_body(self):
        for position in STARTING_POSITON:
            self.add_segment(position)

    def add_segment(self,pos):
        new_segment = Turtle("circle")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    
    def extend_segment(self):
        self.add_segment(self.segments[len(self.segments) -1].pos())


    def move(self):
        for pos in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[pos - 1].xcor()
            new_y = self.segments[pos - 1].ycor()
            
            self.segments[pos].goto(new_x, new_y)

        self.head.forward(20)
        
        
    def game_over(self):
        for seg in self.segments:
            seg.goto(1000,1000)
            self.segments.clear()


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    

        