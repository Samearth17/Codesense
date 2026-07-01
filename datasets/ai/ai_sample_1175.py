"""
Design a "rock, paper, scissors" game using Python.
"""

import random

OPTIONS = ["rock", "paper", "scissors"]

def play_game():
    # Player selection
    print("Choose your weapon: rock, paper, or scissors")
    player_choice = input().lower()

    # Computer selection
    computer_choice = random.choice(OPTIONS)
    print(f"Computer chose {computer_choice.title()}")

    # Compare selections
    if player_choice == computer_choice:
        print("It's a tie!")
    else:
        if player_choice == "rock":
            if computer_choice == "paper":
                print("Computer wins!")
            elif computer_choice == "scissors":
                print("Player wins!")
        elif player_choice == "paper":
            if computer_choice == "scissors":
                print("Computer wins!")
            elif computer_choice == "rock":
                print("Player wins!")
        elif player_choice == "scissors":
            if computer_choice == "rock":
                print("Computer wins!")
            elif computer_choice == "paper":
                print("Player wins!")

if __name__ == "__main__":
    play_game()