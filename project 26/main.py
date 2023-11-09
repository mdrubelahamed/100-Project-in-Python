# # List Comprehension 

# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# # print(new_list)

# # new_list = [new_item for item in list]

# new_list = [n+1 for n in numbers]
# print(new_list)

# Given a range, create a new list that contains the squares of each integer
# square_list = [n*n for n in range(1,10)]
# print(square_list)


# # Given a list of strings, create a new list that contains the lengths of each string.
# words = ["apple", "banana", "cherry", "date"]

# length_of_word = [len(word) for word in words]
# print(length_of_word)


# # Given a list of words, create a new list that contains only the words with more than five characters
# words = ["apple", "banana", "cherry", "date"]

# more_than_5_char = [word for word in words if len(word) > 5]
# print(more_than_5_char)


# # Given a list of numbers, create a new list that contains only the even numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

# even_numbers = [number for number in numbers if number%2 == 0]
# print(even_numbers)


# # list comprehesion perform in string
# name = "Rubel"
# new_list = [letter for letter in name]
# print(new_list)

# # list comprehesion perform in range
# num_list = [number*2 for number in range(1,5)]
# print(num_list)



# # # # list comprehesion perform in conditional item
# names = ['Alex', 'Beth', 'Cacoline', 'Dave', 'Eleanor', 'Freddie']

# # # 4 or less letter name in  o/p 
# # short_name = [name for name in names if len(name) <= 4]
# # print(short_name)

# # # 5 or more letter name in o/p  and it must be in uppercase
# # long_name = [name.upper() for name in names if len(name) >= 5]
# # print(long_name)


# PrACTice More

# # print out Squared Numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num*num for num in numbers]
# print(squared_numbers)

# # Filter out even Numbers
# string_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']

# int_list = [int(num) for num in string_list]
# # print(int_list)

# even_num = [num for num in int_list if num%2 == 0]
# print(even_num)



######################### DICTIONARY COMPREHENSION ########################################################
# new_dict = {new_key:new_value for item in list}

# # Create a dictionary where the keys are numbers from 1 to 5, and the values are the squares of those numbers 
# new_dict = {n: n*n for n in range(1,6)}
# print(new_dict)

# # Given a list of fruits, create a dictionary where the fruit names are the keys, and the values are the lengths of the fruit names.
# fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
# fruits_lenght_dict = {fruit:len(fruit) for fruit in fruits}
# print(fruits_lenght_dict)

# create a dictionary that counts the frequency of each letter in a given string as keys and uses the letter count as values
# name = "Md Rubel Ahamed"
# frequency_count = {char: name.count(char) for char in name}
# print(frequency_count)

# nested dictionay - dictionary comprehension
# human_names = ["JohnSmith", "MaryJohnson", "DavidBrown", "JenniferLee", "RobertDavis", "LindaWilson", "WilliamJones", "PatriciaTaylor", "MichaelMiller", "ElizabethWhite", "JamesHarris", "SusanAnderson", "JosephMartin", "KarenMoore", "CharlesJackson", "NancyDavis", "ThomasClark", "BettyTaylor", "DanielHall", "SarahThompson"]
# frequency_count_for_list = {name: {char: name.count(char) for char in name} for name in human_names}
# print(frequency_count_for_list)


# # Generate random score for each student
# from random import randint
# names = ['Alex', 'Beth', 'Cacoline', 'Dave', 'Eleanor', 'Freddie']
# student_score = {name: randint(1,100) for name in names}
# # print(student_score)

# # create a passed score dict

# passed_student = {name: score for name,score in student_score.items() if score >=50} # you can also do (name, score)
# print(passed_student)


# ## TEST - from a variable sentece find out each has how much letter
# text = "The quick brown fox jumps over the lazy dog"
# # words = text.split(" ") ## I jump the line in the result dict to make the code more shorter
# result = {word: len(word) for word in text.split(" ")}
# print(result)

# # from Celcius to Farenheit - Dictionary Comprehension
# temperature_data = {"Monday": 25, "Tuesday": 23, "Wednesday": 27, "Thursday": 22, "Friday": 24, "Saturday": 28, "Sunday": 26 }
# weather_F = {day: ((temp* 9/5) +32) for day,temp in temperature_data.items()}
# print(weather_F)

# student_data = {
#     "student": ["Alice", "Bob", "Charlie"],
#     "score": [90, 85, 92]
# }
# for key,value in student_data.items():
#     print(key)
#     print(value)

# import pandas
# student_data_frame = pandas.DataFrame(student_data)
# # print(student_data_frame)

# # # loop through a dataframe
# # for key,value in student_data_frame.items():
# #     print(value)

# # pandas method iterrows()

# for (index, row) in student_data_frame.iterrows():
#     if row.score >= 90:
#         print(row.student)
    

# import pandas as pd

# data = {
#     "student": ["Alice", "Bob", "Charlie", "David"],
#     "score": [75, 58, 90, 90]
# }

# df = pd.DataFrame(data)

# # print the names of students who scored below 60
# for index,row in df.iterrows():
#     if row.score < 60:
#         print(row.student)

# # **Find the student with the highest score in a DataFrame of student scores**
# max_score = -1
# hig_score_std = []
# for index,row in df.iterrows():
#     if row.score > max_score:
#         max_score = row.score
#         hig_score_std = [row.student]
#     elif row.score == max_score:
#         hig_score_std.append(row.student)
# print(hig_score_std)

############################################################################# do no know #####################

import pandas as pd
data = pd.read_csv("project 26/nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

phonetic_dict = {row.letter: row.code for index,row in data.iterrows()}
# print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in user_word]
print(output_list)

# output_list = []
# for letter in user_word:
#     output_list.append(phonetic_dict[letter])
# print(output_list)
