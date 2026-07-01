def primes(lst): 
 result = [] 
  
 # Iterate over the given list 
 for num in lst:  
      
    # If num is greater than 1  
    # so it must be prime 
    if num > 1: 
        for j in range(2, num): 
            if (num % j) == 0: 
                break 
        else: 
            result.append(num)  
  
 return result 

# Driver code 
lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(primes(lst)) 

# Output: [2, 3, 5, 7]