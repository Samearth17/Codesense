import random

options = ['Rock', 'Paper', 'Scissor']

while True:
    # Player 1 turn
    print('What would you like to choose?\n Rock, Paper, or Scissor?')
    p1_choice = input()

    # Player 2 turn
    p2_choice = random.choice(options)

    # Game rules
    if p1_choice == p2_choice:
        print('Its a tie!')
    elif (p1_choice == 'Rock' and p2_choice == 'Paper') or (p1_choice == 'Paper' and p2_choice == 'Scissor') or (p1_choice == 'Scissor' and p2_choice == 'Rock'):
        print('Player 2 wins')
    else:
        print('Player 1 wins')
        
    quit_game = input('Would you like to play again?(yes/no)\n')
    if quit_game.lower() == 'no':
        break