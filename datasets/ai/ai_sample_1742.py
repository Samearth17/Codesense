def maxSubArraySum(arr):
  max_so_far = 0 
  max_ending_here = 0 
  
  for i in range(0, len(arr)): 
      max_ending_here = max_ending_here + arr[i] 
    
      if (max_ending_here < 0): 
          max_ending_here = 0
    
      if (max_so_far < max_ending_here): 
          max_so_far = max_ending_here 
 
  return max_so_far 

# Test
arr = [1, -2, 3, 4, -5, 6]
max_sum = maxSubArraySum(arr)

print('Max Sum =', max_sum)