def find_maximum(list): 
    
    # Base case
    if len(list) == 1: 
        return list[0] 
    
    # Recursive case
    else: 
        sub_max = find_maximum(list[1:]) 
        # Compare the sub_maximum with the first
        # element of the list and return the 
        # maximum of the two 
        return max(list[0], sub_max) 
    
# Driver Code
list = [3, 9, 7, 6]
print(find_maximum(list))