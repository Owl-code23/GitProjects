MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO#1: print report
# TODO#2: check resources sufficient?
# TODO#3: process coins
# TODO#4: check transaction successful?
# TODO#5: make coffee

def sufficient_resources():
    """return False if resources are not sufficient and also print the first low resource"""
    for ingredient in MENU[decision]['ingredients']:
        if resources[ingredient] < MENU[decision]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def update_resources(choice):
    """update resources after choosing a coffee"""
    for coffee in MENU[choice]['ingredients']:
        resources[coffee] -= MENU[choice]['ingredients'][coffee]


def process_coins():
    """ask the user for different coins and return the combine value"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies


turn_off = False
money = 0

while not turn_off:
    decision = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if decision == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif decision == 'off':
        turn_off = True
    else:
        if sufficient_resources():
            payment = process_coins()

            # Check transaction
            if payment < MENU[decision]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if payment > MENU[decision]['cost']:
                    change = payment - MENU[decision]['cost']
                    print(f"Here is ${change:.2f} dollars in change")
                money += MENU[decision]['cost']
                update_resources(decision)
                print(f"Here is your {decision}. Enjoy!")