# Build a Calculator

from calculator_module import logo

def additon(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2


operations = {
    "+": additon,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


def calculator():
    """It's a basic calculator\n
    which perform additon, subtraction, multiplication and division."""
    
    print(logo)
    num1 = float(input("What is the first number?\n"))
    
    operation_left = True
    while operation_left:
        result = None
        for symbol in operations:
            print(symbol, end="  ")
            
        operation_symbol = input(f"Choose your operation from the options\n")
        num2 = float(input("What is the second number?\n"))
        calculation_function = operations[operation_symbol]
        
        if calculation_function == division:
            if num2 == 0:
                print("ZeroDivisionError")
                operation_left = False
            else:
                result = calculation_function(num1, num2)
                print(f"{num1} {operation_symbol} {num2} = {result}")
        else:
            result = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")


        user_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, for exit type 'stop'\n").lower()
        if user_input == "y":
            num1 = result
        elif user_input == "n":
            calculator()
        elif user_input == "stop":
            operation_left = False




calculator()






