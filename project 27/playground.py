
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


# def explore_arguments(a, b, *args, c=10, **kwargs):
#     result = a + b + c
#     for arg in args:
#         result += arg
#     for key, value in kwargs.items():
#         result += value
#     return result


# # Example usage:
# output = explore_arguments(2, 3, 4, 5, 6, c=15, x=8, y=12)

# a=2, b=3, c=15, args = (4,5,6), kw = {x:8, y:12}
  

# Now, some questions for you:
# 1. What are the values of 'a', 'b', 'args', 'c', and 'kwargs' in the function call?
# 2. What is the final output of the function for the given example usage?
# 3. How does the order of arguments affect the function's behavior?
# 4. Try calling the function with different combinations of values. What happens?
# 5. How would you modify the function to make 'c' a required argument?

# Take your time to analyze the code and answer these questions. Let me know if you have any doubts!


# ------------------------- WIDGET EXAMPLES ------------------------- #
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=550, height=550)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=20)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=20)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

# ---------------------- CELCIUS TO FARENHEIT ------------------------- # 
# celsius to fareherit 
# (C + 9/5) + 32 = F 
# °C 

# from tkinter import *

# def c_to_f():
#     celsius = float(celecius_input.get())
#     farenheit = ((celsius * 9/5) + 32)
#     farenheit_result.config(text=f"{farenheit}")

# FONT = ("Arial", 20, "normal")
    
# window = Tk()
# window.minsize(width=400, height=400)
# window.config(padx=20, pady=20)
# window.title("celsius to Farenheit Converter")

# celecius_input = Entry(width=10)
# celecius_input.focus()
# celecius_input.grid(column=1, row=1)

# c_label = Label(text="°C", font=FONT)
# c_label.config(padx=5, pady=5)
# c_label.grid(column=2, row=1)

# equal_button = Button(text="=", font=FONT, command=c_to_f)
# equal_button.config(padx=30, pady=20)
# equal_button.grid(column=3, row=1)

# farenheit_result = Label(text="32", font=FONT)
# farenheit_result.config(padx=5, pady=5)
# farenheit_result.grid(column=4, row=1)

# f_label = Label(text="°F", font=FONT)
# f_label.grid(column=5, row=1)

# window.mainloop()