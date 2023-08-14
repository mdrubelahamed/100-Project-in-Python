# rollercoaster ride multiple f
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120 :
    print("You can ride the roller coaster!")
    age = int(input("what is your age? "))
    if age < 12:
        print("Your Ticket Price is $5")
    elif age <= 18:
        print("Your Ticket Price is $7")
    else:
        print("Your Ticket Price is $12")
else:
    print("Sorry, you have to grow taller before you can ride.")