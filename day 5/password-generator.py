# #Password Generator Project

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# ## WAY NO.1
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= input("How many letters would you like in your password?\n")
# nr_numbers = input(f"How many numbers would you like?\n")
# nr_symbols = input(f"How many symbols would you like?\n")

# #creat an emplty list
# password_list = []

# # find out the length of the input given by user so we can run for loop 
# nr_letters_len = int(nr_letters)
# nr_symbols_len = int(nr_symbols)
# nr_numbers_len = int(nr_numbers)

# # using for loop to generate letters, numbers, symbols, asmuch user want 
# for i in range(nr_letters_len):
#     x = random.choice(letters)
#     password_list.append(x)

# for i in range(nr_numbers_len):
#     x = random.choice(numbers)
#     password_list.append(x)
    
# for i in range(nr_symbols_len):
#     x = random.choice(symbols)
#     password_list.append(x)

# # create join those value into a single varible using join method 
# easy_password = "".join(password_list)

# # now shuffling the easy_password we generate so we make more randomized, now it doesn't follow the letter,number and symbol rule--
# easy_password_list = list(easy_password)
# random.shuffle(easy_password_list)
# print(easy_password_list)

# # create join those value into a single varible using join method 
# hard_password = "".join(easy_password_list)

# print(f"Here is your easy password {easy_password}")
# print(f"Here is your hard password {hard_password}")


# ---------------------------------------------------------------------------------------------------
## WAY NO.2
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))

# # # easy level
# # password = ""

# # for letter in range(nr_letters):
# #     password += random.choice(letters)
# # for number in range(nr_numbers):
# #     password  += random.choice(numbers)
# # for symbol in range(nr_symbols):
# #     password += random.choice(symbols)
# # print(f"Here is your password: {password}")


# #hard level
# password_list = []
# for letter in range(nr_letters):
#     password_list += random.choice(letters)
# for number in range(nr_numbers):
#     password_list  += random.choice(numbers)
# for symbol in range(nr_symbols):
#     password_list += random.choice(symbols)

# random.shuffle(password_list)

# password = ""
# for char in password_list:
#     password += char

# print(f"Here is your password: {password}")




# ------------------------------------
# --------------------------------------
# totaly random

print("Welcome to the PyPassword Generator!")
# nr_letters = random.randint(1,5)
# nr_numbers = random.randint(1,5)
# nr_symbols = random.randint(1,5)

nr_letters = 4
nr_numbers = 2
nr_symbols = 1



password_list = []
for letter in range(nr_letters):
    password_list += random.choice(letters)
for number in range(nr_numbers):
    password_list  += random.choice(numbers)
for symbol in range(nr_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

# print(f"A complete random password : {password}")


print(f"Your Reset password otp: {password}")