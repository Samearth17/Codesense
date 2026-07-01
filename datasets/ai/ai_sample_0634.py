def reverse_array(arr): 
      
    # Initialize start and end index 
        start = 0
        end = len(arr) - 1
  
    # Loop over the array 
    while start < end: 
  
        # Swap the elements at start and end 
        arr[start], arr[end] = arr[end], arr[start]  
          
        # Update start and end index 
        start += 1
        end -= 1
  
# Driver code 
arr = [1, 2, 3] 
  
reverse_array(arr) 
  
# Print our modified array   
print(arr)