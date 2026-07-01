def multiply_matrix(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
 
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
 
A = [[1, 2],
     [3, 4]]
B = [[1, 2],
     [2, 3]]
 
print(multiply_matrix(A,B))