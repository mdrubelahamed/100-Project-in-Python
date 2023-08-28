from coffeeModule import MENU,resources

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True
    

def process_coin():
    penny_count = int(input("enter penny: ")) * 1
    nickel_count = int(input("enter nickel: ")) * 5
    dime_count = int(input("enter dime: ")) * 10
    quarter_count = int(input("enter quarter: ")) * 25
    total_amt = penny_count + nickel_count + dime_count + quarter_count
    return total_amt


def is_transaction_successful(money_recieved,drink_cost):
    if money_recieved >= drink_cost:
        change_amt = money_recieved - drink_cost
        print(f"Here is your change ₹{change_amt}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"You don't have enough money, Money Refunded.")
        return False
    

def make_coffee(drink_name,order_ingredients):
    """Deduct ingredient from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your ☕ {drink_name}")
    

profit = 0
make_more_coffee = True
while make_more_coffee:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        make_more_coffee = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ₹{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            paymet = process_coin()
            if is_transaction_successful(paymet,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
