x = "Fizz"
y = "Buzz"

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0 :
        print(f"{x}{y}")
    elif number % 3 == 0:
        print(f"{x}")
    elif number % 5 == 0:
        print(f"{y}")
    else :
        print(number)