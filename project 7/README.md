# DAY 7
##  HANGMAN PROJECT

I meesed up here I must GO through the hangman project more carefully ??


```
from module import word_list,stages,logo
import random,os

random_word = random.choice(word_list)
word_len = len(random_word)
print(f"Psswt random word {random_word}")

underscore_list = []

for _ in range(word_len):
    underscore_list += "_"


end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess the letter: ").lower()
    os.system("cls")

    if guess in underscore_list:
        print(f"{lives} lifes left")
        print(f"you guessed it already {guess}")

    for i in range(word_len):
        letter = random_word[i]
        if letter == guess:
            underscore_list[i] = letter
    
    if guess not in random_word:
        lives -= 1
        print("You guessed wrong you lose a life")
        print(f"{lives} lives left")

    if lives <= 0:
        print("You lose")
        print(f"Correct word {random_word}")
        end_of_game = True

    print(' '.join(underscore_list))

    if "_" not in underscore_list:
        print("you won")
        end_of_game = True
    
    print(stages[lives])
```