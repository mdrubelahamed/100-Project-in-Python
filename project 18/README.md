## What?
- Draw a square, Dashed line, 
- Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon shape from the same position
- Draw a random walk
- draw a spirograph where several different circle will be drawn and create big circle which looks cool with different colours

---


```
# Draw a square
for i in range(4):
    timmy.forward(100)
    timmy.right(90)


# Draw a Dashed line
for _ in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
```


- Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon shape from the same position
```
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon shape
from turtle import Turtle
import random

colors = ["red", "green", "blue", "yellow", "purple", "orange"]
def forward():
    timmy.forward(100)

corner = 3
def right():
    timmy.right(360//corner)


for j in range(3,11):
    mycolor = random.choice(colors)
    timmy.color(mycolor)
    for i in range(corner):
        right()
        forward()
    corner += 1
```

- Draw a random walk

```
# Draw a random walk (Mathamatics)
timmy.speed(10)
timmy.width(10) #or #timmy.pensize(10)
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
    timmy.pencolor(change_color())

    timmy.setheading(random_dir)  #or #timmy.right(random_dir)
    timmy.forward(30)

```


- draw a spirograph
```
# draw a spirograph where several different circle will be drawn and create big circle which looks cool with different colours
from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("classic")
timmy.color("red")

timmy.speed(70)

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_shape(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_shape(5)


screen = Screen()
screen.exitonclick()

```


- draw random walk with random **bg color**
```
import turtle
import random
turtle.colormode (255)
i = 0
while i < 20:
    i += 1
    R = random.randrange (255)
    G = random.randrange (255)
    B = random.randrange (255)
    turtle.bgcolor (R,G,B,)
    turtle.color (R,G,B,)
    ang = random.randrange (360)
    turtle.width (5)
    turtle.forward (50)
    turtle.setheading(ang)

screen = turtle.Screen()
screen.exitonclick()
```