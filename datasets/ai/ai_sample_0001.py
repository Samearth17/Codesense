# Rock, paper, scissors game!

def play_game(player1, player2):
    #  Define the winning rules
    rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if player1 == player2:
        return 'It is a draw!'
    elif rules[player1] == player2:
        return 'Player 1 wins!'
    elif rules[player2] == player1:
        return 'Player 2 wins!'

# Get user input
player1 = input('Player 1, make a choice: rock, paper, or scissors? ').lower()
player2 = input('Player 2, make a choice: rock, paper, or scissors? ').lower()

# Start the game and get the result
result = play_game(player1, player2)
print(result)