# Algorithm to solve a 9x9 sudoku

def solve(board):
    # Function to check if a given position on the board is empty
    def is_empty(board):
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == 0:
                    return (row, col)
        return None

    # Function to check if a given number is valid in the given position on the board
    def is_safe(board, row, col, num):
        for position in range(0, 9):
            # checking for row
            if board[row][position] == num and position != col:
                return False
            # checking for column
            if board[position][col] == num and position != row:
                return False

        # checking for subboxes
        upper_row = row - row%3
        upper_col = col - col%3
        for r in range(upper_row, upper_row + 3):
            for c in range(upper_col, upper_col + 3):
                if board[r][c] == num and (r, c) != (row, col):
                    return False
        
        return True

    next_num = is_empty(board)
    if not next_num:
        return True

    row, col = next_num

    for number in range(1, 10):
        if is_safe(board, row, col, number):
            board[row][col] = number

            if solve(board):
                return True

            # backtracking
            board[row][col] = 0

    return False

board = [
 [3, 0, 6, 5, 0, 8, 4, 0, 0],
 [5, 2, 0, 0, 0, 0, 0, 0, 0],
 [0, 8, 7, 0, 0, 0, 0, 3, 1],
 [0, 0, 3, 0, 1, 0, 0, 8, 0],
 [9, 0, 0, 8, 6, 3, 0, 0, 5],
 [0, 5, 0, 0, 9, 0, 6, 0, 0],
 [1, 3, 0, 0, 0, 0, 2, 5, 0],
 [0, 0, 0, 0, 0, 0, 0, 7, 4],
 [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

solve(board)

for row in range(9):
    for col in range(9):
        print(board[row][col], end=" ")
    print()