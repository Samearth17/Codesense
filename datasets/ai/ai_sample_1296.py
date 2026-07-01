import random

# Function to print the tic tac toe board
def print_board(board):
 for i in range(3):
 for j in range(3):
 print(board[i][j], end=" ")
 print()
 print()

# Function to generate a random tic tac toe board
def generate_board():
 board = [[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

 for i in range(3):
 for j in range(3):
 board[i][j] = random.choice(["X", "O"]) 
 
 print_board(board)

generate_board()