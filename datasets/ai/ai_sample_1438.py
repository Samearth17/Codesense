def solve_sudoku(board):
 size = len(board)
 empty = find_empty_entry(board, size)
 
 if not empty:
  return True
 
 else:
  row, col = empty
 
 for num in range(1, size+1):
  if check_valid_number(board, size, num, (row, col)):
   board[row][col] = num
 
   if solve_sudoku(board):
    return True
 
   board[row][col] = 0
 
 return False
 
 
def find_empty_entry(board, size):
 for row in range(size):
  for col in range(size):
   if board[row][col] == 0:
    return (row, col)
 
 return None
 
 
def check_valid_number(board, size, num, position):
 row, col = position
 
 # If the number is already present in the column or row, then return false
 for gen in range(size):
  if board[row][gen] == num or board[gen][col] == num:
   return False
 
 # Check if the number is present inside the board's 3x3 box
 row_start = (row//3)*3
 col_start = (col//3)*3
 
 for num_row in range(row_start, row_start+3):
  for num_col in range(col_start, col_start+3):
   if board[num_row][num_col] == num:
    return False
 
 return True