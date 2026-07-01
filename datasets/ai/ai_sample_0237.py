class Game:
    def __init__(self):
        self.board = [["-", "-", "-"], 
                      ["-", "-", "-"], 
                      ["-", "-", "-"]]
        self.current_player = "X"

    def display_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ")
            print()

    def move(self, current_player, row, col):
        if self.board[row][col] == "-": 
            self.board[row][col] = current_player
        else:
            print("invalid move, row and col has already been taken")

    def check_winner(self):
        winner = None
        for row in self.board:
            if row[0] == row[1] == row[2]:
                winner = row[0]
                break
        for col in range(len(self.board[0])):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                winner = self.board[0][col]
                break
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            winner = self.board[0][2]

        if winner == None:
            return False
        else:
            return winner