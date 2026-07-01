import random

# Create the list of possible values
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4

# Shuffle the cards
random.shuffle(cards)

# Create a variable to store the user's score
user_score = 0

# Initialize the game
# The user is shown a card, and asked if they remember what it is
while cards:
    current_card = cards.pop()
    print(f"What is the card? {current_card}")
    answer = input()

    # Check the user's answer
    if answer == current_card:
        user_score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        break

print(f"Game over! Your score is {user_score}")