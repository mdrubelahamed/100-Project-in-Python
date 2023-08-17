# Welcome to the Number Guessing Game!
# I've picked a number between 1 and 100.
# Guess the number: 50
# Too low! Guess higher.

# Guess the number: 75
# Too high! Guess lower.

# Guess the number: 60
# Congratulations! You guessed the number 60.
import random
computer_choice = random.randint(1,20)
print("Welcome to the Number Guessing Game!")
print("I've picked a number between 1 and 20.")

user_choice = None
guess_count = 0
out_of_guesses = False
guess_limit = int(input("guess limit "))
while user_choice != computer_choice and not (out_of_guesses) :
    if guess_count < guess_limit :
        user_choice = int(input("Guess the number: "))
        if user_choice > computer_choice:
            print("Too High! guess lower")
        elif user_choice < computer_choice:
            print("Too low! guess higher")
        guess_count += 1

    else:
        out_of_guesses = True


if out_of_guesses == False:
    print("you win")
else : 
    print("you lose")