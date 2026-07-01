def tic_tac_toe_heuristic(board):    
    # check winning condition
    win_conditions = ((0,1,2), (3,4,5), (6,7,8),
                      (0,3,6), (1,4,7), (2,5,8), 
                      (0,4,8), (2,4,6))

    winner = 0
    for each in win_conditions:
      if board[each[0]] == board[each[1]] == board[each[2]] == 1:
        winner = 1
      elif board[each[0]] == board[each[1]] == board[each[2]] == 2:
        winner = 2

    # when the game is over
    if winner != 0:
      return winner

    # evaluate each position
    max_eval = -2
    best_move = None
    for move in board:
      if move == 0:
        board[move] = 1
        eval = minimax(board, 0, False)
        board[move] = 0
        if eval > max_eval:
          max_eval = eval
          best_move = move

    return best_move

def minimax(board, depth, isMaximizing):
    # check winning condition
    win_conditions = ((0,1,2), (3,4,5), (6,7,8),
                      (0,3,6), (1,4,7), (2,5,8), 
                      (0,4,8), (2,4,6))

    winner = 0
    for each in win_conditions:
      if board[each[0]] == board[each[1]] == board[each[2]] == 1:
        winner = 1
      elif board[each[0]] == board[each[1]] == board[each[2]] == 2:       
        winner = 2

    # when the game is over
    if winner != 0:
        return (-1)**(winner == 2)*10/depth

    # when there is no valid move
    if sum((x != 0) for x in board) == 9:
        return 0

    if isMaximizing:
        best_eval = -10
        for move in board:
            if move == 0:
                board[move] = 1
                eval = minimax(board, depth + 1, False)
                board[move] = 0
                best_eval = max(best_eval, eval)
        
        return best_eval
    else:    
        best_eval = 10
        for move in board:
            if move == 0:
                board[move] = 2
                eval = minimax(board, depth + 1, True)
                board[move] = 0
                best_eval = min(best_eval, eval)
        
        return best_eval

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

best_move = tic_tac_toe_heuristic(board)
print(best_move)