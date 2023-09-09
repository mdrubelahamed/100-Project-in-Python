from turtle import Turtle,Screen
import turtle
import random


tim = Turtle()
screen = Screen()

tim.speed("fast")

def move_forward():
    tim.forward(20)

screen.listen()

screen.onkey(key="f", fun=move_forward)

screen.exitonclick()