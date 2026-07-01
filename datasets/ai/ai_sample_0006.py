def solve_sudoku(board): 
  
    # Utility function to find vacant cells 
    # Returns a boolean     
    def find_vacant_cell(board, l): 
        for row in range(9): 
            for col in range(9): 
                if board[row][col] == 0: 
                    l[0] = row 
                    l[1] = col 
                    return True
        return False
  
    # Utility function to check if a number  
    # is not currently placed in a particular  
    # row, column and block 
    def is_safe(board, row, col, num): 
  
        # Check if 'num' is not already placed  
        # in current row, current column  
        # and current 3x3 box 
        for i in range(9): 
  
            # Check the rows
            if(board[row][i] == num): 
                return False
  
            # Check the columns 
            if(board[i][col] == num): 
                return False
  
            # Check the 3x3 boxes 
            if(board[(row//3)*3 + i//3][(col//3)*3 + i%3] == num): 
                return False
  
        return True
  
    # Solve the sudoku 
    def solve(board): 
        # 'l' is a list variable that keeps 
        # the record of row and col in 
        # find_vacant_cell function 
        l = [0, 0] 
  
        # If there is no unassigned location, 
        # we are done 
        if (not find_vacant_cell(board, l)): 
            return True
  
        # Assigning the list values
        row = l[0] 
        col = l[1] 
  
        # consider digits 1 to 9 
        for num in range(1, 10): 
  
            # if it is a safe position
            if (is_safe(board, row, col, num)): 
  
                # make tentative assignment 
                board[row][col] = num 
  
                # return if succcess
                if (solve(board)): 
                    return True
  
                # failure, unmake and try again 
                board[row][col] = 0
  
        # trigger backtracking 
        return False
  
    #Driver Program 
    if (solve(board)): 
        for row in board: 
            print(row) 
    else: 
        print("No solution")