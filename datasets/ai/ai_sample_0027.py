def is_armstrong_number(num):   
    n = len(str(num)) 
    # initialize sum  
    temp = num  
    sum_of_digits = 0
  
    # find sum of nth power of individual digits  
    while temp > 0:  
        digit = temp % 10  
        sum_of_digits += digit ** n  
        temp //= 10  
  
    # if num is equal to sum_of_digits then the number is an Armstrong number  
    if num == sum_of_digits:  
        return True 
  
    else: 
        return False