def solve(grid): 
  
    """solves a 9x9 sudoku grid   
    """
    row = 0
    col = 0
  
# Initially searching for an unassigned position 
    while row<9: 
        while col<9: 
            # If the entry is empty 
            if grid[row][col]==0: 
                for num in range(1,10): 
                    if check(grid, row, col, num): 
                        grid[row][col] = num     
  
                        # recursively checking 
                        if solve(grid):   
                            return True
                        else:
                            grid[row][col]=0
            # If the entry is not empty, go to the next position 
            col += 1  
            if col >= 9: 
                col = 0 
                row += 1 
   
# returning true when the whole grid is assigned with numbers
    return True
  
def check(grid, row, col, num): 
    # checking row and column 
    for i in range(0, 9): 
        # To check whether this num is  
        # already present in the row 
        if grid[row][i] == num:  
            return False
  
        # To check whether this num is 
        # already present in the column 
        if grid[i][col] == num: 
            return False
  
        
    # now checking in its block (3x3) 
    r = row - row%3
    c = col - col%3
  
    for i in range(3): 
        for j in range(3): 
            if grid[i+r][j+c] == num: 
                return False
  
    # If everything checks out, 
    # return true (num is not being used) 
    return True

# Driver program to test above function 
if __name__ == '__main__': 
  
    grid = [ 
        [7,8,0,4,0,0,1,2,0], 
        [6,0,0,0,7,5,0,0,9], 
        [0,0,0,6,0,1,0,7,8], 
        [0,0,7,0,4,0,2,6,0], 
        [0,0,1,0,5,0,9,3,0], 
        [9,0,4,0,6,0,0,0,5], 
        [0,7,0,3,0,0,0,1,2], 
        [1,2,0,0,0,7,4,0,0], 
        [0,4,9,2,0,6,0,0,7] 
    ]
    if solve(grid):
        for row in grid:
            print (*row, sep=' ')
    else: 
        print("No solution exists!")