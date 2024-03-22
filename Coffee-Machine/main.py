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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_ingredients(ingredients_of_coffee):
    """Check's ingredients are enough or not and return's true or false"""
    for item in ingredients_of_coffee:
        if ingredients_of_coffee[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns totals calculated from coins"""
    print("please insert cions.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimmes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

should_continue = True
while should_continue:

    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == "off":
        should_continue = False
    elif user_input == "report":
        print(f"Milk: {resources['milk']}ml")
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if check_ingredients(drink["ingredients"]):
            payment = process_coins()
            

print("☕")
