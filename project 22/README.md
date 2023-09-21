- day 23











my `car.py` code
``` from turtle import Turtle
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
```




- Note - I just change all folder name day to project... here is the  code
```
import os

# Define the path to the parent folder
parent_folder = os.getcwd()

# Loop through the folders and rename them
for day_number in range(1, 22):
    old_folder_name = os.path.join(parent_folder, f'day {day_number}')
    new_folder_name = os.path.join(parent_folder, f'project {day_number}')
    
    # Use os.rename to rename the folder
    os.rename(old_folder_name, new_folder_name)

print("Folders renamed successfully.")
```
