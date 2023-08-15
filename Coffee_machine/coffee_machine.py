from menu import MENU
from menu import resources
user_choice = ""
quarters = 0
dimes = 0
nickels = 0
pennies = 0
saved_money = 0
is_on = True

def report():
    print("Water: " + str(resources["water"]) + "ml\nMilk: " + str(resources["milk"]) + "ml\nCoffee: " + str(resources["coffee"]) + "g\nMoney: $" + str(round(resources["money"],2)))

def sufficiency():
    global user_choice
    if resources["water"] < (MENU[user_choice]["ingredients"]["water"]):
        print("Not enough water. Please turn off and refill the coffee machine.")
        return False          
    elif resources["coffee"] < (MENU[user_choice]["ingredients"]["coffee"]):
        print("Not enough coffee. Please turn off and refill the machine.")
        return False
    elif user_choice != "espresso" and resources["milk"] < (MENU[user_choice]["ingredients"]["milk"]):
        print("Not enough milk. Turn off, add some more milk and try it again.") 
        return False
    else:
        return True
    
def selection():
    while True:
        user_choice = input(f"\nHi!\nHere is your coffee machine!\nCredit value: {round(resources['money'],2)}\nWhat would you like? (espresso - ${MENU['espresso']['cost']}/latte - ${MENU['latte']['cost']}/cappuccino - ${MENU['cappuccino']['cost']}): ")
        if user_choice == "espresso":
            return user_choice
        elif user_choice == "latte":
            return user_choice
        elif user_choice == "cappuccino":
            return user_choice
        elif user_choice == "report":
            return user_choice
        elif user_choice == "off":
            return user_choice
        else:
            print("Try it again.")
            continue

def check_saved_coins():
    if saved_money > 0 and saved_money >= (MENU[user_choice]["cost"]):
        return False
    else:
        return True

def insert_money():
    global user_choice
    global total
    print("Please insert coins:")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters*0.25)+(dimes*0.10)+(nickels*0.05)+(pennies*0.01)
    return total

def prepare_drink():
    global total
    global money_back
    global saved_money
    money_back = total-(MENU[user_choice]["cost"])
    if money_back > 0:
        print(f"Here is ${round(money_back,2)} dollars in change.")
        saved_money += money_back
    print(f"Here is your {user_choice}. Enjoy!\n")
    if user_choice != "espresso":
        (resources["coffee"]) -= int(MENU[user_choice]["ingredients"]["coffee"])
        (resources["milk"]) -= int(MENU[user_choice]["ingredients"]["milk"])
        (resources["water"]) -= int(MENU[user_choice]["ingredients"]["water"])
        (resources["money"]) += round(money_back,2)
    else:
        (resources["coffee"]) -= int(MENU[user_choice]["ingredients"]["coffee"])
        (resources["water"]) -= int(MENU[user_choice]["ingredients"]["water"])
        (resources["money"]) += round(money_back,2)
#____________________________________________ 
while is_on == True:
    total = 0
    money_back = 0
    user_choice = selection()
    if user_choice == "off":
        is_on = False
        print(".... coffee machine is going to sleep ......... ")
        continue
    elif user_choice == "report":
        report()
    else:
        if sufficiency() == True:
            if check_saved_coins() == True:
                total = insert_money()
                if total >= (MENU[user_choice]["cost"]):
                    prepare_drink()
                else:
                    print("Sorry that's not enough money. Money refunded.\n")
            else:
                prepare_drink()
        else: 
            is_on = False
            continue
    