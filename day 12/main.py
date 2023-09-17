# GUESS NUMBER GAME WITH EASY AND HARD LEVEL
from random import randint
from day12module import logo
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def check_number(guess,computer_choice,attempts):
    """check guessing number is correct or not. Return how many attempt left for guessing the correct answer"""
    if guess > computer_choice:
        print("Too high")
        return attempts - 1
    elif guess < computer_choice:
        print("Too low")
        return attempts - 1
    else:
        print(f"you guessed {computer_choice} correct. you win")


def choose_difficulty():
    """Easy or Hard level choosing"""
    level = input("Choose your playing level? 'easy' or 'hard'- ")
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def play_game():
    """User will guess until he either guess the correct answer or he is out of guesses"""
    # print(logo)
    print("welcome to number guessing game.")
    print("I am thinking a number between 1 to 100. can you guees the number? ")
    computer_choice = randint(1,100)
    # print(f"Pssst computer guess: {computer_choice}")

    attempts = choose_difficulty()

    guess = 0
    while guess != computer_choice:
        print(f"you have {attempts} attempt to guess the correct number.")
        guess = int(input("Make a guess: "))
    
        attempts = check_number(guess,computer_choice,attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            print(f"Guessing number is {computer_choice}")
            return guess == computer_choice
        elif guess != computer_choice:
            print("Guess again.")
play_game()
