from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")
screen.tracer(0)

#Create a snake body
segments = []
# starting_postion = [(0,0), (-20,0), (-40,0)]
x_pos = 0
y_pos = 0


for i in range(0,3):
    shape = Turtle(shape="square")
    shape.color("white")
    shape.penup()
    shape.goto(x=x_pos,y=y_pos)  # shape.goto(starting_postion[i])
    segments.append(shape)
    x_pos -= 20


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
     
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)

    screen.listen()

    def turn_left():
        segments[0].left(90)
    
 











screen.exitonclick()