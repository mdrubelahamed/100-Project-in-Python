# with open("project 24/weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("project 24/weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # for row in data:
#     #     print(row)

#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))        
#     print(temperatures)



import pandas

data = pandas.read_csv("project 24/weather_data.csv")
print(type(data))