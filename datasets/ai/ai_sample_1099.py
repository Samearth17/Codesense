# Return the longest increasing subsequence
def lis(arr): 
  n = len(arr) 
  
  # Initialize LIS values for all indexes 
  lis = [1]*n 
 
  # Compute LIS values from left to right 
  for i in range (1, n): 
    for j in range(0, i): 
      # lis[i] = max(lis[i], lis[j] + 1) if arr[i] > arr[j] 
      if arr[i] > arr[j] and lis[i] < lis[j] + 1 : 
        lis[i] = lis[j]+1
  
  # Return the maximum value
  return max(lis)