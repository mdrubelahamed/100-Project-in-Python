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
`pip install pandas` - to install pandas library<br>
In previouly I used so many lines to get only the tempDegree but through pandas library I can do this in so much easy way
```
import pandas

temperatures = []
data = pandas.read_csv("project 24/weather_data.csv)

for t in data["temp"]:
    temperatures.append(t)

```






---
---
---
- Querating code
- 1
```
# with open("project 24/weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("project 24/weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    # for row in data:
    #     print(row)

    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))        
    print(temperatures)
```
