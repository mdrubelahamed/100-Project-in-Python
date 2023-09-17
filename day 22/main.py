from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)


r_paddle = Paddle((470,0))
l_paddle = Paddle((-470,0))
ball = Ball()


screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()






screen.exitonclick()

