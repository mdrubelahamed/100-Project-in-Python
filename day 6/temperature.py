# Temperature convertion ---
print("Temperature convert menu:")
print("1.Celcius to Farenheit \n2.Farenheit to Celcius")

convert = 1

while convert != 0:
    choice = int(input("Which way you want to choice (1/2) or 0 for quit\n"))
    if choice == 0:
        print("Goodbye!")
        convert = choice     
    elif choice == 1:
        celcius = float(input("Enter the temperature in celcius: "))
        farenheit = round((celcius * 9 / 5) + 32,2)
        print(f"{celcius}°C is {farenheit}°F")
        convert = choice
    elif choice == 2:
        farenheit = float(input("Enter the temperature in farenheit: "))
        celcius = round((farenheit - 32) * 5 / 9,2)
        print(f"{farenheit}°F is {celcius}°C")
        convert = choice
    else:
        print("Please choose between 0,1 and 2 ")
