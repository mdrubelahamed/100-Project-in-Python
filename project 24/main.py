# with open("project 24/weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open("project 24/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas as pd

data = pd.read_csv("project 24/weather_data.csv")
# print(data)
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
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
# df.to_csv("project 24/student_data_from_scratch.csv")



# ##############################
# # Squirel Count

# import pandas as pd

# data = pd.read_csv("project 24/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
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

# df.to_csv("project 24/squirrel_count.csv")



#####################
