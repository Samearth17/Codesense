from collections import deque

# Helper function to get the neighbors of a cell
def get_neighbors(cell):
     x, y = cell[0], cell[1]
     neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
     return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < 6 and 0 <= neighbor[1] < 6]

# Helper function to get the cost of a cell
def get_cost(cell):
     x, y = cell[0], cell[1]
     return abs(x-5) + abs(y-5)  

# Find the shortest path from the source to the destination
def find_shortest_path(source, destination):
     # Create a queue to store the cells to be visited
     cells_to_visit = deque([source])

     # Create a dictionary to store the parent cell for each cell
     parents = {source: None}

     while cells_to_visit:
         current_cell = cells_to_visit.popleft()

         # Find the neighbors of the current cell
         neighbors = get_neighbors(current_cell) 

         # Iterate over the neighbors
         for neighbor in neighbors:
             # Get the cost of the neighbor
             neighbor_cost = get_cost(neighbor)

             # If the neighbor has not been visited yet
             if neighbor not in parents:
                 # Update the queue
                 cells_to_visit.append(neighbor)

                 # Update the parents dictionary
                 parents[neighbor] = current_cell

                 # If the neighbor is the destination
                 if neighbor == destination:
                     shortest_path = []
                     current = destination 
                     while current is not None:
                         shortest_path.append(current)
                         current = parents[current]
                     return reversed(shortest_path)

# Call the find_shortest_path function
shortest_path = find_shortest_path([0, 0], [5, 5])

# Print the shortest path
print('The shortest path is:')
print(list(shortest_path))