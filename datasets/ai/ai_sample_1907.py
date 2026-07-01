def matrixMultiplication(A, B):
	N = len(A)
	C = [[0 for x in range(N)] for y in range(N)]

	for i in range(N):
		for j in range(N):
			for k in range(N):
				C[i][j] += A[i][k] * B[k][j]

	return C

A = [[1,2],
     [3,4]]
B = [[4,3],
     [2,1]]

print(matrixMultiplication(A, B))

#output: [[8, 5], [20, 13]]