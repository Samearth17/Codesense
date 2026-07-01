def count_islands(grid): 
    if not grid: 
        return 0 
  
    row = len(grid) 
    col = len(grid[0]) 
  
    num_islands = 0
  
    for i in range(row): 
        for j in range(col): 
            if grid[i][j] == 1: 
                num_islands += dfs(grid, i, j, row, col) 
  
    return num_islands 
  
  
def dfs(grid, i, j, row, col): 
    if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0: 
        return 0
  
    grid[i][j] = 0
  
    dfs(grid, i + 1, j, row, col) 
    dfs(grid, i - 1, j, row, col) 
    dfs(grid, i, j + 1, row, col) 
    dfs(grid, i, j - 1, row, col) 
  
    return 1