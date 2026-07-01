# Python program to calculate the dot product of two vectors

# vector A 
A = [1, 2, 3] 

# vector B 
B = [2, 3, 4] 

# dot product of two vectors 
dot_product = 0

# iterating over vector elements 
for i in range(len(A)): 
    dot_product += A[i] * B[i] 
# print the dot product 
print(dot_product) 

# Output: 20