## Inheritance
```
#####################################
# Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exahle.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doint it underwater")

    def swim(self):
        print("moving in water")

rui = Fish()

rui.swim()
rui.breathe()
print(rui.num_eyes)
```


## Control the Snake


## COMPELET GAME 
```
from turtle import Screen  # Turtle,
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to The Snake Game!")
screen.tracer(0)


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
    time.sleep(0.2)
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
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
```

## Slicing
- Example

```
piano_keys = ["a", "b", "c", "d", "e", "f", "g"] 
print(piano_keys[2:5])       # Output: ['c', 'd', 'e']
```

```
...
complete code before tail
....

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()
```

- Note That day 20 has also include day21