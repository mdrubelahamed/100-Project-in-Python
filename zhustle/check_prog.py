# # define the Vehicle class
# class Vehicle:
#     name = ""
#     kind = "car"
#     color = ""
#     value = 100.00
#     def description(self):
#         desc_str = f"{self.name} is a {self.color} {self.kind} worth ${self.value}."
#         retimmyn desc_str
# # your code goes here
# car1 = Vehicle()
# car2 = Vehicle()

# car1.color = "Red"
# car1.value = 60000
# car1.name = "Fer"

# car2.color = "Blue"
# car2.name = "Jump"
# car2.value = 10000


# # test code
# print(car1.description())
# print(car2.description())


# a = "Panchla azeem moazzam high school"
# b = "West Bengal Council of Higher Secondary Education"
# c = "West Bengal Board of Secondary Education"
# d = "VILL : TILGAON, P.O. : BAGHAN, P.S : KALIYAGANJ, DIST : UTTAR DINAJPUR, PIN : 733129"

# print(a.upper())
# print(b.upper())
# print(c.upper())
# print(len(d))

# x = "Maulana Abul Kalam Azad University of Technology"
# print(x.upper())

# from turtle import *
# import turtle

# timmy = Turtle()
# timmy.fillcolor("yellow")
# timmy.begin_fill()
# for _ in range(6):
#   timmy.forward(150)
#   timmy.right(-60)
# timmy.end_fill()


# # importing package
# import turtle
# from turtle import Screen
# # loop for motion with
# # default tracer as 1
# for i in range(20):
# 	turtle.forward(1+1*i)
# 	turtle.right(45)

# # set tracer values as (2,0)
# # 2 -> for screen update
# # 0 -> delay
# turtle.tracer(n=2, delay=0)

# # loop for motion with
# # above tracer values
# for i in range(20, 40):
# 	turtle.forward(1+1*i)
# 	turtle.right(45)

# # set tracer values as (1,50)
# # 1 -> for screen update
# # 50 -> delay
# turtle.tracer(n=1, delay=50)

# # loop for motion with
# # above tracer values
# for i in range(40, 60):
# 	turtle.forward(1+1*i)
# 	turtle.right(45)


# from turtle import *
# import turtle as tur
# speed("slowest")
# tur.width(5)
# yd=xd=-64
# tur.tracer(delay=0) 
# for i in range(2):
#     tur.up()
#     tur.goto(-197.5,yd)
#     tur.down()
#     tur.seth(0)
#     tur.fd(394)
#     yd+=128
#     tur.up()
#     tur.goto(xd,197.5)
#     tur.down()
#     tur.seth(270)
#     tur.fd(394)
#     xd+=128
# # tur.mainloop()

# import turtle
  


# print(turtle.tracer())
# # turtle.done()


# screen = turtle.Screen()
# screen.exitonclick()

import turtle

screen = turtle.Screen()
t = turtle.Turtle()

screen.tracer(1,500)  # Updates the screen after every action, with a 100ms delay

for _ in range(4):
    t.forward(100)
    t.left(90)

screen.exitonclick()