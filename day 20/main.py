from turtle import Screen  # Turtle,
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from difficulty import Difficulty
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to The Snake Game!")
screen.tracer(0)



difficulty_choice = screen.textinput(title="CHOOSE LEVEL", prompt="Choose difficulty \n(easy, medium, hard)").lower()
game_level = Difficulty(difficulty_choice)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep(0.2)
    time.sleep(game_level.get_sleep_time())
    snake.move()

    # Detect collision with food, increase the score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()