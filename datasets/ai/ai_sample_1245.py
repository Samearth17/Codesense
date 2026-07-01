def matrix_multiply(matrixA, matrixB):
    if len(matrixA[0]) != len(matrixB):
        print("Error: The number of columns of matrix A is not equal to the number of rows of matrix B")
        return
 
    m, n, p = len(matrixA), len(matrixA[0]), len(matrixB[0])
    result = [[0 for i in range(p)] for j in range(m)]
    # multiplying matrix A and matrix B 
    for i in range(m): 
        for j in range(p): 
            for k in range(n):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
  
    return result

# Example
mata = [[2, 4, -3], 
        [6, 1, 0]] 
matb = [[1, -1],  
        [2, 0], 
        [3, 4]]

res = matrix_multiply(mata, matb)

for row in res:
   print(row)

# Output
# [4, -4] 
# [24, 12]