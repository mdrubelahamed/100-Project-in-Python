from turtle import Turtle,Screen
from car import Car
import time

POSITIONS = [(380,-210), (380,-140), (380,-70), (380,0), (380,70), (380,140), (380,210)]
screen = Screen()
screen.title("Car Game!")
screen.setup(width=800, height=600)
screen.colormode(255)
screen.tracer(0)

cars = []




game_is_on = True
while game_is_on:
    for i in range(0,7):
        new_car = Car(POSITIONS[i])
        cars.append(new_car)

        time.sleep(0.9)
        screen.update()

        for car in cars:
            car.move()
            if car.xcor() < -400:
                car(POSITIONS[i])
        

screen.exitonclick()