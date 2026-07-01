# Function to find the most efficient path
def find_path(start, end):
    # Current location of the robot
    x = start[0]
    y = start[1] 
    # Destination coordinates
    goal_x = end[0] 
    goal_y = end[1] 
    # set to record the cells already visited
    visited = set() 
    # define a queue to store the tuple of current position and the path
    queue = [([x, y], [])] 
    # define a neighbor list 
    neighbor = [[1, 0], [0, 1], [-1, 0], [0, -1]] 
    # define a maximum tries
    max_tries = 100 
    # define a while loop
    while queue:
        # get current position and current path
        position, path = queue.pop(0) 
        # check if the goal is reached
        if position[0] == goal_x and position[1] == goal_y:
            return path + [position]
        # check if the current position is out of maximum tries and not visited before
        if position not in visited and max_tries > 0:
            visited.add(position)
            max_tries = max_tries - 1 
            #get all neighbors of the current position
            for neighbor_x, neighbor_y in neighbor:
                next_x = position[0] + neighbor_x
                next_y = position[1] + neighbor_y
                # add to the queue
                queue.append(([next_x, next_y], path + [position]))
    return None
 
start = (4, 2) 
end = (9, 9) 
# most efficient path from start to end
path = find_path(start, end) 
print(path)