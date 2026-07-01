"""
Create a game of Rock, Paper, Scissors
"""
import random

def game(): 
    choices = ["Rock", "Paper", "Scissors"] 
    # randomly select a choice  
    user = random.choice(choices)  
    # randomly select a choice 
    computer = random.choice(choices) 
    print("User chooses: ", user) 
    print("Computer chooses: ", computer) 
    if user == computer:
        print("It is a tie") 
    if user == "Rock": 
        if computer == "Paper": 
            print("Computer wins!", computer, "covers", user)
        else: 
            print("User wins!", user, "smashes", computer)
    elif user == "Paper": 
        if computer == "Scissors": 
            print("Computer wins!", computer, "cut", user)
        else: 
            print("User wins!", user, "covers", computer)

if __name__ == '__main__': 
    game()