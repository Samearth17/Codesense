def binary_search(arr, x): 
    low = 0
    high = len(arr) - 1
      
    while low <= high: 
        mid = (high + low) // 2
        if arr[mid] < x: 
            low = mid + 1
        elif arr[mid] > x: 
            high = mid - 1
        else: 
            return mid 
  
arr = [2, 8, 10, 17, 19, 25, 28]
x = 19
result = binary_search(arr, x)
print(result)