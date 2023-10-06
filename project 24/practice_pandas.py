# calculator

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2


operations = {
    "+" : addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}


def calculator():
    num1 = float(input("What is first number: "))
    
    operation_left = True
    while operation_left:
        for operator in operations:
            print(f"'{operator}' ", end=" ")
        
        op = input("Choose from this operators\n")
        num2 = float(input("What is second number: "))

        cal_func = operations[op]

        if cal_func == division:
            if num2 == 0:
                print("ZeroDivisionError")
                return
            else:
                result = cal_func(num1, num2)
        else:
            result = cal_func(num1, num2)
        
        print(f"{num1} {op} {num2} = {result}")

        go_on = input("type 'y'  for continue or 'n' for a new calculation, to exit type 'e'\n").lower()
        if go_on == 'y':
            num1 = result
        elif go_on == 'n':
            calculator()
        else:
            operation_left = False
    
        
calculator()