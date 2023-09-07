## Turtle Graphics, Tuples And Importing Modules

- timmy the turtle
```
from turtle import Turtle,Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")    
timmy_the_turtle.color("green")

def forward_66():
    timmy_the_turtle.forward(66)

def left_60():
    timmy_the_turtle.left( 60)



# Hexagon
timmy_the_turtle.right(90)
for i in range(6):
    forward_66()
    left_60()


# #################
# # Hexagon
# timmy_the_turtle.right(60)
# for i in range(6):
#     forward_66()
#     left_60()
```

- Draw a square, Dashed line, 
- Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon shape
```
# Draw a square
for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


# Draw a Dashed line
for _ in range(10):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)



# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon shape

def forward():
    timmy_the_turtle.forward(100)

corner = 3
def right():
    timmy_the_turtle.right(360//corner)


for j in range(3,11):
    mycolor = random.choice(colors)
    timmy_the_turtle.color(mycolor)
    for i in range(corner):
        right()
        forward()
    corner += 1
```

- DRAW A RANDOM WALK
```
# Draw a random walk (Mathamatics)
timmy_the_turtle.speed(10)
timmy_the_turtle.width(10) #or #timmy_the_turtle.pensize(10)
direction1 = [0,90,180,270]

# Setting the colormode 
turtle.colormode(255)
# screen = Screen()
# screen.colormode(255)

def change_color():
    """return a set of (r,g,b) colors"""
    return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

for _ in range(200):
    random_dir = random.choice(direction1)
    timmy_the_turtle.pencolor(change_color())

    timmy_the_turtle.setheading(random_dir)  #or #timmy_the_turtle.right(random_dir)
    timmy_the_turtle.forward(30)

```
-
-
```
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("classic")
timmy.color("red")

# # Draw spirograph
# timmy.speed(70)

# turtle.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# def draw_shape(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)

# draw_shape(5)


# colormode
# x = turtle.colormode(255)
# print(x)

# import turtle
# import random
# turtle.colormode (255)
# i = 0
# while i < 20:
#     i += 1
#     R = random.randrange (255)
#     G = random.randrange (255)
#     B = random.randrange (255)
#     turtle.bgcolor (R,G,B,)
#     turtle.color (R,G,B,)
#     ang = random.randrange (360)
#     turtle.width (5)
#     turtle.forward (50)
#     turtle.setheading(ang)



screen = Screen()
screen.exitonclick()

```