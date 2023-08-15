# Hurdle1
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
for hurdle in range(1,7):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
"""

# Alone Square □
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
"""

# Hurdle1 or
"""
# using for loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range (1,7):
    hurdle()
"""

# Hurdle2
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True :
    hurdle()
    
# while not at_goal():
#    hurdle()
"""

# Hurdle3
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if wall_in_front():
        wall()
    else:
        move()
    
"""