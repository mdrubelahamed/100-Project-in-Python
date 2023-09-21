#love calculator
first_name = input("What is your name? ").lower()
second_name = input("What is your patner's name? ").lower()

both_name = first_name + second_name
count_true = 0
count_love = 0

t = both_name.count("t")
r = both_name.count("r")
u = both_name.count("u")
e = both_name.count("e")

l = both_name.count("l")
o = both_name.count("o")
v = both_name.count("v")
e = both_name.count("e")

count_true = t + r + u + e
count_love = l + o + v + e

#or
# love_as_str = str(count_true) + str(count_love)
# love_as_int = int(str(count_true) + str(count_love))

love_as_int = int(str(count_true) + str(count_love))

if love_as_int<10 or love_as_int>90:
    print(f"Your love chance is {love_as_int}%,you go together like coke and mentos")
elif 40<= love_as_int <=50:
    print(f"Your love chance is {love_as_int}%, you are alright together.")
else:
    print(f"Your love chance is {love_as_int}")

