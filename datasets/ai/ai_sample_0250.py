# define the game board
board = ["_" for i in range(9)]

# define the player and computer symbols
player = "X"
computer = "O"

def display_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# check for a win
def check_win():
    # check rows
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    # if any row does have a match, flag that there is a win
    if row1 or row2 or row3:
        game_over = True
    # check columns
    col1 = board[0] == board[3] == board[6] != "_"
    col2 = board[1] == board[4] == board[7] != "_"
    col3 = board[2] == board[5] == board[8] != "_"
    # if any column does have a match, flag that there is a win
    if col1 or col2 or col3:
        game_over = True
    # check diagonals
    diag1 = board[0] == board[4] == board[8] != "_"
    diag2 = board[2] == board[4] == board[6] != "_"
    # if any diagonal does have a match, flag that there is a win
    if diag1 or diag2:
        game_over = True
    # if any condition is true, there is a win
    if row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2:
        winner = player
    else:
        game_over = False
    return game_over, winner

# play the game
while True:
    # display the game board
    display_board()
    # get player input
    while True:
        try:
            player_choice = int(input("Pick a number between 1-9: "))
            if player_choice >= 1 and player_choice <= 9:
                if board[player_choice - 1] == "_":
                    board[player_choice - 1] = player
                    break
            else:
                print("Sorry, please try again")
        except:
            print("Sorry, please try again")

    # check for a win
    game_over, winner = check_win()
    if game_over:
        display_board()
        print("Congratulations! You win! ")
        break
    # check for a tie
    if "_" not in board:
        print("It's a tie")
        break