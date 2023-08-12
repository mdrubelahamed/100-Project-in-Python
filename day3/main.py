#conditional Statements, Logical Operators, Code Blocks , Scope and many more
# Treasure Island game


# rollercoaster ride
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120 :
    print("You can ride the roller coaster!")
    age = int(input("what is your age? "))
    if age < 12:
        print("Your Ticket Price is $5")
    elif 12 <= age <= 18:
        print("Your Ticket Price is $7")
    else:
        print("Your Ticket Price is $12")
else:
    print("Sorry, you have to grow taller before you can ride.")



# #checking odd even number
# number = int(input("Which number do you want to check? "))
# if number%2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")
