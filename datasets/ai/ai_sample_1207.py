import numpy as np

# define the number of rows and columns
N, M = 6, 8

# define the start and target nodes
source = (1, 0)
target = (4, 6)

# list of obstacles 
obstacle_coords = [(2, 4), (3, 3)]

# define the data representing open nodes/obstacles
# 0 stands for open node, 1 for obstacle
matrix = [
 [0, 0, 0, 0, 1, 1, 0, 0],
 [0, 1, 1, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
]

# convert the matrix to a NumPy array
nodeInfo = np.array(matrix)

# define the A* algorithm
def aStar(openNodes, source, target):
    
 # repeat until there are no more open nodes
 while openNodes: 
 
  # sort the nodes according to their heuristic scores
  openNodes.sort(key=lambda x: x.cost + x.heuristic) 
  
  # get current node (lowest score)
  current_node = openNodes.pop(0) 
  
  # check if target is reached
  if current_node == target: 
   path = []
   current = current_node 
   while current is not None: 
    path.append(current.position) 
    current = current.parent 
   return path[::-1]
  
  # get all neighbours
  for neighbour in current_node.neighbours:
   new_cost = current_node.cost + current_node.distance(neighbour) 
  
   # determine if neighbour is in closed or open set
   if neighbour in closedSet:
    if neighbour.cost > new_cost:
     closedSet.remove(neighbour) 
     neighbour.cost = new_cost
     neighbour.parent = current_node 
     heappush(openNodes, neighbour)
  
   elif neighbour in openSet:
    if neighbour.cost > new_cost:
     neighbour.cost = new_cost
     neighbour.parent = current_node 
  
   else:
    neighbour.cost = new_cost
    neighbour.parent = current_node 
    heappush(openNodes, neighbour)
  
  closedSet.append(current_node)