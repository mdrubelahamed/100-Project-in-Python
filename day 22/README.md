# PING PONG GAME

## What?
- Create Screen
- Create Paddle in oop
- move the paddle



#### lost code
```
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
```



```
from turtle import Turtle

MOVE_DISTANCE = 20
Y_AXIX_SCREEN = 260
PADDLE_POSITION = 479

class Paddle:

    def __init__(self): 
        self.create_paddle()

    def create_paddle(self,x_pos,y_pos):
            self.paddle = Turtle("square")
            self.paddle.shapesize(stretch_wid=5, stretch_len=1)
            self.paddle.color("white")
            self.paddle.penup()
            self.paddle.goto(x_pos, y_pos)


    def move_up(self):
        if self.paddle.ycor() < 260:
            new_y = self.paddle.ycor() + MOVE_DISTANCE
            self.paddle.goto(self.paddle.xcor(),new_y)


    def move_down(self):
        if self.paddle.ycor() > -260:
            new_y = self.paddle.ycor() - MOVE_DISTANCE         
            self.paddle.goto(self.paddle.xcor(),new_y)
```



## NOTE how i am doing it?
-- First i setup a 1000,600 screen  

then i create a "Paddle" with where i use "Turtle" as a super class 
the i design two move_up and move_down function 
`self.shapesize(stretch_wid=5, stretch_len=1)` here i strech my paddle length multiply by 5 

- create the ball?
first i create a file called `ball.py` the inside this i create a ball turtle, and create a move function which change the .xcor() and .ycor()  
so it's looks that the ball is moving
    & i added also sleep time so the ball move a bit slow which help us to catch the ball
