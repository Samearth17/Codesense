def countIslands(grid):
 count = 0

 for i in range(len(grid)):
  for j in range(len(grid[0])):
   if grid[i][j] == 1:
    dfs(grid, i, j)
    count += 1

 return count

def dfs(grid, r, c):
 if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
  return
 grid[r][c] = 0
 dfs(grid, r+1, c)
 dfs(grid, r, c+1)
 dfs(grid, r-1, c)
 dfs(grid, r, c-1)

print(countIslands([[1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 1],
                    [1, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 1]]))
// Output: 5