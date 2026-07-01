def subtractMatrix(A, B): 
  
    rowsA = len(A) 
    colsA = len(A[0]) 
    rowsB = len(B) 
    colsB = len(B[0]) 
  
    # Checking if the given two matrix are of same size 
    if rowsB != rowsA or colsA != colsB: 
        print("ERROR") 
     
    # Subtracting corresponding elements 
    C = [[0 for j in range(colsA)] for i in range(rowsB)] 
    for i in range(rowsA): 
        for j in range(colsB): 
            C[i][j] = A[i][j] - B[i][j] 
    return C