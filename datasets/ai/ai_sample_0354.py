def matrixMultiplication(A,B): 
 
    return [[sum(a*b for a,b in zip(A_row,B_col))  
                 for B_col in zip(*B)] for A_row in A] 

A = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]] 

B = [[7, 8, 9], 
     [4, 5, 6], 
     [1, 2, 3]]

C = matrixMultiplication(A,B) 

for i in range(len(C)): 
    print(C[i])