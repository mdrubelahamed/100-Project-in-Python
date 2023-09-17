# GUESS NUMBER GAME WITH EASY AND HARD LEVEL

import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

class NumberChecking:  
    def check_number(self,guess,computer_choice,attempts):
        if guess > computer_choice:
            print("Too high")
            return attempts - 1
        elif guess < computer_choice:
            print("Too low")
            return attempts - 1
        else:
            print(f"you guessed {computer_choice} correct. you win")


class Difficulty(NumberChecking):
    
    def __init__(self):
        super().__init__()

    def choose_difficulty(self):
        level = input("Choose your playing level? 'easy' or 'hard'- ")
        if level == 'easy':
            return EASY_LEVEL_ATTEMPTS
        else:
            return HARD_LEVEL_ATTEMPTS

class StartGame(Difficulty):

    def __init__(self):
        super().__init__()


    def play_game(self):
        print("welcome to number guessing game.")
        print("I am thinking a number between 1 to 100. can you guees the number? ")
        computer_choice = random.randint(1,100)
        # print(f"Pssst computer guess: {computer_choice}")

        attempts = self.choose_difficulty()

        guess = 0
        while guess != computer_choice:
            print(f"you have {attempts} attempt to guess the correct number.")
            guess = int(input("Make a guess: "))
        
            attempts = self.check_number(guess,computer_choice,attempts)
            if attempts == 0:
                print("You've run out of guesses, you lose.")
                print(f"Guessing number is {computer_choice}")
                return
            elif guess != computer_choice:
                print("Guess again.")


# startgame = StartGame()

# startgame.play_game()