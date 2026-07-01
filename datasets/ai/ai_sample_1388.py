def find_all(arr, number): 
    if len(arr) < number: 
        return False

    temp = [False for i in range(number + 1)] 
  
    # mark each position present in the given list. 
    for i in range(len(arr)): 
        if arr[i] <= number: 
            temp[arr[i]] = True
    # check if all numbers are marked.  
    for i in range(1, number + 1): 
        if temp[i] == False: 
            return False

    return True

arr = [1, 3, 5, 2] 
number = 5
print(find_all(arr, number)) # True