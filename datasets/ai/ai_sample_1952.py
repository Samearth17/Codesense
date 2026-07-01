def solveNQueens(n): 
  
    # A utility function to check if 
    # a queen can be placed on board[row][col]
    # Note that this function is called when 
    # "col" queens are already placed in columns 
    # from 0 to col -1. So we need to check 
    # only left side for attacking queens 
    def is_safe(row, col): 
  
        # Check this row on left side 
        for i in range(col): 
            if board[row][i] == 1: 
                return False
  
        # Check upper diagonal on left side 
        for i, j in zip(range(row, -1, -1),  
                        range(col, -1, -1)): 
            if board[i][j] == 1: 
                return False
  
        # Check lower diagonal on left side 
        for i, j in zip(range(row, n, 1),  
                        range(col, -1, -1)): 
            if board[i][j] == 1: 
                return False
  
        return True
  
    # Place N queens on an NxN board 
    def solve(n): 
      
        # A board for the queen positions 
        board = [[0 for _ in range(n)] for _ in range(n)] 
      
        # A list to store the positions of the queens 
        result = [] 
  
        # Start from the first column 
        solveQueen(board, 0, result) 
        return result 
  
    # Function to check if the queen can be 
    # placed or not 
    def solveQueen(board, col, result): 
      
        # If all the queens are already placed 
        if col == n: 
            # Add the result to the result list 
            # Append the list of a single result 
            result.append(list()) 
            # Add the queen's positions to the current list 
            for i in range(n): 
                current_result = [] 
                for j in range(n): 
                    # Add only the positions with the queen 
                    # in it to the current list 
                    if board[i][j] == 1: 
                        current_result.append(j + 1) 
                # Add the current list to the result list 
                result[-1].append(current_result) 
            return
  
        # Try the current row
        for i in range(n): 
  
            # If the column of the current row is safe 
            # for the queen
            if is_safe(i, col): 
              
                # Place the queen
                board[i][col] = 1
  
                # Increase the column by 1 
                # and recursively call the 
                # function for the next column 
                solveQueen(board, col + 1, result) 
  
                # Else backtrack 
                board[i][col] = 0
  
    # start solving
    result = solve(n) 
  
    # Print the result
    for res in result: 
        print(res) 
  
n = 4
solveNQueens(n)