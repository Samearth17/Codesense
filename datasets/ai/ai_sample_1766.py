ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
 board = [[0 for i in range(COLUMN_COUNT)] for j in range(ROW_COUNT)]
 return board
   
def drop_piece(board, row, col, piece):
 board[row][col] = piece

def is_valid_location(board, col):
 return board[ROW_COUNT - 1][col] == 0

## Check for a win
def check_win(board):
 # Check all horizontal locations for win
 for c in range(COLUMN_COUNT-3):
  for r in range(ROW_COUNT):
   if board[r][c] == board[r][c + 1] == board[r][c + 2] == board[r][c + 3] != 0:
    return board[r][c]

 # Check all vertical locations
 for c in range(COLUMN_COUNT):
  for r in range(ROW_COUNT-3):
   if board[r][c] == board[r + 1][c] == board[r + 2][c] == board[r + 3][c] != 0:
    return board[r][c]

 # Check both diagonals
 for c in range(COLUMN_COUNT-3):
  for r in range(ROW_COUNT-3):
   if board[r][c] == board[r + 1][c + 1] == board[r + 2][c + 2] == board[r + 3][c + 3] != 0:
    return board[r][c]
   if board[r][c + 3] == board[r + 1][c + 2] == board[r + 2][c + 1] == board[r + 3][c] != 0:
    return board[r][c + 3]

 # No win found
 return 0