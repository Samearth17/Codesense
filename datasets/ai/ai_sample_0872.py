class TicTacToe(object):
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.x_player = 1
        self.o_player = -1
        self.empty = 0

    def get_available_moves(self):
        moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == self.empty:
                    moves.append((row, col))
        return moves

    def _evaluate(self):
        winner = self.get_winner()

        if winner == self.x_player:
            return +1
        elif winner == self.o_player:
            return -1
        else:
            return 0

    def get_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2]:
                return self.board[row][0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[1][1]
        else:
            return None

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def minimax(self, depth, player):
        if player == self.x_player:
            best = [-1, -1, -1000]
        else:
            best = [-1, -1, 1000]

        if depth == 0 or self.get_winner() != None:
            score = self._evaluate()
            return [-1, -1, score]

        for move in self.get_available_moves():
            row = move[0]
            col = move[1]

            self.make_move(row, col, player)
            score = self.minimax(depth - 1, -player)
            self.make_move(row, col, self.empty)

            score[0] = row
            score[1] = col

            if player == self.x_player:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score

        return best