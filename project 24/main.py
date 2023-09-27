import pandas

data = pandas.read_csv("project 24/weather_data.csv")
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

data_dict = {
    "students": ["John", "Emily", "Michael"],
    "scores": [90, 85, 88]
}

data = pandas.DataFrame(data=data_dict)
print(data)
data.to_csv("project 24/scratch_data.csv")
