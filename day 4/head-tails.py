# Toss Coin which will generate Heads or Tails
import random

# toss = random.randrange(2)  
toss = random.randint(0,1)


if toss == 1:
    print("Heads")
else:
    print("Tails")