def find_max(arr): 
    # Initialize max 
    max = arr[0] 
  
    # Traverse from arr[1] to end 
    for i in range(1, len(arr)): 
  
        # Compare every element with current max 
        if arr[i] > max: 
            max = arr[i] 
              
    return max

arr = [2, 4, 6, 1, 7, 12] 

result = find_max(arr)
print(result)