### day 23
---
- what?  
- project  
The project is basically a turtle cross the road means one side of the screen to an another side, in between there are many cars which are coming if the turtle make collision with any cars the game will over, and after reaching on the other side the level will be increased, meaning the car will get faster on each level and the turtle will be back on his orginal position

- lesson  
Building project with the help of class, oop concept, in first it looks really hard to me but the more i learn the more it's become cool for me and now i feel it's is more efficient way of creating project, we should build project around oop concept
i learn about .xcor() and .ycor() which is really efficient for changing position, detecting position,

in `car_manager.py` file I learn how to generate mulitple cars at the same time, and also at the same time choosing random colors for every particular car,  
  
  
*important new* - I learn how to slow the cars speed or as i can say how to make optimal speed for cars,  
by using random number choice
```
random_chance = random.randint(1,19)
            if random_chance == 1:
            ...
```
so in here as you can see i use ` if random_chance == 1` which will reduce to generate cars, it will only generate cars when the ranodm change will be equal = 1


---




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
