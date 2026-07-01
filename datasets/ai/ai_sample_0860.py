def tsp(graph, start, end): 
    # Create an unvisited list 
    unvisited = {vertex: None for vertex in graph} 
    current = start 
    unvisited[current] = current 
    visited = dict() 
    route = list() 
  
    while True: 
        visited[current] = current 
        route.append(current) 
        unvisited.pop(current, None) 
        if current == end: 
            break
  
        min_dist = float('inf')
        for neighbour in graph[current].keys(): 
            if neighbour not in unvisited: 
                continue
            dist = graph[current][neighbour]
            if dist < min_dist: 
                min_dist = dist 
                next_vertex = neighbour 
  
        current = next_vertex 
  
    route.append(end) 
    return route