def decimalToBinary(num): 
    # empty list to store the binary number 
    binaryList = [] 
   
    # if the number is 0, return 0
    if num == 0:
        return [0]
  
    # loop until the number becomes 0 after division by 2
    while num > 0:
        binaryList.append(num % 2) 
        num //= 2
  
    # Reverse the list
    binaryList = binaryList[::-1] 
  
    return binaryList