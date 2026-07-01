def tic_tac_toe():
    game_board = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
    player_1 = True
    while not game_over():
        move = get_ai_move()
        if player_1:
            game_board[move[0]][move[1]] = 1
            player_1 = False
        else:
            game_board[move[0]][move[1]] = -1
            player_1 = True

def get_ai_move():
    # Use AI algorithms to find the best move
    best_move = 0
    # Return the best move
    return best_move

def game_over():
    # Game is over if there's a winner or a tie
    return False