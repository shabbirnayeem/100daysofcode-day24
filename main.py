MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


# TODO 3: report, when the user type in report it should print out current resources and how money was made
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${money_earned}")


# TODO 4: Check resource sufficient
# When the user chooses a drink, the program should check if there are enough resources to make that drink.


def check_resource(drink_choice):
    water = MENU[drink_choice]['ingredients']['water']
    coffee = MENU[drink_choice]['ingredients']['coffee']
    milk = MENU[drink_choice]['ingredients']['milk']
    if resources['water'] < water:
        print("Sorry there is not enough water.")
        return False
    elif resources['coffee'] < coffee:
        print("Sorry there is not enough coffee.")
        return False
    elif resources['milk'] < coffee:
        print("Sorry there is not enough milk.")
        return False
    else:
        resources['water'] -= water
        resources['coffee'] -= coffee
        resources['milk'] -= milk
        return True

# TODO 5: Process coins
# If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# prompt the user to enter quarters, dimes, nickles, pennies
# Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


def calculate():
    amount_quarters = int(input("how many quarters? "))
    amount_dimes = int(input("how many dimes? "))
    amount_nickles = int(input("how many nickles? "))
    amount_pennies = int(input("how many pennies? "))
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    total = quarters * amount_quarters + dimes * amount_dimes + nickles * amount_nickles + pennies * amount_pennies
    return total


# print(calculate())

# TODO 6: Check transaction successful. check if the user entered enough money to buy coffee
# if the user entered less then price print"Sorry that's not enough money. Money refunded."
# if user entered enough money the cost should be added to the report Money:
# if the user entered too many coins, the machine should offer change
# “Here is $2.45 dollars in change.”
# drink_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()

# print(money_earned)
# print(MENU[drink_choice]['cost']


# TODO 7: Make coffee. if the transaction if successful and enough resources to make the drink
#  the ingredients to make the coffee should be deducted from the resources
# Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.

off = False
money_earned = 0
while not off:
    # TODO 1:  Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    drink_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()

    if drink_choice == 'report':
        report()
    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
    elif drink_choice == 'off':
        off = True
    else:
        is_enough = check_resource(drink_choice)

        if is_enough:
            # Helpful to print out the price of the coffee when the user makes his/her selection
            print(f"That will be ${MENU[drink_choice]['cost']}")
            user_money = calculate()

            if MENU[drink_choice]['cost'] > user_money:
                print("Sorry that's not enough money. Money refunded.")
            elif MENU[drink_choice]['cost'] == user_money:
                money_earned += user_money
                print(f"Here is your {drink_choice} ☕️. Enjoy!")
            elif MENU[drink_choice]['cost'] < user_money:
                change = user_money - MENU[drink_choice]['cost']
                price = user_money - change
                money_earned += price
                print(f"Here is ${change} in change.")
                print(f"Here is your {drink_choice} ☕️. Enjoy!")