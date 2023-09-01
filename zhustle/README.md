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