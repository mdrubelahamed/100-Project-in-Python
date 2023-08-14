import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock,paper,scissors]
user_choice = int(input("Choose between rock(0), paper(1), scissors(2)\n"))
if user_choice>2:
    print("Please choose between rock(0), paper(1), scissors(2) ")
else:
    print(game_image[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer Choose:")
    print(game_image[computer_choice])

    if user_choice == computer_choice:
        print("Draw")
    elif user_choice == 0 and computer_choice == 1 :
        print("you lose")
    elif user_choice == 0 and computer_choice == 2 :
        print("you win")
    elif user_choice == 1 and computer_choice == 0 :
        print("you win")
    elif user_choice == 1 and computer_choice == 2 :
        print("you lose")
    elif user_choice == 2 and computer_choice == 0 :
        print("you lose")
    elif user_choice == 2 and computer_choice == 1 :
        print("you win")
