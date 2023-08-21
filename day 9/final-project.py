import os
from day9module import logo
print(logo)
dict1 = {}

# define function which check the highest bidder and what is the bid amount
def bid():
    highest_bid = 0
    highest_bidder = ""
    for bidder,bid_amount in dict1.items(): 
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    print(f"The bid goes to {highest_bidder} with a bid of ${highest_bid}")

# while loop continue until there is no bidder
bidder_left = True
while bidder_left:
    print("Welcome to the secret auction Stage.")
    name = input("What is your name? ")
    bid_amount = int(input("What's your bid $"))
    dict1[name] = bid_amount
    # ask is there any bidder left or not
    quit = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    # because of the we want to clear the screen so no one can see others bid amount
    os.system('cls')
    if quit.lower() == "no":
        bidder_left = False

# calling the function
bid()
