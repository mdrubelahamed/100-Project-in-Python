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


- Draw a square