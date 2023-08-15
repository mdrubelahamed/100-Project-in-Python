# fruits = ["Aplle", "Mango", "Lemon"]
# for fruit in fruits:
#     print(fruit)

# # adding all numbers from 1 to 100
# sum = 0
# for number in range(1,101):
#     sum += number
# print(f"Summation of 1 to 100 is {sum}")


# adding all even numbers between 1 to 100
sum = 0
for number in range(1,101):
    if number % 2 == 0:
        sum += number
print(f"Summation of 1 to 100 even number is {sum}")

# # or
# for number in range(2,101,2):
#     sum += number
# print(sum)