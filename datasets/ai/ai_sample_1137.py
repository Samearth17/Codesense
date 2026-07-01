def selection_sort(arr):
  
  # Iterate through array 
  for i in range(0, len(arr)-1): 
    # Find the minimum element in the unsorted subarray 
    min_index = i 
    for j in range(i+1, len(arr)): 
        if arr[min_index] > arr[j]: 
            min_index = j 
  
    # Swap the found minimum element with the first element         
    arr[i], arr[min_index] = arr[min_index], arr[i] 
  
# Driver code 
arr = [2, -3, 1, 10, 0] 
selection_sort(arr) 
  
for i in range(len(arr)): 
    print(arr[i]),