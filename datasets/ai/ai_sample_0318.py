# create Tic-tac-toe game
board = [None] * 9

def draw_board(): 
  row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
  row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
  row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
  
  print()
  print(row1)
  print(row2)
  print(row3)
  print()

def get_row_col():
  row = int(input("Enter row: "))
  col = int(input("Enter col: "))
  index = (row * 3) + col
  return index 

def update_board(icon, index): 
  board[index] = icon

def is_victory(icon): 
  # check victory across row
  across1 = (board[0] == icon) and (board[1] == icon) and (board[2] == icon)
  across2 = (board[3] == icon) and (board[4] == icon) and (board[5] == icon)
  across3 = (board[6] == icon) and (board[7] == icon) and (board[8] == icon)

  # check victory across column
  column1 = (board[0] == icon) and (board[3] == icon) and (board[6] == icon)
  column2 = (board[1] == icon) and (board[4] == icon) and (board[7] == icon)
  column3 = (board[2] == icon) and (board[5] == icon) and (board[8] == icon)

  # check victory across diagonal
  diagonal1 = (board[0] == icon) and (board[4] == icon) and (board[8] == icon)
  diagonal2 = (board[2] == icon) and (board[4] == icon) and (board[6] == icon)

  if (across1 or across2 or across3 or column1 or column2 or column3 or diagonal1 or diagonal2):
    return True
  else:
    return False

while True:
  # player 1 
  index = get_row_col()
  update_board("X", index)
  draw_board()

  if(is_victory("X")):
    print("Player 1 wins")
    break

  # player 2
  index = get_row_col()
  update_board("O", index)
  draw_board()

  if(is_victory("O")):
    print("Player 2 wins")
    break