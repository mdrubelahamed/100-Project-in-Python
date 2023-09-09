from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=600,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? \n(red, orange, yellow, green, blue, purple) \nEnter a color: ")
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