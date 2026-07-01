def edit_distance(str1, str2):
 # convert the strings into a list of characters
 list_str1 = list(str1)
 list_str2 = list(str2)
 
 # create a matrix to store the result
 matrix = [[0 for x in range(len(list_str2)+1)] for x in range(len(list_str1)+1)]
 
 # create the matrix in bottom up manner 
 for i in range(len(list_str1)+1):
  for j in range(len(list_str2)+1):
   # if the first string is empty
   if i == 0:
    matrix[i][j] = j
   # if the second string is empty
   elif j == 0:
    matrix[i][j] = i
   # if the last characters of both strings match
   elif list_str1[i-1] == list_str2[j-1]:
    matrix[i][j] = matrix[i-1][j-1]
   # if the last characters of both strings do not match
   else:
    matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
 
 # return the last element of the matrix
 return matrix[-1][-1]

str1 = "editing"
str2 = "distance"

print(edit_distance(str1, str2))
# Output: 5