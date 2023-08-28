# BUILDING A HAGMAN GAME
import random
import os

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

random_word = random.choice(word_list)
word_length = len(random_word)

end_of_game = False
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo

# Testing code
# print(f'Pssst, the solution is {random_word}.')

# Create blanks
blank_list = []
for _ in range(word_length):
    blank_list += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in blank_list:
        print(f"You have already guessed {guess}")
    # Check guessed letteryou
    for i in range(word_length):
        letter = random_word[i]
        # print(f"Current i: {i}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            blank_list[i] = letter

    # Check if user is wrong.
    if guess not in random_word:
        # TODO-5: - If the letter is not in the random_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"You have {lives} lives remain")
        if lives == 0:
            end_of_game = True
            print(f"Guessing word is {random_word}")
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(blank_list)}")

    # Check if user has got all letters.
    if "_" not in blank_list:
        end_of_game = True
        print("You win.")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages

    print(stages[lives])
