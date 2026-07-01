def maxSubarrySum(arr):
  cur_max = 0
  global_max = 0
  
  for i in arr:
    cur_max = max(cur_max + i, 0)
    global_max = max(global_max, cur_max)
    
  return global_max
  
# test
arr = [1, -2, 3, 4, -5]
print(maxSubarrySum(arr))

# output: 7