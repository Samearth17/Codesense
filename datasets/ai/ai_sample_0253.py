def find_path(start, end, graph):
    # Initialize an empty list to store path
    path = []
    # Initialize a queue with start node
    q = [start]
    # Initialize a visited list
    visited = set()

    # Iterate until we get to the end node
    while q:
        node = q.pop(0)
        if node == end:
            path.append(node)
            return path
        elif node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                q.append(neighbour)
                path.append(node)
    return path