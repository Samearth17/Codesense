# Function to print the minimum number in a list 
def min_in_list(list): 
    # Inialise minimum to first element in the list 
    min = list[0] 
  
    # Traverse through the list from 1st index 
    # and update minimum if found 
    for i in range(len(list)): 
        if list[i] < min: 
            min = list[i] 
  
    return min
  
# Driver Code 
list = [5, 12, 3, 1, 8] 
print ("Minimum in the list is ", min_in_list(list))