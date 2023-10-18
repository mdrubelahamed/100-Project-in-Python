```
import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

class Level:

    def chance(self,user_input):
        if user_input == "easy":
            return EASY_LEVEL_ATTEMPTS
        elif user_input == "hard":
            return HARD_LEVEL_ATTEMPTS
        else:
            return EASY_LEVEL_ATTEMPTS
        

    def level_choice(self):
        user_level = input("Choose your playing level? 'easy' or 'hard'-")
        self.chance(user_input=user_level)
    




class Guess(Level):

    def __init__(self):
        super().__init__()
        self.computer_number = random.randint(1,100)

    def user_guess(self):
        self.guess_process(self.computer_number)


    

    def check_number(self,user_num,comp_num,attempts):
        if user_num == comp_num:
            game_on = False
            print("you guessed correct!")
            print(f"The Correct Nubmer is {comp_num}")
        elif user_num > comp_num:
            print("Too High")
            return attempts  - 1
        elif user_num < comp_num:
            print("Too Low")
            return attempts  - 1
        
       
    def attempts_check(self,comp_num):
        game_on = True
        while user_number != comp_num :
            print(f"You have {attempts} left")
            user_number = int(input("Make a guess: ")) 
            self.check_number(user_num=user_number,comp_num=self.computer_number,attempts=self.attempts)

```

-----------------------------------------------------------------------------
```
"""
You are building a weather application that needs to store temperature data for different cities. Create a dictionary where the keys are city names and the values are lists of temperature readings. Perform the following tasks:

Add temperatures for at least 3 cities.
Add a new temperature to an existing city.
Remove the last temperature from a city.
Print the average temperature for each city.
"""

temperature_database = {
    "kolkata": [33,40,30,24],
    "raiganj": [34,38,29],
    "chennai": [22,37,25,29]
}
print(temperature_database)

temperature_database["raiganj"].append(50)
print(temperature_database)

temperature_database["raiganj"].pop()
print(temperature_database)

for temparature in temperature_database:
    toatal_temperature = 0
    values = temperature_database[temparature]
    values_length = len(values)
    for value in values:
        toatal_temperature += value
    avarage = round(toatal_temperature/values_length,2)
    print(avarage)
```


"""
Problem 3: Sales Analytics

You have sales data in the form of a list of dictionaries, where each dictionary represents a sale with 'product', 'quantity', and 'price'. Calculate the total sales for each product and store it in a dictionary where the product names are keys, and the total sales are values.

Problem 4: English to Spanish Dictionary

Create a simple English-to-Spanish dictionary. You should be able to add new word translations, update existing ones, and look up translations by providing an English word as input.

Problem 5: Student Records

You are managing student records. Create a dictionary where the keys are student IDs, and the values are dictionaries containing 'name', 'age', and 'grades'. Implement functions to:

Add a new student record.
Update a student's information (name, age, or grades).
Remove a student record by ID.
Calculate the average grade for a given student.
These problems cover various aspects of dictionary manipulation and usage. Solving them will help you gain a deep understanding of dictionaries in Python and their practical applications. Feel free to start with any problem that interests you the most!    
"""


#########################################################
```
# Nested Dictionary
org_str = {
    "company_name": "ABC limited",
    "departments": {
        "HR": {
            "employees": {
                "101": {
                        "name": "Rubel",
                        "position": "HR Head",
                        "salay": 60000,
                },
                "102": {
                        "name": "Bob",
                        "position": "Junior HR",
                        "salay": 25000,
                }
            },
        },
        "IT":{
            "employees":{
                "201": {
                    "name": "Rohan",
                    "position": "Seniour IT Manager",
                    "salary": 100000
                },
                "202": {
                    "name": "Jojo",
                    "position": "Jounier IT Devloper",
                    "salary": 30000
                }
            }
        }
        
    }
}



# Find Jojo Salary

print(org_str["departments"]["IT"]["employees"]["202"]["salary"])

```


---
> dir(__builtins__)

---

-------------------------------------------------------------------------------------------------------------
# Snake game whole code 
- `main.py`
```
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
```
- `snake.py`
```
from turtle import Turtle

STARTING_POSITON = [(0, 0), (-20, 0), (-40, 0)]

class Snake():  
    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0]


    def create_body(self):
        for position in STARTING_POSITON:
            self.add_segment(position)

    def add_segment(self,pos):
        new_segment = Turtle("circle")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    
    def extend_segment(self):
        self.add_segment(self.segments[len(self.segments) -1].pos())


    def move(self):
        for pos in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[pos - 1].xcor()
            new_y = self.segments[pos - 1].ycor()
            
            self.segments[pos].goto(new_x, new_y)

        self.head.forward(20)
        
        
    def game_over(self):
        for seg in self.segments:
            seg.goto(1000,1000)
            self.segments.clear()


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
```

- `food.py`
```
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    
        self.color("lightgreen")
        self.penup()
        self.speed(10)
        self.reset_position()
        
    def reset_position(self):
        self.goto(random.randint(-280,280), random.randint(-280,260))


```
- `scoreboard.py`
```
from turtle import Turtle
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        with open("draw/snake_data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.create_scoreboard()

    def create_scoreboard(self):
        self.clear()
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.goto(-30,270)
        self.pendown()
        self.write(f"Score: {self.score}     Higherst Score: {self.high_score}", align="center", font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.create_scoreboard()
        
    def save_highest_score(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("draw/snake_data.txt", mode="w") as file:
                file.write(str(self.high_score))
                
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER!", align="center", font=FONT)
```

---
-------------------------------------------------------------------------------------------------------------

- csv data
```
    # data = file.readlines()
    # print(data)
```

```
# import csv
# with open("draw/weather_data.csv") as file:
#     data = list(csv.reader(file, delimiter=","))
#     # print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


import csv
with open("draw/weather_data.csv") as file:
    data = csv.reader(file, delimiter=',')
    # print(data)
    days = []
    temperatures = []
    conditions = []
    for row in data:
        if row[0] != 'day' or row[1] != 'temp' or row[2] != 'condition':
            days.append(row[0]) 
            temperatures.append(int(row[1])) 
            conditions.append(row[2]) 
    print(days)
    print(temperatures)
    print(conditions)```

```

```
import pandas

df = pandas.DataFrame(
    {
        "Name": [
            "Vikrant Sinha", "Koma Parekh", "Priya Malhotra", "Avika Gaur", "Priyanka Kapoor"
            ],
        "City": [
            "Dehradun", "Ahemadabad", "Mumbai", "Ambala", "Delhi"
            ],
        "State": [
            "Uttrakhand", "Gujrat", "Maharastra", "Punjab", "Delhi"
        ],
        "Postal Code": [
            233001, 592114, 245771, 301137, 243722
        ],
        "Age": [
            22, 25, 35, 46, 20
        ],
    }
)

# print(df)

# print(df["Postal Code"])
# print(df.describe())

print(df.index)


# ages = pandas.Series([22,25,20,46,25], name="Age")
# print(ages)
# print(ages.max())
```