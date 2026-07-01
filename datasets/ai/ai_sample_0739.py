def max_pos(mat):
 max_v = -float('inf')
 max_i = -1
 max_j = -1
 
 for i in range(len(mat)):
  for j in range(len(mat[i])):
   if mat[i][j] > max_v:
    max_i = i
    max_j = j
 
 return (max_i, max_j)
 
matrix = [[2, 8, 7], [3, 11, 5], [1, 9, 4]]
pos = max_pos(matrix)
print(pos) # (1, 1)