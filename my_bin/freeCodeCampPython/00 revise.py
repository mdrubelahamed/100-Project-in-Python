# #01
# print("hi","hello","goodbye",end="@", sep=",")
# print("ending checking")

# #02
# salad = "salad is great food when it's comes to nutrition"
# print(salad.replace("great","healthy"))
# # crosscheck = salad.replace("great","healthy")
# # print(crosscheck)
# print(salad)

# notebook = "notebook is great when it's comes to winning, it's help us to realize our knowledge through practice"

# srk = notebook.replace("winning","writing")
# srk = notebook.replace("realize","analyze")
# print(srk)


# def printPattern():
#     for i in range(n):
#         for j in range (i+1):
#             print("*",end=" ")
#         print()

# n = int(input("enter a range: "))
# printPattern()

#@table

# def multitable():
#     for i in range(1,n+1):
#         print(f"Multiplication table for {i}")
#         for j in range(1,n+1):
#             print(f"{i} * {j} =", (i*j))
#         print()

            
# n = int(input("enter table for : "))
# multitable()

def additon(a,b):
    return a+b

try:
    a = float(input("enter first number(a): "))
    b = float(input("enter first number(b): "))
    
    result = additon(a,b)
    print(f"{a} + {b} = {result}")

except ValueError as err:
    print(err)
