def max_sum_subarray(arr): 
    n = len(arr) 
    max_sum = 0
  
    for i in range(n): 
        sum = arr[i] 
        for j in range(i + 1, n): 
            sum += arr[j] 
            if sum > max_sum: 
                max_sum = sum 

    return max_sum 

# Test array 
arr = [2, -1, 3, 5, -7, 3] 

# Function Call 
max_sum = max_sum_subarray(arr) 
  
# Printing maximum sum 
print("Maximum sum of the sub-array is", max_sum) 

# Output: Maximum sum of the sub-array is 8