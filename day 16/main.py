# import another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.color("green")
timmy.shape("turtle")
timmy.forward(100)
timmy.right(angle=90)
timmy.forward(100)
timmy.right(angle=90)
timmy.forward(100)
timmy.right(angle=90)
timmy.forward(100)
# timmy.right(angle=90)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
