def merge_sort(A, B):
 result = [] 
 i, j = 0, 0

# Compare elements and add lower one to result
while i < len(A) and j < len(B):
 if A[i] < B[j]:
 result.append(A[i])
 i += 1
 else:
 result.append(B[j])
 j += 1

# Add remaining elements
result += A[i:]
result += B[j:]

return result

#Test the algorithm
A = [3, 6, 8, 10, 11]
B = [2, 5, 7, 12]

print(merge_sort(A, B))
# Output: [2, 3, 5, 6, 7, 8, 10, 11, 12]