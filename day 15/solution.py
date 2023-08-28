from coffeeModule import MENU,resources

def is_resources_sufficient(order_ingredients):
    """Returns true if enough resources or return false"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def process_coin():
    """Return the total amount from inserted coins"""
    print("Please insert coins.")
    total = int(input("how many peenis?")) * 1
    total += int(input("how many nickles?")) * 5
    total += int(input("how many dime?")) * 10
    total += int(input("how many quarter?")) * 25
    return total


def is_trasaction_successful(money_recieved,drink_cost,choice):
    """Retrun true if payment accepted, or false if money is in sufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Here is your change ₹{change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"You don't have enough money to buy a ☕ {choice}, Money Refunded.")
        return False


def make_coffee(drink_name,order_ingredients):
    """Deduct ingredient from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your ☕ {drink_name}")


profit = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ₹{profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_trasaction_successful(payment,drink["cost"],choice):
                make_coffee(choice,drink["ingredients"])
