from turtle import Turtle,Screen
import random

# # this is not the optimal way to doing the turtle race - go check out main.py file
# screen = Screen()
# screen.setup(width=600,height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race, Enter a color: ")
# print(user_bet)

# a = Turtle()
# b = Turtle()
# c = Turtle()
# d = Turtle()
# e = Turtle()

# a.color("red")
# b.color("green")
# c.color("blue")
# d.color("purple")
# e.color("yellow")

# turtle_list = [a,b,c,d,e]
# x = -280
# y = 200


# for turtle in turtle_list:
#     y -= 40
#     turtle.shape("turtle")
#     turtle.penup()
#     turtle.goto(x, y)
#     # turtle.pendown()

# should_move = True
# while should_move:
#     for turtle in turtle_list:
#         turtle.penup()
#         turtle.forward(random.randint(0,10))
#         if turtle.xcor() > 260:  # Check if the turtle's x-coordinate is <= -300
#             should_move = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"you won, The {winning_color} turtle is the winning turtle")
#             else:
#                 print(f"you lost, The {winning_color} turtle is the winning turtle")





##########################################################
screen = Screen()
screen.setup(width=600,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race, Enter a color: ")
print(user_bet)

# a = Turtle()
# b = Turtle()
# c = Turtle()
# d = Turtle()
# e = Turtle()

# a.color("red")
# b.color("green")
# c.color("blue")
# d.color("purple")
# e.color("yellow")


colors = ["red", "green", "blue", "purple", "yellow"]
turtle_list = []
x = -280
y = 200
    
for i in range(0,5):
    # new_turtle = Turtle()
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    y -= 40
    new_turtle.penup()
    new_turtle.goto(x, y)
    turtle_list.append(new_turtle)
    

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


# print(turtle_list)
screen.exitonclick()