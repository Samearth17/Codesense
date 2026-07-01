# Maze Class 
class Maze: 
  
    # Maze constructor 
    def __init__(self): 
        self.n = 5
        self.maze = [[ 1, 0, 0, 0, 1 ], 
                     [ 1, 1, 1, 0, 1 ], 
                     [ 0, 0, 0, 0, 0 ], 
                     [ 0, 1, 1, 1, 1 ], 
                     [ 0, 1, 0, 0, 1 ]] 
   
    # function to print the maze 
    def printMaze(self): 
        for i in range(self.n): 
            for j in range(self.n): 
                print(self.maze[i][j], end =" ") 
            print () 
   
    # function to check if maze is solved or not 
    def isSolved(self, x, y): 
        if x == self.n - 1 and y == self.n - 1: 
            return True
        return False

# Driver Function 
if __name__ == "__main__": 
    mazeObj = Maze() 
    mazeObj.printMaze() 
    print("Is the maze solved? :", 
          mazeObj.isSolved(0, 0))