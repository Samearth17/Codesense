# Python program to find all unique triplets that sum up to 0
def find_triplets(arr):
  result = []
  n = len(arr)
  # Sort the array 
  arr.sort()

  # Fix the first element 
  # and find other two elements 
  for i in range(0,n-1):
    # Fix the second element and
    # find the third 
    l = i + 1
    r = n - 1
    while (l < r):
      sum = arr[i] + arr[l] + arr[r]
      if sum == 0: 
        result.append([arr[i],arr[l],arr[r]]) 
        l+=1
        r-=1
      # If the sum is lesser  
      # than zero, then increase 
      # the left bound    
      elif (sum < 0):
        l+=1
        
      # If the sum is greater 
      # then decrease the right bound 
      else: 
        r-=1
  return result

# Driver code
if __name__ == "__main__":
  arr = [-3, 0, 1, 2, -1, 1, -2] 
  result = find_triplets(arr)
  print(result)