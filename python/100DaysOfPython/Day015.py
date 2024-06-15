# Day 15
# Coffee Machine

coffee: dict = {"espresso": {"price": 1.5, "water": 50, "coffee": 18},
                "latte": {"price": 2.5, "water": 200, "coffee": 24, "milk": 150},
                "cappucino": {"price": 3, "water": 250, "coffee": 24, "milk": 100}
                }
machine: dict = {"water": 300, "milk": 200, "coffee": 100, "payments": 0}
coins: dict = {"penny": 1, "nickel": 5, "dime": 10, "quarter": 25}
exit_machine: bool = False


def print_report(_machine: dict):
    print(f'Water: {_machine["water"]}ml.')
    print(f'Milk: {_machine["milk"]}ml.')
    print(f'Coffee: {_machine["coffee"]}g.')
    print(f'Money: €{round(_machine["payments"],2)}')
    return ""


def process_payments(_receive_coins: int, _user_choice: str, _coffee: dict):
    return _receive_coins - _coffee[_user_choice]["price"]


def receive_coins(_coins: dict):
    quarters = int(input("How many quarters? ")) * _coins["quarter"]
    dimes = int(input("How many dimes? ")) * _coins["dime"]
    nickels = int(input("How many nickels? ")) * _coins["nickel"]
    pennies = int(input("How many pennies? ")) * _coins["penny"]
    return (quarters + dimes + nickels + pennies) / 100


def is_machine_available(_user_choice, _coffee, _machine):
    if _machine["water"] - _coffee[_user_choice]["water"] < 0 or _machine["coffee"] - _coffee[_user_choice]["coffee"] < 0:
        if (_user_choice == "latte" or _user_choice == "cappucino") and _machine["milk"] - _coffee[_user_choice]["milk"]:
            return False
    _machine["water"] -= _coffee[_user_choice]["water"]
    _machine["coffee"] -= _coffee[_user_choice]["coffee"]
    if _user_choice == "latte" or _user_choice == "cappucino":
        _machine["milk"] -= _coffee[_user_choice]["milk"]
    return _machine


while not exit_machine:
    user_choice: str = ""
    while user_choice not in ["espresso", "latte", "cappucino", "report"]:
        user_choice = input("\n\nWhat would you like? (espresso/latte/cappucino): ")

    if user_choice == "report":
        print_report(machine)
        exit_machine = True
        break

    is_available = is_machine_available(user_choice, coffee, machine)
    if not is_available:
        print("\nLow on resources. Not possible at the moment. Sorry!")
        print_report(machine)
        exit_machine = True
        break

    print("Please insert coins: ")
    user_change = process_payments(receive_coins(coins), user_choice, coffee)
    if user_change >= 0:
        machine["payments"] += coffee[user_choice]["price"]
        print(f"\nHere's your change, €{round(abs(user_change),2)}")
        print(f"Here's your {user_choice}. Enjoy!!!")
    else:
        print(f"\nNot enough money. Missing €{round(abs(user_change),2)}. Sorry!")
        exit_machine = True
