class Board:
    def __init__(self, rows, columns):
        """ Constructor to initilize the board"""

        # Grid of the board
        self.grid = []

        # Initialize the grid
        for row in range(rows):
            self.grid.append([])
            for col in range(columns):
                self.grid[row].append("")

class Player:
    def __init__(self, name):
        """ Constructor to initilize the player """

        self.name = name
        self.score = 0
        self.moves = 0

class GameEngine:
    def __init__(self, board, player1, player2):
        """ Constructor to initilize the game engine """

        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.winning_player = None