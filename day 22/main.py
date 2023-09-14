from turtle import Screen
from paddle import Paddle1,Paddle2

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

paddle1 = Paddle1()
paddle2 = Paddle2()

paddle1.create_paddle()
paddle2.create_paddle()

screen.update()




screen.exitonclick()

