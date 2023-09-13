# Python Snake Game
- Before OOP snake code snippet'
```
from turtle import Turtle, Screen 
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")
screen.tracer(0)

#Create a snake body
segments = []
# starting_postion = [(0,0), (-20,0), (-40,0)]
x_pos = 0
y_pos = 0

for i in range(0,3):
    shape = Turtle(shape="square")
    shape.color("white")
    shape.penup()
    shape.goto(x=x_pos,y=y_pos)  # shape.goto(starting_postion[i])
    segments.append(shape)
    x_pos -= 20


game_is_on = True
while game_is_on:
    screen.update() 
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    time.sleep(0.3)


    # screen.listen()
    # def turn_up():
    #     if segments[0].xcor() > 0:
    #         segments[0].left(90)
    #     else:
    #         segments[0].right(90)
    # screen.onkey(fun=turn_up, key="Up")






screen.exitonclick()
```


## Changing turtle head only
```from turtle import Turtle

STARTING_POSITIONS = [(-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_head()
        self.create_snake()
        self.head = self.segments[0]


    def create_head(self):
        new_head = Turtle(shape="turtle")
        new_head.color("red")
        new_head.penup()
        new_head.goto(x=0,y=0)
        self.segments.append(new_head)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="circle")
            new_segment.color("red")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

....
....
....
```


## Control the Snake