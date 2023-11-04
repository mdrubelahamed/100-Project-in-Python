# day 25

---
- what?

- In today's lesseon I am working with CSV file and analysing data with pandas library

- project
I am going to build a project where i have to remember 50 states of america i will give input as until i reaches the 50 states names

---

I encounter my csv file open and collect data from it, it's a `weather_data.csv` file where day, tempDegree, Condition mentioned My job is to find to first read every line of data, then with the help of for loop I will take only tempDegree data and store it into a list name temperature
So i did it
```
import csv

with open("project 24/weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))        
    print(temperatures)
```

- Pandas library    
`pip install pandas` - to install pandas library    
In previouly I used so many lines to get only the tempDegree but through pandas library I can do this in so much easy way
```
import pandas

temperatures = []
data = pandas.read_csv("project 24/weather_data.csv)

for t in data["temp"]:
    temperatures.append(t)

```

- url(https://pandas.pydata.org/docs/getting_started/overview.html)     
The two primary data structures of pandas, Series (1-dimensional) and DataFrame (2-dimensional)





Now Date 27/9/23 - I am in the evening learning about data manupulation by pandas library I just get a glimpse of that 

- ⤵️⤵️Intake⤵️⤵️
1. I have study the pandas library seriously and be ready to practice it like math muliple time so it's not about memorizing it's become about practicing

2. There are two types of data - Series, DataFrame
```
data = pandas.read_csv("project 24/weather_data.csv")
print(type(data))
print(type(data["temp"]))

Output: 
<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.series.Series'>
```

#### **NOTE :** `data = pandas.read_csv("project 24/weather_data.csv")`

3. How to convert Series data into different type for ex in dictionary
```
data = pandas.read_csv("project 24/weather_data.csv")
data_dict = data.to_dict()
temp_list = data["temp"].to_list()

Output:
{0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}
[12, 14, 15, 14, 21, 22, 24]
```

4. With the help of Series Computations How to get valuable information (https://pandas.pydata.org/docs/reference/series.html#computations-descriptive-stats)


```
# print avarage temerature
# 1
temp_list = data["temp"].to_list()
print(sum(temp_list) / len(temp_list))

# 2
print(data["temp"].mean())

Output:
17.428571428571427
17.428571428571427
```

another computation example


```
print(data["temp"].max())

print(data["temp"].min())
```

5. There are two way we can hold any csv file coloums   
a. data.temp.max()  
b. data["temp"].max()

both a & b are same     
So Basically in backgound pandas convert the heading in attributes so we can use it as an attributes also   
`data.temp.max()` here .temp is behave like a attributes

an other way is hold the data and use the heading as key
`data[temp].max()`

6. HOW TO GET THE DATA FROM ROWS ?
- If we hold the attributes it return us the whole coloum but if we want a particular row so what we can do is - first hold the entire data the in key we will take    
`data.attributes == "name_of_attributes"`   

```
print(data[data.day == "Monday"])

Output:
      day  temp condition
0  Monday    12     Sunny
```

- we can use it in various way in below we just take the particulat row which has maximum temperature
```
print(data[data.temp == data.temp.max()])
```

- *we can go more further also*


```
monday = data[data.day == "Monday"]
print(monday.condition)

print(data[data.day == "Monday"].condition)


Output:
0    Sunny
Name: condition, dtype: object
```


- *exercise*
Q. Take max temp data from the row and convert the temp in farenheit

```
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]

monday_temp_F = monday_temp * (9/5) + 32
print(monday_temp_F)
```

7. How to create dataframe from scratch ?
- In below I have a dictionary which contains data I am converting the data in `.csv` file and create a .csv file by the program (filename = scratch_data.csv)

```
data_dict = {
    "students": ["John", "Emily", "Michael"],
    "scores": [90, 85, 88]
}

data = pandas.DataFrame(data=data_dict)
print(data)
data.to_csv("project 24/scratch_data.csv")
```

8. I am putting my little knowledge into test
- chapter 229


- Us state game
https://stackoverflow.com/questions/42878641/get-mouse-click-coordinates-in-python-turtle
```
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

```

-------------------------------------------------------------
## Practice Pandas

- how to select a subset of DataFrame

















---
---
---
- Collect code
```
# with open("project 24/weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)
```


```
import pandas

data = pandas.read_csv("./project 24/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"]

color_list = fur_color.to_list()

grey = 0
cinnamon = 0
black = 0

for color in color_list:
    if color == "Gray":
        grey += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Black":
        black += 1

color_dict = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [grey, cinnamon, black]
}

new_data = pandas.DataFrame(data=color_dict)

new_data.to_csv("project 24/squirrel_count.csv")
```


```
# import pandas

# data = pandas.read_csv("project 24/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict["temp"])

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

# print(data["temp"].mean())


# print(data["temp"].max())

# print(data["temp"].min())

# print(data["condition"])
# print(data.condition)


#### ** data.temp.max() == data["temp"].max() is same **

## HOW TO GET THE DATA FROM ROWS
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# print(monday.condition)

# print(data[data.day == "Monday"].condition)


# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
## print(monday_temp)

# monday_temp_F = monday_temp * (9/5) + 32
# print(monday_temp_F)




## How to create dataframe from scratch

# data_dict = {
#     "students": ["John", "Emily", "Michael"],
#     "scores": [90, 85, 88]
# }

# data = pandas.DataFrame(data=data_dict)
# data.to_csv("project 24/scratch_data.csv")



# import pandas

# data = pandas.read_csv("./project 24/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# # fur_color = data["Primary Fur Color"] 


# grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])


# color_dict = {
#     "Fur Color": ["Grey", "Cinnamon", "Black"],
#     "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
# }

# df = pandas.DataFrame(data=color_dict)
# df.to_csv("project 24/squirrel_count.csv")
```


```
#### main.py file unused data
import turtle
import pandas
screen = turtle.Screen()
screen.title("Us state game")
image = "./project 24/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("project 24/50_states.csv")
all_state = data.state.to_list()
guessed_state = []



while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess state name", prompt="Tell another state name?").title()
    
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)

        df = pandas.DataFrame(missing_state)
        df.to_csv("project 24/states_to_learn.csv")
        break  

    if answer_state in all_state:
        guessed_state.append(answer_state)

        state_data = data[data.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)

        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x_cor, y_cor)
        new_turtle.pendown()
        new_turtle.write(answer_state)  # new_turtle.write(state_data.state.item()) ## - Series.item()

```