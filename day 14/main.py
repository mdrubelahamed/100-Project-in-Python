import random
import os
from day14module import data
from art import vs,logo

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"COMPARE A : {format_data(account_a)}")
    print(vs)
    print(f"COMPARE B : {format_data(account_b)}")

    guess = input("who has more followers 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_followers_count)

    if is_correct:
        score += 1
        os.system('cls')
        print(logo)
        print(f"you're right, current score {score}")
    else :
        game_should_continue = False
        print(f"That's wrong, final score {score}")