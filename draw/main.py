from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Py Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

not_endgame = True
while not_endgame:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.reset_position()
        snake.extend_segment()
        scoreboard.increase_score()

    # Detect collisioin with screen
    if snake.head.xcor() > 293 or snake.head.xcor() < -293 or snake.head.ycor() > 293 or snake.head.ycor() < -293:
        scoreboard.save_highest_score()
        scoreboard.game_over()
        not_endgame = False


    # Detect collison with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        else:
            if snake.head.distance(segment) < 10:
                snake.game_over()
                scoreboard.save_highest_score()
                scoreboard.game_over()
                not_endgame = False


screen.exitonclick()