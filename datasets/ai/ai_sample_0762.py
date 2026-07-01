def monkey_sort(arr): 
 
    # Check array length 
    arr_len = len(arr) 
  
    # Create a copy of the array 
    result = arr.copy() 
  
    # Randomly shuffle the elements of the array  
    # until it is sorted 
    while(result != sorted(result)): 
        for i in range(arr_len): 
            r = random.randint(0, arr_len - 1) 
            result[i], result[r] = result[r], result[i] 
  
    # Return the sorted array 
    return result 

# Driver code 
arr = [7, 5, 4, 9, 6, 2, 1, 8] 
print(monkey_sort(arr))