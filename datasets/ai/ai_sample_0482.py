def merge_sort(arr): 
    # Base case 
    if len(arr) <= 1:
        return arr
    else: 
        # Split array into two halves 
        mid = len(arr)//2
        left = arr[:mid] 
        right = arr[mid:] 

        # Call merge_sort recursively with each half 
        left = merge_sort(left) 
        right = merge_sort(right)
    
        # Merge each half 
        return merge(left, right) 
 
def merge(left, right): 
  
    # Initialize variables 
    result = [] 
    left_index = 0
    right_index = 0
   
    # result will be a sorted array
    while left_index < len(left) and right_index < len(right): 
        if left[left_index] < right[right_index]: 
            result.append(left[left_index]) 
            left_index += 1
        else: 
            result.append(right[right_index]) 
            right_index += 1
    
     # If left is longer, add remaining elements
    result += left[left_index:] 

    # If right is longer, add remaining elements
    result += right[right_index:] 
    return result