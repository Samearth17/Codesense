import random

moves = ["Rock", "Paper", "Scissors"]

player_move = input("Please enter your move: Rock, Paper, Scissors \n")

computer_random = random.randint(0,2)
computer_move = moves[computer_random]

print("Computer plays:" + computer_move)

if player_move == "Rock" and computer_move == "Scissors" or player_move == "Paper" and computer_move == "Rock" or player_move == "Scissors" and computer_move == "Paper":
 print("You Win!")
elif player_move == computer_move:
 print("It's a tie!")
else:
 print("You Lose!")