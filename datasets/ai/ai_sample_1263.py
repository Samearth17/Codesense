import random

def rock_paper_scissors():
  
    choices = ['rock', 'paper', 'scissors']
    while True:
        player_choice = input("Choose rock, paper, or scissors: ")
        if player_choice not in choices:
            print("Invalid choice! Please choose again.")
            continue

        computer_choice = random.choice(choices)
        print("The computer chose", computer_choice)

        if player_choice == computer_choice:
            print("It's a draw!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")
        break