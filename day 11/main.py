# A SIMPLIER VERSION OF BLACKJACK GAME 
import random
import os
from day11module import logo
def get_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculate the final value of cards"""
    if sum(cards) == 21 and len(cards) == 2 :
        return 21
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(user_score,computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 21:
        return "you lose, opponent has blackjack"
    elif user_score == 21:
        return "you win, you got a blackjack"
    elif user_score > 21:
        return "you lose, you bust"
    elif computer_score > 21:
        return "you win, opponent bust"
    elif user_score > computer_score:
        return "you win,you score more"
    elif computer_score > user_score:
        return "you lose, opponent has more score"

def blackjack():
    user_cards = []
    computer_cards = []
    is_game_over = False
    # get two cards for user and computer
    for _ in range(2):
        user_cards.append(get_card())
        computer_cards.append(get_card())

    # until the game ends
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User cards {user_cards}, score {user_score}")
        print(f"computer first cards {computer_cards[0]}")

        if user_score == 21 or computer_score == 21 or user_score > 21:
            is_game_over = True
        else:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass ")
            if get_another_card == 'y':
                user_cards.append(get_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score <17:
        computer_cards.append(get_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nuser final hand {user_cards}, score {user_score}")
    print(f"computer final hand {computer_cards},  score {computer_score}")
    print(compare_score(user_score,computer_score))


while input("do you want to play blackjack, type 'y' or 'n': ") == 'y':
    os.system('cls')
    print(logo)
    blackjack()
    