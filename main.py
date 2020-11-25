menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def money_calculator(quarter_input, dimes_input, nickel_input, pennies_input):
    return quarter_input*0.25 + dimes_input*0.1 + nickel_input*0.05 + pennies_input*0.01


machine_on = True

original_water = resources["water"]
original_milk = resources["milk"]
original_coffee = resources["coffee"]

remaining_water = original_water
remaining_milk = original_milk
remaining_coffee = original_coffee

water_consumed = []
milk_consumed = []
coffee_consumed = []
total_money = []
cash = 0

while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()

    if order == "off":
        machine_on = False
        print("Machine is turning off")
    elif order == "report":
        print(f"Water: {remaining_water}ml\nMilk: {remaining_milk}ml\nCoffee: {remaining_coffee}g\nMoney: ${cash}")
    else:
        print("Please insert coins")

        quarter = int(input("how many quarters?"))
        dimes = int(input("how many dimes?"))
        nickel = int(input("how many nickel?"))
        pennies = int(input("how many pennies?"))

        required_water = (menu[order]["ingredients"]["water"])
        required_milk = (menu[order]["ingredients"]["milk"])
        required_coffee = (menu[order]["ingredients"]["coffee"])

        if required_water > remaining_water or required_milk > remaining_milk or required_coffee > remaining_coffee:
            print("Sorry there is not enough ingredients")
        else:
            water_consumed.append(menu[order]["ingredients"]["water"])
            milk_consumed.append(menu[order]["ingredients"]["milk"])
            coffee_consumed.append(menu[order]["ingredients"]["coffee"])

            remaining_water = original_water - sum(water_consumed)
            remaining_milk = original_milk - sum(milk_consumed)
            remaining_coffee = original_coffee - sum(coffee_consumed)

            total_paid = money_calculator(quarter, dimes, nickel, pennies)
            charge = menu[order]["cost"]
            change = round((total_paid - charge), 3)

            total_money.append(menu[order]["cost"])
            cash = sum(total_money)

            if total_paid < charge:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${change} change")
                print(f"Here is your {order} enjoy!")
