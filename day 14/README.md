```
# HIGHER OR LOWER

# import random module of randint()
import random
from day14module import data

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {account}"

def compare(guess,a_followers,b_followers):
    if choice == "a":
        if random1_followers > random2_followers:
            random1 = random1
            return score + 1
        return "wrongchoice"
    else:
        if random2_followers > random1_followers:
            random1 = random2
            return score + 1
        return "wrongchoice"



# def random1_data():
#     print(random1)
#     random1_name = random1["name"]
#     random1_followers = random1["follower_count"]
#     random1_description = random1["description"]
#     random1_country = random1["country"]
#     pr1 = f"{random1_name}, a {random1_description}, from {random1_country}"
#     return random1_followers


# def random2_data():
#     global random2
#     random2 = data[randint(0, data_position)]
#     print(random2)
#     random2_name = random2["name"]
#     random2_followers = random2["follower_count"]
#     random2_description = random2["description"]
#     random2_country = random2["country"]
#     pr2 = f"{random2_name}, a {random2_description}, from {random2_country}"
#     return random2_followers


# def compare(choice, score):
#     random1_followers = random1_data()
#     random2_followers = random2_data()
#     if choice == "a":
#         if random1_followers > random2_followers:
#             random1 = random1
#             return score + 1
#         return "wrongchoice"
#     else:
#         if random2_followers > random1_followers:
#             random1 = random2
#             return score + 1
#         return "wrongchoice"


# def game():
#     score = 0
#     choice = None
#     random1 = data[randint(0, data_position)]
#     random2 = data[randint(0, data_position)]
#     while choice != "wrongchoice":
#         random1_data()
#         print("\n")
#         random2_data()
#         print("\n")
#         choice = input("Who has more followers? TYPE 'A' or 'B'").lower()
#         x = compare(choice, score)
#         print("----------------")
#         if x != "wrongchoice":
#             print(f"Your current score is {x}")
#         else:
#             return


# game()

```







```


def get_random_account():
    return random.choice(data)


def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

```