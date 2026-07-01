def sort(arr): 
    n = len(arr) 
    
    for i in range(n-1): 
        min_index = i 
        for j in range(i+1, n): 
            if arr[min_index] > arr[j]: 
                min_index = j 
                  
        arr[i], arr[min_index] = arr[min_index], arr[i] 
        
    return arr

list = [3, 5, 2, 1, 4] 
print(sort(list)) # [1, 2, 3, 4, 5]