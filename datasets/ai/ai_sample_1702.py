def travellingSalesmanProblem(graph, s): 
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(len(graph)): 
        if i != s: 
            vertex.append(i) 
    # store minimum weight Hamiltonian Cycle 
    min_path = float("inf") 
  
    while True: 
        # stoar current Path weight(cost) 
        current_pathweight = 0
          
        # compute current path weight 
        for i in range(len(vertex)): 
            current_pathweight += graph[s][vertex[i]] 
  
        # update minimum 
        min_path = min(min_path, current_pathweight) 
  
        if len(vertex) == 0: 
            break
        else: 
            s = vertex[0] 
            vertex.remove(s) 
    return min_path

# driver program to test the above function
if __name__ == "__main__": 
    # matrix representation of graph 
    graph = [[0, 2, 3, 8], 
            [2, 0, 5, 7],  
            [3, 5, 0, 6], 
            [8, 7, 6, 0]] 
    s = 0
    print(travellingSalesmanProblem(graph, s)) 
# Output: 13