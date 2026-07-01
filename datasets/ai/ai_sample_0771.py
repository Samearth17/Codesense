def findMode(arr): 
 max_count = 1 
 mode = arr[0] 
 count = 1 
  
 for i in range(1,len(arr)): 
 if (arr[i] == arr[i - 1]): 
 count = count + 1 # increment count
 if (count > max_count): 
 max_count = count # update max_count 
 mode = arr[i] 
 else: 
 count = 1 # reset count 
  
 return mode 

# Driver program 
arr = [2, 4, 3, 3, 5, 3, 7] 
print(findMode(arr)) # prints 3