secret_word="rubel"
guess=""
guess_count= 0
guess_limit= 30
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess=input("enter your guess word: ")
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses == True:
    print("You lose!!!")
else: 
    print("You Win!!!")
