def min_cost(n, costs):
    # create cost matrix
    matrix = [[float('inf')] * n for _ in range(n)]
    matrix[0][0] = 0
    # populate cost matrix
    for cost in costs:
        start, end, value = cost[0], cost[1], cost[2]
        matrix[start][end] = value
    # traverse the matrix
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[j][k] > matrix[j][i] + matrix[i][k]:
                    matrix[j][k] = matrix[j][i] + matrix[i][k] 
    # find the minimum cost
    min_cost = float('inf')
    for row in matrix:
        min_cost = min(min_cost, min(row))
    return min_cost