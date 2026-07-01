def perfect_numbers(n): 
   
    # Initialize perfect number list 
    perfect_number_list = [] 
  
    for num in range(1, n + 1): 
        sum = 0
        for i in range(1, num): 
            if num % i == 0: 
                sum += i 
  
        # If the sum of its divisor equals  
        # the number itself, then that   
        # number is a perfect number. 
        if sum == num: 
            perfect_number_list.append(num) 
  
    return perfect_number_list 

# Driver code 
n = 1000
print(perfect_numbers(n))