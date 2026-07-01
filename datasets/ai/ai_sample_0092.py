# Python
def matrixMultiplication(A, B):
    if len(A[0]) != len(B):
        return "Matrix multiplication not possible"

    C = [[0 for i in range(len(A[0]))] for j in range(len(B[0]))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C

A = [[3, 4], 
     [1, 2]]
B = [[7, 5],
     [0, 1]]
C = matrixMultiplication(A, B)

print(C) # Output = [[21, 17], [0, 2]]