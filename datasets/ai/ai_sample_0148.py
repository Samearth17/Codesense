def add_large_numbers(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1] 
    carry = 0
    result = "" 
   
    # Iterate over the length of the length of larger string  
    for i in range(max(len(num1), len(num2))): 
        if i < len(num1):
            digit1 = int(num1[i])
        else:
            digit1 = 0

        if i < len(num2):
            digit2 = int(num2[i])
        else:
            digit2 = 0
       
        sum_total = digit1 + digit2 + carry  
        carry = sum_total // 10  

        result += str(sum_total % 10) 

    # Add remaining carry  
    if carry > 0:  
        result += str(carry) 

    return result[::-1]

print(add_large_numbers("111", "1337"))
# Output: 1448