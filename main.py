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


def check_resources(choice, menu, c_resources, money):
    water, milk, coffee = c_resources["water"], c_resources["milk"], c_resources["coffee"]

    if choice in menu:
        drink = menu[choice]
        drink_ingredients = drink["ingredients"]
        cost = drink["cost"]

        if choice in ["latte", "cappuccino"]:
            if water >= drink_ingredients.get("water", 0) and milk >= drink_ingredients.get("milk", 0) and coffee >= drink_ingredients.get("coffee", 0):
                water -= drink_ingredients.get("water", 0)
                milk -= drink_ingredients.get("milk", 0)
                coffee -= drink_ingredients.get("coffee", 0)
                money += cost
            else:
                return water, milk, coffee, money, False
        elif choice == "espresso":
            if water >= drink_ingredients.get("water",0) and coffee >= drink_ingredients.get("coffee", 0):
                water -= drink_ingredients.get("water", 0)
                coffee -= drink_ingredients.get("coffee", 0)
                money += cost
            else:
                return water, milk, coffee, money, False

    return water, milk, coffee, money, True


def process_coins(quarters, dimes, nickels, pennies):
    q = quarters * 0.25
    d = dimes * 0.10
    n = nickels * 0.05
    p = pennies * 0.01
    return q + d + n + p


def coffee_machine():
    money = 0
    is_done = False
    while not is_done:
        coffee_choice = input("Choose Espresso, Latte, or Cappuccino ").lower()
        report = (check_resources(coffee_choice, MENU, resources, money))
        resources["water"], resources["milk"], resources["coffee"], money, enough_resources = report

        if coffee_choice in MENU:
            drink = MENU[coffee_choice]
            cost = drink["cost"]

            if enough_resources:
                if coffee_choice != 'report' or coffee_choice != 'off':
                    print(f"This {coffee_choice} costs ${cost}. Please insert coins: ")
                    q = float(input("How many quarters? "))
                    d = float(input("How many dimes? "))
                    n = float(input("How many nickels? "))
                    p = float(input("How many pennies? "))
                    total = process_coins(q, d, n, p)
                    refund = "%.2f" % (total - cost)
                    change = f"Your change is ${refund}"

                    if total == cost:
                        print(change)
                    elif total > cost:
                        print(change)
                    elif total < cost:
                        print("Sorry, that's not enough money. Money refunded.")
                        continue
                    print(f"Here is your {coffee_choice}. Enjoy!")
            else:
                print(f"Sorry, not enough ingredients for {coffee_choice}")

        if coffee_choice == "report":
            print(f"Water: {report[0]}ml\nMilk: {report[1]}ml\nCoffee: {report[2]}g\nMoney: ${report[3]}")

        if coffee_choice == 'off':
            is_done = True


coffee_machine()