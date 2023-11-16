
## how to provide default values and optional paramerter 
# def add(a=1, b=2, c=3):
#     print(a+b+c)
# add(b=6)


# ## how to take unlimited arguments //args 

# def add(*args):
#     """ *args is give the option of unlimited arguments, \n'args' is a variable which you can change but the '*' is compulsory"""
#     for n in args:
#         print(n)

# add(5,6,7)

###############
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(1,2,3,4,5,6,7,8,9,10))


## Define a function with default values for some of its arguments. Call the function with both the default values and new values to observe the behavior

# def show_value(a=1, b=2, c=3, d=4):
#     print(a,b,c,d)

# show_value(d=6)


## Write a function that accepts a variable number of arguments and returns a list containing only the even numbers.

# def even_num(*args):
#     even_list = []
#     for n in args:
#         if n%2 == 0:
#             even_list.append(n)
#     return even_list

# print(even_num(1,2,3,4,5,6,7,8,9,10))


## Create a function that uses keyword arguments. Call the function with different combinations of values to see how the order of keyword arguments can affect the result

# def func(arg1, arg2=2):
#     return arg1, arg2

# print(func(arg1=5))


## ** / kwargs

# def calculate(n, **kwargs):
#     print(kwargs)
#     # print(kwargs["add"])
#     # print(kwargs["multiply"])

#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     # n += kwargs["add"]
#     # print(n)
#     # n*= kwargs["multiply"]
#     # print(n)


# calculate(5, add=2, multiply=3)




# # create a class with kwars from scratch

# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.speed = kw.get("speed")
    
# my_car = Car(make="Tata", model="Nano", color="Red", speed=255)
# print(my_car.color)


# def all_aboard(a, *args,**kw):
#     print(a, args, kw)

# all_aboard(4, 7, 3, 0, x=10, y=64)


def explore_arguments(a, b, *args, c=10, **kwargs):
    result = a + b + c
    for arg in args:
        result += arg
    for key, value in kwargs.items():
        result += value
    return result


# Example usage:
output = explore_arguments(2, 3, 4, 5, 6, c=15, x=8, y=12)

# a=2, b=3, c=15, args = (4,5,6), kw = {x:8, y:12}
  

# Now, some questions for you:
# 1. What are the values of 'a', 'b', 'args', 'c', and 'kwargs' in the function call?
# 2. What is the final output of the function for the given example usage?
# 3. How does the order of arguments affect the function's behavior?
# 4. Try calling the function with different combinations of values. What happens?
# 5. How would you modify the function to make 'c' a required argument?

# Take your time to analyze the code and answer these questions. Let me know if you have any doubts!

