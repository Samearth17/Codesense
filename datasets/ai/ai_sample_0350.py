def sort(arr): 
    n = len(arr) 
  
    for i in range(n): 
  
        min_index = i # assuming current element is smallest 
          
        # look for smallest element in the rest of the array 
        for j in range(i+1, n): 
            if arr[j] < arr[min_index]: 
                min_index = j 
  
        arr[i], arr[min_index] = arr[min_index], arr[i] # swap 
  
    return arr
  
arr = [5, 4, 3, 1, 2] 
sorted_arr = sort(arr) 
  
print(sorted_arr)