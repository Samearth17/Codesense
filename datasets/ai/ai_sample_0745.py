def multiply(A, B):
        rows_A = len(A)
        cols_A = len(A[0])
        rows_B = len(B)
        cols_B = len(B[0])
        if cols_A != rows_B:
            # Check matrix dimensions
            print("Cannot multiply the two matrices. Incorrect dimensions.")
            return

        result = [[0 for row in range(cols_B)] for col in range(rows_A)]
    
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        return result