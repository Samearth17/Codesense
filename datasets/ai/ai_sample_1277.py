# create the grid function
def createGrid(length, width): 
    grid = [[0 for x in range(width)] for y in range(length)] 
    return grid 
  
# initialise the grid with cells 
def initGrid(grid): 
    for i in range(len(grid)): 
        for j in range(len(grid[i])): 
            grid[i][j] = int(random.random()+.5) 
    return grid 
  
# display the grid 
def display(grid): 
    for i in range(len(grid)): 
        for j in range(len(grid[i])): 
            print(grid[i][j], " ", end="") 
        print() 
  
# make each cell follow the game rules 
def updateGrid(grid): 
    newGrid = [[0 for x in range(len(grid[0]))] for y in range(len(grid))] 
  
    for i in range(len(grid)): 
        for j in range(len(grid[i])): 
            # calculate the current cell's neighbors 
            neighbors = 0
            for k in range(-1, 2): 
                for l in range(-1, 2): 
                    if k == 0 and l == 0: 
                        continue
                    elif (i+k >= 0 and i+k < len(grid) and 
                            j+l >= 0 and j+l < len(grid[i])): 
                        neighbors += grid[i+k][j+l] 
  
            # rule 1 and rule 3 
            if (grid[i][j] == 1 and (neighbors < 2 or neighbors > 3)): 
                newGrid[i][j] = 0
            # rule 4 
            elif (grid[i][j] == 0 and neighbors == 3): 
                newGrid[i][j] = 1
            # rule 2 
            else: 
                newGrid[i][j] = grid[i][j] 
    return newGrid 

size = 10
grid = createGrid(size, size)
grid = initGrid(grid) 
  
# display the initial grid 
print("Initial Grid") 
display(grid) 
  
# update the grid for 25 iterations 
for i in range(25): 
    print("Iteration", i+1) 
    grid = updateGrid(grid) 
    display(grid)