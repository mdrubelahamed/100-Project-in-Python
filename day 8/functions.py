# def greet():
#     print("Hello Sir !!! Welcome to Our Hotel")
#     print("Which room do you want to book?")
#     print("1.Normal 2.Premium 3.VIP")

# greet()

# # write a function which can take input
# def greet_with_name(name):
#     print(f"Hello {name}, welcome to our hotel")
#     print("Which room do you want to book? \n1.Normal 2.Premium 3.VIP")

# greet_with_name("Rubel")

# # function() with more than one input
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is like in {location}")

# # greet_with("Rubel", "Tilgaon")
# greet_with(location="Tilgaon", name="Rubel")

# finding paint_can
import math

def paint_calc(height, width, cover):
    cans = math.ceil((height * width) / cover)
    print(f"you will need {cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)
