def is_armstrong_number(num): 
 
    # Calculate the number of digits 
    n = len(str(num)) 
  
    # Check whether is an armstrong number 
    sum = 0 
    temp = num 
    while temp > 0: 
        digit = temp % 10
        sum += digit ** n 
        temp //= 10
  
    if num == sum: 
        return True
    else: 
        return False