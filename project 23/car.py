from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(self.random_color())
        self.penup()
        self.goto(pos)

    def random_color(self):
        R = random.randint(50,255)
        G = random.randint(50,255)
        B = random.randint(50,255)
        return (R,G,B)
    
    def move(self):
        self.backward(random.randint(1,10))
    
    def reset_position(self,pos2):
        self.goto(pos2)