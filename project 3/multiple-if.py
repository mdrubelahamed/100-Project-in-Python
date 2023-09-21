# rollercoaster ride
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120 :
    print("You can ride the roller coaster!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}")
    # elif age>=45 and age<=55: #logical operator
    #     print("Have a free ride on us $0")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}")

    photo = input("do you want a photo ticket? 'Y or N' --")
    if photo.lower() == 'y':
        bill = bill + 3
        print(f"your ticket price are ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")