from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)


r_paddle = Paddle((480,0))
l_paddle = Paddle((-480,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 440 or ball.distance(l_paddle) < 50 and ball.xcor() < -440:
        ball.bounce_x()

    # Detect when the ball misses the paddle 

    # Detect when R Paddle misses
    if ball.xcor() > 490:
        ball.reset_postion()
        scoreboard.l_point()


    # Detect when L Paddle misses
    if ball.xcor() < -490:
        ball.reset_postion()
        scoreboard.r_point()

screen.exitonclick()

