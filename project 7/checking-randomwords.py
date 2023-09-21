import random

word_list = ["ardvark", "baboon", "camel"]
choose_word = random.choice(word_list)
print(f"{choose_word}")
guess = ""

underscore_list = []
for underscore in choose_word:   # for underscore in len(choosen_word)
    underscore_list += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess the letter: ").lower()
    # i = 0 
    # for letter in choose_word:
    #     if letter == guess:
    #         underscore_list[i] = letter
    #     i += 1

    for i in range(len(choose_word)):
        letter = choose_word[i]
        if letter == guess:
            underscore_list[i] = letter
    print(underscore_list)
    
    if "_" not in underscore_list :
        end_of_game = True
        print("you win")