import random

# Define a list of possible moves
moves = ["rock", "paper", "scissors"]

# Define the AI's move
def ai_move():
    ai_choice = random.choice(moves)
    return ai_choice

# Define the function to determine the winner
def play_round(player_move, ai_move):
    if player_move == ai_move:
        result = "tie"
    elif (player_move == "rock" and ai_move == "scissors") or (player_move == "paper" and ai_move == "rock") or (player_move == "scissors" and ai_move == "paper"):
             result = "player"
    else:
        result = "ai"
    return result

# Define a function to check the opponent's last move
def check_opponent_move(opponent_move):
    if opponent_move == "rock":
        ai_choice = "paper"
    elif opponent_move == "paper":
        ai_choice = "scissors"
    elif opponent_move == "scissors":
        ai_choice = "rock"
    return ai_choice

# Play the game
player_move = input("Choose your move: ")
opponent_move = input("What was your opponent's last move? ")

ai_choice = check_opponent_move(opponent_move)
result = play_round(player_move, ai_choice)
 
if result == "player":
    print("You won!")
elif result == "ai":
    print("You lost!")
else:
    print("It's a tie!")