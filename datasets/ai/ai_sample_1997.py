def median(arr): 
  
    # Sort the array 
    arr.sort() 
  
    # Calculate the index of the middle element 
    if len(arr) % 2 == 0: 
        # If the number of elements is even 
        mid = int(len(arr)/2) 
        median = (arr[mid] + arr[mid-1])/2
    else: 
        # If the number of elements is odd 
        mid = int(len(arr)/2) 
        median = arr[mid] 
   
    return median

arr = [4, 5, 2, 7, 1] 
print(median(arr))