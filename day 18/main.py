from turtle import Turtle, Screen
from random import choice
from colors import colors

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")



# # Draw a square
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# # Draw a Dashed line
# for _ in range(10):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)



# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon shape

def forward():
    timmy_the_turtle.forward(100)

corner = 3
def right():
    timmy_the_turtle.right(360//corner)


for j in range(3,11):
    mycolor = choice(colors)
    timmy_the_turtle.color(mycolor)
    for i in range(corner):
        right()
        forward()
    corner += 1










screen = Screen()
screen.exitonclick()
