# with open("project 25/weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open("project 25/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas as pd

# data = pd.read_csv("project 25/weather_data.csv")
# # print(data)
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# # avarage temperature
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

# # avarage temperature in the Series way 
# print(data["temp"].mean())

# Max value by Series
# print(data["temp"].max())
# print(data["temp"].nlargest())

# # Get data in column
# # How pandas take every column head and bts make it a attribute, that's why we can access data.temp (.temp because of attribute )
# print(data["temp"])
# print(data.temp)

# # Get data in row
# print(data[data["day"] == "Monday"])

# print(data[data.day == "Monday"])


# # Get max temp data row
# print(data[data.temp == data.temp.max()])

# # get furture to get a particular value from a particular row
# max_temp_row = data[data.temp == data.temp.max()]
# print(max_temp_row.condition)


# # challenge - Monday's temperature into fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# # print(monday_temp)
# monday_temp_F = (monday_temp * 9/5) + 32
# print(monday_temp_F)


# # Create DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "Rohan", "James"],
#     "scores": [76, 56, 65]
# }

# df = pd.DataFrame(data_dict)
# # print(df)
# df.to_csv("project 25/student_data_from_scratch.csv")



# ##############################
# # Squirel Count

# import pandas as pd

# data = pd.read_csv("project 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # fur_color = data["Primary Fur Color"]
# # print(fur_color)

# grey_count = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
# cinnamon_count = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
# black_count = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()


# # print(grey_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_count, cinnamon_count, black_count]
# }
# # print(data_dict)

# df = pd.DataFrame(data_dict)

# df.to_csv("project 25/squirrel_count.csv")



######################### USA STATE QUIZ ########################################################
import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("Us States Game")

image = "project 25/blank_states_img.gif"
screen.addshape(image, shape=None)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

data = pd.read_csv("project 25/50_states.csv")

guessed_states = []
score = 0
all_states = data.state.to_list()
# print(all_states)

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{score}/50 Guess state name", prompt="Type a state name?").title()

    if answer_state == "Exit":
        # missed_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        
        missed_states = [state for state in all_states if state not in guessed_states]
        df = pd.DataFrame(missed_states)
        df.to_csv("project 25/USA_forgot_states_name.csv", index=False)
        break


    if answer_state in all_states:
        score += 1
        guessed_states.append(answer_state)
        state_row = data[data.state == answer_state]  
        x_cor = int(state_row.x.iloc[0])
        y_cor = int(state_row.y.iloc[0])
        # print(x_cor, y_cor)
        
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x_cor, y_cor)
        new_turtle.pendown()
        new_turtle.color("green")
        new_turtle.write(answer_state, font=("Arial",8,"normal"))
        



######################### INDIAN STATE QUIZ ########################################################
# import turtle
# import pandas as pd
# screen = turtle.Screen()
# # width = height = 1000
# # screen.screensize(width, height)

# img = "project 25/Indian-state.gif"
# screen.addshape(img)
# turtle.shape(img)

# data = pd.read_csv("project 25/Indian_state_data.csv")

# all_states = data.state.to_list()

# guessed_states = []
# score = 0

# while len(guessed_states) < 29:
#     answer_state = screen.textinput(title=f"{score}/28 Guess State Name", prompt="Type a state name?").title()

#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         state_row = data[data.state == answer_state]
#         x_cor = int(state_row.x.iloc[0])
#         y_cor = int(state_row.y.iloc[0])
#         # print(x_cor, y_cor)
        
#         new_turtle = turtle.Turtle()
#         new_turtle.hideturtle()
#         new_turtle.penup()
#         new_turtle.goto(x_cor, y_cor)
#         new_turtle.pendown()
#         new_turtle.write(answer_state, align="center", font=("Arial", 7, "normal"))


#     if answer_state == "Exit":
#         # forgot_states = []
#         # for state in all_states:
#         #     if state not in guessed_states:
#         #         forgot_states.append(state)
#         forgot_states = [state for state in all_states if state not in guessed_states]
#         df = pd.DataFrame(forgot_states)
#         df.to_csv("project 25/India_forgot_state_name.csv", index=False)
#         break