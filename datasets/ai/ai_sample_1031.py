def generate_path(grid): 
#initialize an empty list to hold the path
path = [] 
#initialze to false
visited = [[false for x in range(5)] for y in range(5)] 
#start from the top left corner
x = 0 
y = 0 

while (x != 4 and y != 4): 
  #mark the node as visited
  visited[x][y] = True 
  #check if it is possible to go down 
  if y+1<5 and visited[x][y+1] != True and grid[x][y+1] == 0 : 
    path.append("down")
    y = y+1 
 #check if it is possible to go right 
 elif x+1<5 and visited[x+1][y] != True and grid[x+1][y] == 0 : 
    path.append("right")
    x = x+1 
 #backtrack
 else: 
    if path[-1] == "down" : 
            y = y-1 
    else: 
            x = x-1
    path.pop() 

#mark the end/destination cell as visited
visited[4][4] = True
#append the path to tuhe list
path.append("Destination Reached") 

#return the optimal path
return path