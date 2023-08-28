my number guessing game
```
import random
def guess_number():
    attempt_left = 5
    user_choice = input("Which way you want to play? 'easy' or 'hard' ")
    if user_choice == 'easy':
        attempt_left = 10
    guess_chance = True
    while guess_chance:
        print(f"you have {attempt_left} attempt to guess the correct number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == computer_guess:
            print(f"you guessed {computer_guess} correct. you win")
            guess_chance = False
        elif user_guess > computer_guess:
            print("Too high")
        elif user_guess < computer_guess:
            print("Too low")
        attempt_left -= 1
        if attempt_left <= 0:
            guess_chance = False
            if user_guess != computer_guess:
                print("you are run out of guesses,you lose")


print("welcome to number guessing game.")
print("I am thinking a number between 1 to 100. can you guees the number? ")
computer_guess = random.randint(1,100)
print(f"pssst computer guess: {computer_guess}")
guess_number()
```