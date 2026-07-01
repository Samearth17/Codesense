def getMinMax(arr): 
    min = arr[0] 
    max = arr[0] 
  
    for i in range(len(arr)):  
        if arr[i] < min: 
            min = arr[i] 
        if arr[i] > max: 
            max = arr[i] 
  
    return min, max
  
# Driver Code 
arr = [2, 35, 12, 4, 88] 
min_val, max_val = getMinMax(arr) 
print("Minimum is", min_val) 
print("Maximum is", max_val) 
 
Output:
Minimum is 2
Maximum is 88