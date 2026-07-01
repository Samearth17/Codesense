import random
import numpy as np

BOARD_SIZE = 3
PLAYER = 1  # player is X
AI = 2  # AI is O

def create_board():
  board = np.zeros((BOARD_SIZE, BOARD_SIZE)) # board is 3x3 array of 0's
  return board

def valid_space(board, position):
  if position[0] < 0 or position[0] >= BOARD_SIZE:
    return False
  elif position[1] < 0 or position[1] >= BOARD_SIZE:
    return False
  elif board[position[0], position[1]] != 0:
    return False
  else:
    return True

def make_move(board, pos, symbol):
  board[pos[0], pos[1]] = symbol

def ai_move(board, symbol):
  pos = random.choice(list(zip(*np.where(board == 0)))) # pick random empty space
  make_move(board, pos, symbol)

def player_move(board, symbol):
  pos = input('Enter your move (row column): ').split()
  pos = [int(i) for i in pos]
  if not valid_space(board, pos):
    print('Invalid move!')
    return False
  else:
    make_move(board, pos, symbol)
    return True


def main():
  board = create_board()
  winner = 0
  turn = PLAYER
  complete = False

  while not complete and not winner:
    if turn == PLAYER:
      player_move(board, PLAYER)
      turn = AI
    else:
      ai_move(board, AI)
      turn = PLAYER
    winner = check_winner(board)
    complete = check_complete(board)
    print_board(board)

  if winner == PLAYER:
    print('Player wins')
  elif winner == AI:
    print('AI wins')
  else:
    print('Draw')

def check_complete(board):
  if 0 in board:
    return False
  else:
    return True

def check_winner(board):
  for i in range(BOARD_SIZE):
    if np.all(board[i] == PLAYER):
      return PLAYER
    elif np.all(board[i] == AI):
      return AI

  for j in range(BOARD_SIZE):
    if np.all(board[:,j] == PLAYER):
      return PLAYER
    elif np.all(board[:,j] == AI):
      return AI

  diag1 = np.diag(board)
  diag2 = np.diag(np.fliplr(board))
  if np.all(diag1 == PLAYER):
    return PLAYER
  elif np.all(diag1 == AI):
    return AI
  elif np.all(diag2 == PLAYER):
    return PLAYER
  elif np.all(diag2 == AI):
    return AI

  else:
    return 0

def print_board(board):
  for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
      if board[i,j] == PLAYER:
        print('X ', end="")
      elif board[i,j] == AI:
        print('O ', end="")
      else:
        print('  ', end="")
    print()

if __name__ == "__main__":
  main()