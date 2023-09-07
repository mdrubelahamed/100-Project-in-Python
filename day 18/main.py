import colorgram
import random
import turtle
from turtle import *

# rgb_color_list = []
# colors = colorgram.extract('day 18/hust.jpg',2**32)


# for color in colors:
#     # RGB = color.rgb
    
#     R = color.rgb.r
#     G = color.rgb.g
#     B = color.rgb.b

#     rgb_set = (R, G, B)
#     rgb_color_list.append(rgb_set)

# print(rgb_color_list)


## Draw a 10 by 10 image using CIRCLE
# color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205), (104, 129, 152), (67, 64, 59), (112, 135, 140), (175, 196, 206)]


# tim = Turtle()
# tim.speed(50)
# turtle.colormode(255)



# x = -200
# y = -250
# for i in range(1, 101):
#     tim.penup()
#     tim.setposition(x,y)
#     random_color = random.choice(color_list)
#     tim.pendown()
#     tim.pencolor(random_color)
#     tim.fillcolor(random_color)
#     tim.begin_fill()
#     tim.circle(8)
#     tim.end_fill()
    
#     if i in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
#         x = -200
#         y += 50
#     else :
#         x += 50


## Draw a 10 by 10 image using DOT
color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205), (104, 129, 152), (67, 64, 59), (112, 135, 140), (175, 196, 206)]


tim = Turtle()
tim.speed(100)
turtle.colormode(255)

x = -200
y = -250
for i in range(1, 101):
    tim.hideturtle()
    
    random_color = random.choice(color_list)
    tim.penup()
    tim.setposition(x,y)
    tim.pendown()
    tim.dot(20,random_color)

    if i in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
        x = -200
        y += 50
    else :
        x += 50















screen = Screen()
screen.exitonclick()