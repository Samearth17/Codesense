import random
import time

# Create classes
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.position = [0, 0]

class Enemy:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(50, 100)

# Initialize globals
player = Player(input("What is your name? "))
enemies = []
done = False

# Game loop
while not done:
    print("You are in room ({}, {})".format(player.position[0], 
                                            player.position[1]))
    print("1. Move")
    print("2. Check HP")
    print("3. Exit Game")
    action = int(input("What do you want to do? "))

if action == 1:
    # Movement
    x = int(input("Move how many units on the x-axis? "))
    y = int(input("Move how many units on the y-axis? "))
    player.position[0] += x
    player.position[1] += y

elif action == 2:
    # Check HP
    print("Your HP is {}".format(player.hp))

elif action == 3:
    # Exit Game 
    done = True

# Generate enemies randomly
if random.random() < 0.1:
    enemies.append(Enemy("Rat"))
    print("An enemy appeared!")

# Combat
for enemy in enemies:
    print("A {} approaches!".format(enemy.name))
    print("What do you do? 1. Fight 2. Flee")
    action = int(input(">"))

    if action == 1:
        fight(player, enemy)