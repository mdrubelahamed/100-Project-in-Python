#Order size
print("Welcome to Python size Shop!")

size = input("What size size do you want 'S,M,L' : ")
add_pepperoni = input("Do you want to add Pepperoni 'Y or N'?")
extra_cheese = input("Do you want extra cheese in your size 'Y or N'?")

bill = 0
if size == 'S':
    bill += 15
    print(f"Small size Price are {bill}")
elif size == 'M':
    bill += 20
    print(f"Medium size Price are {bill}")
elif size == 'L':
    bill += 25
    print(f"Large size Price are {bill}")
else:
    print("Invalid Input")


if add_pepperoni == 'Y':
    if size == 'S':
        bill +=2
    else:
        bill += 3


if extra_cheese == 'Y':
    bill += 1
 
print(f"Your final bill is ${bill}")
