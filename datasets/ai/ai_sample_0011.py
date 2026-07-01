class TicTacToe:

def __init__(self):
    self.board = [['_' for _ in range(3)] 
                   for _ in range(3)]
    self.turn = 'x'
    
def display(self):
    for row in self.board:
        print(' '.join(row))

def check_win(self):
    board = self.board

    # check if the player with the current turn has a row of three
    for row in self.board:
        if row.count(self.turn) == 3:
            return True
        
    # check if the player with the current turn has a column of three
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] == self.turn:
            return True
        
    # check for the two diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == self.turn:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == self.turn:
        return True
    return False