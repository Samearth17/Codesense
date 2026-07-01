def find_all_paths(graph, source, target):
    # create a queue list to store all the paths
    paths = queue.Queue()
    # initiate the queue with the source node
    paths.put([source])
    # create visited array to mark the visited nodes
    visited = [False]*len(graph)
    # update the source node as visited
    visited[source] = True
 
    # loop for finding all paths
    while not paths.empty():
        # Get the first path from the queue
        path = paths.get()
        # get the last node from the path
        last_node = path[-1]
        # if last node is the target
        if last_node == target:
            yield path
        # if last node is not the target
        else:
            # iterate for the adjacent nodes in the graph
            for adjacent in graph.get(last_node):
                # check if the adjacent node is not visited
                if not visited[adjacent]:
                    # create a new path, add the adjacent node 
                    # and update the visited array
                    new_path = list(path)
                    new_path.append(adjacent)
                    visited[adjacent] = True
                    # add the new path to the queue
                    paths.put(new_path)