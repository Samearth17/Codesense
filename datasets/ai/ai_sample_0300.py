import random
import os

# define the characters
villain = { "name": "Evil Wizard", "hp": 100 }
hero = { "name": "Hero", "hp": 100 }

def fight_evil_wizard():
    print("You attack the Evil Wizard!")
    # randomly choose to either hit or miss the target
    is_hit = random.choice([True, False])
    if is_hit:
        print("You hit the Evil Wizard!")
        villain["hp"] -= 10
    else:
        print("You missed!")
    # print out the hp of each character 
    print("Your HP: {}".format(hero["hp"]))
    print("Evil Wizard HP: {}".format(villain["hp"]))

def manage_hp(target, value):
    target["hp"] += value
    print("Your HP: {}".format(hero["hp"]))
    print("Evil Wizard HP: {}".format(villain["hp"]))

while True:
    os.system("cls")  # clear the terminal output
    # check if either character is alive
    if hero["hp"] <= 0:
        print("You have been defeated!")
        break
    if villain["hp"] <= 0:
        print("You have slain the Evil Wizard!")
        # you won!
        break

    # show the user the options
    print("What would you like to do?")
    print("1. Fight Evil Wizard")
    print("2. Heal (HP +10)")
    print("3. Run away")
    user_input = int(input(">> "))

    if user_input == 1:
        fight_evil_wizard()
    elif user_input == 2:
        manage_hp(hero, 10)
    elif user_input == 3:
        print("You run away from the Evil Wizard!")
        break
    else:
        print("Invalid input!")