- listen() function in turtle graphics  
- onkey(key=listiningkey, fun=function()) function in turtle graphics  

```
from turtle import Turtle,Screen
import turtle
import random


tim = Turtle()
screen = Screen()

tim.speed("fast")
turtle.colormode(255)

def random_color():
    R = random.randrange(0,255)
    G = random.randrange(0,255)
    B = random.randrange(0,255)
    return(R,G,B)

def draw_shape(set_color):
    
    
    def move_forwards():
        tim.forward(20)

    def move_backward():
        tim.backward(20)

    def draw_triangle():
        tim.pencolor(set_color())
        for _ in range(3):
            tim.forward(100)
            tim.right(120)

    def draw_square():
        tim.pencolor(set_color())
        for _ in range(4):
            tim.forward(100)
            tim.right(90)

    def draw_pentagon():
        for _ in range(5):
            tim.forward(100)
            tim.right(72)

    def draw_hexagon():
        for _ in range(6):
            tim.forward(100)
            tim.right(60)

    def draw_heptagon():
        for _ in range(7):
            tim.forward(100)
            tim.right(360/7)

    def draw_octagon():
        for _ in range(8):
            tim.forward(100)
            tim.right(45)

    def draw_nonagon():
        for _ in range(9):
            tim.forward(100)
            tim.right(40)

    def draw_decagon():
        for _ in range(10):
            tim.forward(100)
            tim.right(36) # 360/number_of_sides


    screen.listen()
    screen.onkey(key="m", fun=move_forwards)
    screen.onkey(key="b", fun=move_backward)
    screen.onkey(key="3", fun=draw_triangle)
    screen.onkey(key="4", fun=draw_square)
    screen.onkey(key="5", fun=draw_pentagon)
    screen.onkey(key="6", fun=draw_hexagon)
    screen.onkey(key="7", fun=draw_heptagon)
    screen.onkey(key="8", fun=draw_octagon)
    screen.onkey(key="9", fun=draw_nonagon)
    screen.onkey(key="0", fun=draw_decagon)


draw_shape(set_color=random_color)

screen.exitonclick()
```