import numpy as np

board = np.array([[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]])

def is_valid(x, y):
 return 0 <= x < 3 and 0 <= y < 3

def make_move(player, x, y):
 if is_valid(x, y):
 board[x, y] = player
 else:
 raise ValueError("Invalid move")

def check_victory():
 xs, ys = np.where(board == 0)
 # Check vertically
 vertical = board == board.T
 # Check diagonally
 diagonal = np.diag(board).all() or np.diag(np.flipud(board)).all()
 
 if any(vertical) or diagonal:
 return True
 
 return False

def ai_make_move(player):
 xs, ys = np.where(board == 0)
 for x, y in zip(xs, ys):
 board[x, y] = player
 if check_victory():
 return
 board[x, y] = 0 # Reset

if __name__ == "__main__":
 # Set the board state
 board = np.array([[1, 0, -1],
 [-1, 1, 0],
 [0, 0, 1]])

 # AI player
 ai_make_move(-1)
 print(board)