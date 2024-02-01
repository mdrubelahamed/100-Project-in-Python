num1=float(input("enter first number: "))
operator=input("enter operator: ")
num2=float(input("enter second number:"))

if operator == "+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)
elif operator =="/":
    print(num1/num2)
elif operator =="//":
    print(num1//num2)
elif operator =="%":
    print(num1%num2)
else: print("Invalid operator!")

# def add(num1,num2):
#     return num1+num2
# def sub(num1,num2):
#     return num1-num2
# def multi(num1,num2):
#     return num1*num2
# def div(num1,num2):
#     return num1/num2
# def quo(num1,num2):
#     return num1//num2
# def mod(num1,num2):
#     return num1%num2

# num1=float(input("enter first number: "))
# num2=float(input("enter second number: "))
# op = input("enter operator: ")

# if op == '1':
#     print("{}".format(add(num1,num2)))