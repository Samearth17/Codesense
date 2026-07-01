"""
Write a Python program to create a Tic Tac Toe game
"""

# global variables 
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"] 
game_is_still_going = True 
  
# who is the winner 
winner = None
  
 # whose turn is it 
current_player = "X"


# display board
def display_board(): 
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print(board[6] + " | " + board[7] + " | " + board[8])
  
  
# play a game of tic tac toe 
def play_game(): 
    
    # display initial board 
    display_board() 
  
    # while game is still going 
    while game_is_still_going: 
  
        # assign handle turn to a variable 
        handle_turn(current_player) 
  
        # check if game is finished 
        check_if_game_over()
  
        # flip to another player 
        flip_player() 
          
    # check if winner  
    if winner == "X" or winner == "O": 
        print("Winner is: " + winner) 
    elif winner == None: 
        print("Tie.") 

# handle a single turn of a player 
def handle_turn(player): 
  
    position = input("Choose a position from 1-9: ") 
    position = int(position) - 1
  
    board[position] = player 
  
    display_board() 
  
  
# check win
def check_if_game_over(): 
    check_if_win() 
    check_if_tie() 
  
# check rows, columns and diagonals for a win 
def check_if_win(): 
    # set global variables 
    global winner 
    # check rows 
    row_winner = check_rows() 
    # check columns 
    column_winner = check_columns() 
    # check diagonals 
    diagonal_winner = check_diagonals() 
    if row_winner: 
        # there is a win 
        winner = row_winner 
    elif column_winner: 
        # there is a win 
        winner = column_winner 
    elif diagonal_winner: 
        # there is a win 
        winner = diagonal_winner 
    else: 
        # there is no win 
        winner = None
    return 
  
# check rows for a win 
def check_rows(): 
    # set global varibales 
    global game_is_still_going 
    # check if any of the rows have all the same values (and is not empty) 
    row_1 = board[0] == board[1] == board[2] != "-" 
    row_2 = board[3] == board[4] == board[5] != "-" 
    row_3 = board[6] == board[7] == board[8] != "-" 
    # if any row does have a match, flag that there is a win 
    if row_1 or row_2 or row_3: 
        game_is_still_going = False 
    # return the winner (X or O) 
    if row_1: 
        return board[0] 
    elif row_2: 
        return board[3] 
    elif row_3: 
        return board[6] 
    # or return None if there was no win 
    else: 
        return None
  
# check columns for a win 
def check_columns(): 
    # set global variables 
    global game_is_still_going 
    # check if any of the columns have all the same values (and is not empty) 
    column_1 = board[0] == board[3] == board[6] != "-" 
    column_2 = board[1] == board[4] == board[7] != "-" 
    column_3 = board[2] == board[5] == board[8] != "-" 
    # if any column does have a match, flag that there is a win 
    if column_1 or column_2 or column_3: 
        game_is_still_going = False 
    # return the winner (X or O) 
    if column_1: 
        return board[0] 
    elif column_2: 
        return board[1] 
    elif column_3: 
        return board[2] 
    # or return None if there was no win 
    else: 
        return None
  
# check diagonals for a win 
def check_diagonals(): 
    # set global variables 
    global game_is_still_going 
    # check if any of the diagonals have all the same values (and is not empty) 
    diagonal_1 = board[0] == board[4] == board[8] != "-" 
    diagonal_2 = board[2] == board[4] == board[6] != "-" 
    # if any diagonal does have a match, flag that there is a win 
    if diagonal_1 or diagonal_2: 
        game_is_still_going = False 
    # return the winner (X or O) 
    if diagonal_1: 
        return board[0] 
    elif diagonal_2: 
        return board[2] 
    # or return None if there was no win 
    else: 
        return None
  
# check if there is a tie 
def check_if_tie(): 
    # set global variables 
    global game_is_still_going 
    # if board is full 
    if "-" not in board: 
        game_is_still_going = False 
    # return true if there is a tie, false if not 
    return

# flip to another player
def flip_player(): 
    # global variables we need 
    global current_player 
    # if current player was x, make it o 
    if current_player == "X": 
        current_player = "O"
    # if current player was o, make it x 
    elif current_player == "O": 
        current_player = "X"

if __name__ == '__main__':
    play_game()