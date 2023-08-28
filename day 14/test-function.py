# Define a function called greet that takes a name as an argument and returns a greeting message like "Hello, [name]!"
# def greet(name):
#     return f"Hello {name}"

# name = input("what is your name? ")
# print(greet(name))

#################################################
# Write a function named square that takes a number as input and returns the square of that number
# def square(number):
#     return number*number

# number = int(input("which number's square do you want?"))
# print(square(number))


#################################################
# # Create a function called is_even that takes an integer as an argument and returns True if the number is even, otherwise False
# def is_even(integer):
#     if integer % 2 == 0:
#         return True
#     else:
#         return False
# integer = int(input("which number do you want to check? is even or not?"))
# print(is_even(integer))


#################################################
# Define a function calculate_total that takes the quantities and prices of items as separate lists and returns the total cost.

# def calculate_total(price,quantities):
#     total_cost = 0
#     for price,quantity in zip(price,quantities):
#         total_cost += price * quantity
#     return total_cost

# price = [10,15,10]
# quantities = [2, 3,10]

# print(calculate_total(price,quantities))


#################################################
# def calculate_total(prices,quantities):
#     total_cost = 0
#     for i in range(len(prices)):
#         total_cost += prices[i] * quantities[i]
#     return total_cost

# quantities = [2,4,5]

# prices = [2.5, 3.0, 1.25]
# print(calculate_total(prices,quantities))


# TAKING INPUT FROM USER
#################################################
# def calculate_total(prices, quantities):
#     return prices * quantities


# item_left = True
# total_cost = 0
# while item_left:
#     price_input = int(input("Enter prices of items "))
#     quantity_input = int(input("Enter quantities of items "))

#     cost = calculate_total(quantity_input, price_input)
#     total_cost += cost
#     print(f"The total cost is: ${total_cost:.2f}")

#     asking = input("is item left type 'y' or 'n' ").lower()
#     if asking == "y":
#         pass
#     else:
#         print(f"The total cost is: ${total_cost:.2f}")
#         item_left = False


#################################################
# Write a function find_average that calculates the average of a list of numbers. Use this function to find the average of two lists of numbers.
# def find_average(n_list):
#     total_value = 0
#     for item in n_list:
#         total_value += item
#     avarage = total_value / len(n_list)
#     return avarage

# a_list = [10, 15, 20, 25, 30]
# b_list = [5, 10, 15, 20, 25]

# print(f"{find_average(a_list)}")
# print(f"{find_average(b_list)}")


#################################################
# Create a function divide_and_remainder that takes two numbers as input and returns both the result of division and the remainder.
# def divide_and_remainder(num1,num2):
#     """takes two number from user and return division and remainder result"""
#     return num1 / num2, num1 % num2

# num1 = int(input("what is the first number?"))
# num2 = int(input("what is the second number?"))

# division_result, remainder_result = divide_and_remainder(num1, num2) #tuple unpacking

# print(f"division result {division_result}")
# print(f"remainder result {remainder_result}")

#################################################
# Write a function analyze_text that takes a sentence as input and returns the number of vowels, consonants, and spaces in the sentence
# from functionModule import vowels,consonants
# def analyze_text(plain_text):
#     """takes plain take and anlayze vowel,consonant,spaces"""
#     vowel = 0
#     consonant = 0
#     space = 0
#     for char in plain_text:
#         if char in vowels:
#             vowel += 1
#         elif char in consonants:
#             consonant += 1
#         elif char == ' ':
#             space += 1
#     return vowel,consonant,space

# plain_text = input("What text do you want to analyze?").lower()
# vowels_count,consonants_count,spaces_count = analyze_text(plain_text)

# print(f"Vowels in your text {vowels_count} ")
# print(f"Consonants in your text {consonants_count} ")
# print(f"Spaces in your text {spaces_count} ")


#################################################
# Implement a recursive function factorial that calculates the factorial of a given positive integer.
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# num = 5
# value = factorial(num)
# print(f"final value {value}")


#################################################
# Fibonacci Sequence
# Create a recursive function to generate the nth term of the Fibonacci sequence, where each term is the sum of the two preceding terms.
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# n = 5

# print(fibonacci(n))


#################################################
# Write a recursive function power(base, exponent) that calculates the value of base raised to the power of exponent.
# def power(base,exponent):
#     if exponent == 1:
#         return base
#     else:
#         return base * power(base,exponent-1)

# base = 2
# exponent = 9

# print(power(base,exponent))

# Implement a recursive function sum_of_digits(n) that calculates the sum of the digits of a given positive integer n.
# def sum_of_digits(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_of_digits(n-1)
# n = 10
# print(sum_of_digits(n))

# Create a recursive function is_palindrome(s) that checks whether a given string s is a palindrome (reads the same forwards and backwards)
# def palindrome(string):
#     if len(string) < 1:
#         return True
#     if string[0] == string[-1] :
#         return palindrome(string[1:-1])
#     else:
#         return False
# string = "@abba@"

# print(palindrome(string))

# 0000
# def apply_function(square,numbers):
#     modified_list = [] 
#     for num in numbers:
#         modified_list.append(square(num))
#     return modified_list
            
# def square(x):
#     return x ** 2
# numbers = [1, 2, 3, 4, 5]

# print(apply_function(square,numbers))

