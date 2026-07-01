import random

# Game Options
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
game_options = [ROCK, PAPER, SCISSORS]

# Game logic which determines the winner
def find_winner(player_option, computer_option):
if player_option == computer_option:
 return 'draw'

if player_option == ROCK:
 if computer_option == PAPER:
  return 'computer'
 else:
  return 'player'

if player_option == PAPER:
 if computer_option == SCISSORS:
  return 'computer'
 else:
  return 'player'

if player_option == SCISSORS:
 if computer_option == ROCK:
  return 'computer'
 else:
  return 'player'

# Main game loop
while True:
# Get user input
player_option = input('Enter Rock, Paper, or Scissors: ').lower()

# Check to make sure input is valid
if player_option in game_options:

# Get computer's option
computer_option = random.choice(game_options)

# Print out computer's option
print(f'Computer chose {computer_option}')

# Determine the winner
winner = find_winner(player_option, computer_option)

# Print out the winner
if winner == 'computer':
 print('Computer won!')
elif winner == 'player':
 print('Congratulations, you won!')
else:
 print('It was a draw!')

# Check if player wants to play another game
play_again = input('Do you want to play again? [y/n] ')
if play_again == 'n':
 break

else:
 print('Please enter a valid option.')