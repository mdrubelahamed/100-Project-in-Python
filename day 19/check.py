from turtle import Turtle, Screen
import turtle
import random


tim = Turtle()
screen = Screen()

tim.speed("fast")
turtle.colormode(255)
def random_color():
    R = random.randrange(0, 255)
    G = random.randrange(0, 255)
    B = random.randrange(0, 255)
    return (R, G, B)

# Define a random color once
current_color = random_color()

def set_random_color():
    global current_color
    current_color = random_color()
    tim.pencolor(current_color)

def move_forwards():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def draw_shape(shape_function):
    set_random_color()  # Set random pen color
    shape_function()

def draw_triangle():
    for _ in range(3):
        tim.forward(100)
        tim.right(120)

def draw_square():
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
        tim.right(36)  # 360/number_of_sides

screen.listen()
screen.onkey(key="m", fun=move_forwards)
screen.onkey(key="b", fun=move_backward)

# Add other shape key bindings similarly...
screen.onkey(key="3", fun=lambda: draw_shape(draw_triangle))
screen.onkey(key="4", fun=lambda: draw_shape(draw_square))
screen.onkey(key="5", fun=lambda: draw_shape(draw_pentagon))
screen.onkey(key="6", fun=lambda: draw_shape(draw_hexagon))
screen.onkey(key="7", fun=lambda: draw_shape(draw_heptagon))
screen.onkey(key="8", fun=lambda: draw_shape(draw_octagon))
screen.onkey(key="9", fun=lambda: draw_shape(draw_nonagon))
screen.onkey(key="0", fun=lambda: draw_shape(draw_decagon))

screen.exitonclick()
