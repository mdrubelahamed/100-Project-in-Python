import os
from module import logo


data = {}

def bid():
    higest_bid = 0
    highest_bidder = ""

    for bidder,bid_amt in data.items():
        if bid_amt > higest_bid:
            higest_bid = bid_amt
            highest_bidder = bidder
    print(f"Highest bidder is {highest_bidder}, with a bid of ${higest_bid}")


auction_live = True

while auction_live:
    print(logo)
    print("Welcome to the secret bid auction")
    person = input("What is your name? ")
    amt = float(input("What is your bid $"))

    data[person] = amt

    bidder_left = input("Anyone wants to bid type 'y' or type 'n'\n").lower()
    os.system("cls")
    if bidder_left == 'n':
        auction_live = False

bid()


    