def sumDigits(num): 
  
    # convert number into string 
    # and convert each digit into number 
    # using ord() and store it in list 
    # convert number into string 
    # and convert each digit into number 
    # using ord() and store it in list 
    strNum = str(num) 
    digits = [int(x) for x in strNum] 
  
    # return sum using sum() function 
    return sum(digits) 
  
# Driver program 
num = 12345
print("Sum of digits in num is:", 
        sumDigits(num))