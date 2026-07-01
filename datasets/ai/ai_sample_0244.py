# Matrix multiplication in Python

matrix_A = [[2, 3], [4, 7]] 
matrix_B = [[6, 5], [1, 4]] 
  
# result matrix
result = [[0, 0], [0, 0]] 
  
# iterating by row of Matrix A 
for i in range(len(matrix_A)): 
  
    # iterating by coloum of Matrix B  
    for j in range(len(matrix_B[0])): 
  
        # iterating by rows of Matrix B 
        for k in range(len(matrix_B)): 
            result[i][j] += matrix_A[i][k] * matrix_B[k][j] 
  
for r in result: 
    print(r)