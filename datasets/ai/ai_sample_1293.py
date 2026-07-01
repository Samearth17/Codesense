def multiply_matrices(m1, m2):
 if len(m1[0]) != len(m2):
 raise ValueError('The matrices cannot be multiplied.')

 # Create the result matrix
 # Dimensions would be m1 rows x m2 columns
 result = [[0 for col in range(len(m2[0]))] for row in range(len(m1))]

 for i in range(len(m1)):
 # Iterate through rows of m1
 for j in range(len(m2[0])):
 # Iterate through columns of m2
 for k in range(len(m2)):
 result[i][j] += m1[i][k] * m2[k][j]
 return result

# Test
m1 = [[1, 2], [3, 4]]
m2 = [[2, 0], [1, 2]]

result = multiply_matrices(m1, m2)
for row in result:
 print(row)

# Output
# [4, 4]
# [10, 8]