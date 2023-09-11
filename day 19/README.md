## listen() method in turtle graphics  
### onkey(key=listiningkey, fun=function()) method in turtle graphics  

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


## Higher Order Function
- when a function use another function as a parameter then it's called higher order function
```
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def calculator(n1,n2,func): # Here calculator is a higher order function, 'cause it's using another function as parameter
    return func(n1,n2)

print(calculator(5,2,divide))
```


### Make a turle which can go forward, backward, clockwise and anti-clockwise
```
from turtle import Turtle,Screen
import turtle
import random


tim = Turtle()
screen = Screen()

# tim.speed("fast")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    # tim.left(10) ## or

def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    # tim.right(10) ##or

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_counter_clockwise, key="a")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=clear_drawing, key="c")

screen.exitonclick()

```


## turtle race program
### 1
```
from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=600,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race, Enter a color: ")
print(user_bet)

a = Turtle()
b = Turtle()
c = Turtle()
d = Turtle()
e = Turtle()

a.color("red")
b.color("green")
c.color("blue")
d.color("purple")
e.color("yellow")

turtle_list = [a,b,c,d,e]
x = -280
y = 200


for turtle in turtle_list:
    y -= 40
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x, y)
    # turtle.pendown()

should_move = True
while should_move:
    for turtle in turtle_list:
        turtle.penup()
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 260:  # Check if the turtle's x-coordinate is <= -300
            should_move = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won, The {winning_color} turtle is the winning turtle")
            else:
                print(f"you lost, The {winning_color} turtle is the winning turtle")




screen.exitonclick()
```

### 2
```
from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=600,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race, Enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_pos = -280
y_pos = 200
all_turtles = []

for t_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t_index])
    y_pos -= 40
    new_turtle.goto(x=x_pos, y=y_pos)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 260:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the wining turtle")
            else:
                print(f"You lost! The {winning_color} turtle is the wining turtle")

        turtle.forward(random.randint(0,10))



screen.exitonclick()
```

# Exapand
..........