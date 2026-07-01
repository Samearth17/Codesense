def findMin(arr): 
   
    # Initialize minimum element 
    min = arr[0] 
   
    # Traverse array elements starting from 
    # 1st to the last 
    for i in range(1, len(arr)): 
        if arr[i] < min: 
            min = arr[i]
   
    return min

arr = [10, 11, 8, 9, 2] 
print(findMin(arr))