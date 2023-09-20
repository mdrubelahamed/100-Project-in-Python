- Create a screen
- Give screen the listing power through we control the snake
- Use sleep method, so the snake update after a time of delay
- create the snake and move
- create food
- detect collisioin with screen
- detect collision with tail
- Increase score and extend the snake 

---
**Note 1--** I create a `difficulty.py` file which is unused, but you can use it by some modification,
File work: it's change the game sleep time system, so basically before opening the game, it will ask you which level do you want to play the game, by you choice the game start slow, medium, hard

**Note 2--** day21 folder is not present because day21 work is in the day20 folder

---

- Concept of Inheritence which we are using to create our classes
```
# Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exahle.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doint it underwater")

    def swim(self):
        print("moving in water")

rui = Fish()

rui.swim()
rui.breathe()
print(rui.num_eyes)
```



- Concept of slicing which we are using to detect the collision between snake.head and the other parts of the body
```
piano_keys = ["a", "b", "c", "d", "e", "f", "g"] 
print(piano_keys[2:5])       # Output: ['c', 'd', 'e']
```

```
...
complete code before tail
....

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()
```
