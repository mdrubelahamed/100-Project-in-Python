# Number guessing game
import random
print("Welcome to the Number Guessing Game!")
guess_count = 0
guess_num = None

print("I am thinkin a number between 1 and 10")
random_num = random.randint(1,10)

while guess_num != random_num:
    guess_num = int(input("Can you guess the number? Enter your guess: "))

    if guess_num == random_num :
        guess_count += 1
        print(f"Congratulations! You've guessed the number {guess_num} in {guess_count} attempts.")
    else :
        guess_count += 1
        if guess_num > random_num :
            print("Too High! Try again.")
        else: 
            print("Too low! Try Again")