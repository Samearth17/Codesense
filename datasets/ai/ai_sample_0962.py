import numpy as np

class Board:
 def __init__(self):
 self.board = np.zeros((6,7), np.int8)
 self.win_state = (
 (0, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6), 
 (7, 8, 9, 10), (8, 9, 10, 11), (9, 10, 11, 12), (10, 11, 12, 13), 
 (14, 15, 16, 17), (15, 16, 17, 18), (16, 17, 18, 19), (17, 18, 19, 20),
 (21, 22, 23, 24), (22, 23, 24, 25), (23, 24, 25, 26), 
 (0, 7, 14, 21), (7, 14, 21, 28), (14, 21, 28, 35), 
 (1, 8, 15, 22), (8, 15, 22, 29), (15, 22, 29, 36),
 (2, 9, 16, 23), (9, 16, 23, 30), (16, 23, 30, 37), 
 (3, 10, 17, 24), (10, 17, 24, 31), (17, 24, 31, 38), 
 (4, 11, 18, 25), (11, 18, 25, 32), (18, 25, 32, 39),
 (5, 12, 19, 26), (12, 19, 26, 33), (19, 26, 33, 40), 
 (6, 13, 20, 27), (13, 20, 27, 34), (20, 27, 34, 41), 
 (3, 9, 15, 21), (4, 10, 16, 22), (10, 16, 22, 28), (11, 17, 23, 29),
 (17, 23, 29, 35), (12, 18, 24, 30), (18, 24, 30, 36), (13, 19, 25, 31), 
 (19, 25, 31, 37), (5, 11, 17, 23), (6, 12, 18, 24), (12, 18, 24, 30),
 (13, 19, 25, 31), (19, 25, 31, 37), (20, 26, 32, 38), (26, 32, 38, 44),
 (27, 33, 39, 45), (33, 39, 45, 51), (34, 40, 46, 52)
 ) 
 self.winner = 0

def move(self, player, column):
 row = board[:,column].argmax()
 if board[row][column] == 0:
 board[row][column] = player
 for row in self.win_state:
 if check_state(row) == player:
 self.winner = player
 return True
 return False

def check_state(self, row):
 board_slice = self.board[row]
 if (board_slice == player).all():
 return board_slice[0]
 else:
 return 0

def reset(self):
 self.board = np.zeros((6,7), np.int8)
 self.winner = 0