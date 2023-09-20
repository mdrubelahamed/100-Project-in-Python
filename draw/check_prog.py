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



  


# print(turtle.tracer())
# # turtle.done()


# screen = turtle.Screen()
# screen.exitonclick()

# import turtle

# screen = turtle.Screen()
# t = turtle.Turtle()

# screen.tracer(1,500)  # Updates the screen after every action, with a 100ms delay

# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# screen.exitonclick()



# #####################################
# # Inheritance
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
    
#     def breathe(self):
#         print("Inhale, Exahle.")


# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

#     def breathe(self):
#         super().breathe()
#         print("doint it underwater")

#     def swim(self):
#         print("moving in water")

# rui = Fish()

# rui.swim()
# rui.breathe()
# print(rui.num_eyes)


# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# print(piano_keys[2:5])



slow = "Then I added a logic where if the ball hits the paddle's the ball change his direction in the opposite where i change x-axis direction, so the ball move to the opposite direction"

print(slow.title())