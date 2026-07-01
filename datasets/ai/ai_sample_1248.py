def searchElement(arr, x): 
    for i in range(len(arr)): 
        if arr[i] == x: 
            return i
    return -1
    
arr = [2, 4, 6, 8]
x = 8

result = searchElement(arr, x) 

if(result == -1): 
  print("Element is not present in array") 
else: 
  print("Element is present at index", result)