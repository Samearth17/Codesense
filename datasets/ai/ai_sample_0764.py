def validateCreditCardNumber(number):
    
    # Reverse of the card number
    rev_number = number[::-1]
    
    # Declare a sum of all digits
    sum_of_digits = 0
    
    for i in range(len(rev_number)):
        digit = int(rev_number[i])
        
        # For alternate digits multiply by 2
        if i % 2 != 0:
            digit *= 2
        
        # Add the higher digit of each result to the sum
        if digit > 9:
            sum_of_digits += digit // 10 + digit % 10
        else:
            sum_of_digits += digit
            
    # If the sum is divisible by 10 its a valid card number
    return sum_of_digits % 10 == 0

print(validateCreditCardNumber('45397431 85747991'))
// Output: True