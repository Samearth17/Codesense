def isValidISBN(input):
    '''
    This function takes a string of numbers as input 
    and returns True if it is a valid ISBN 
    otherwise False.
    '''

    # Check length of string
    if len(input) != 10:
        return False
    
    # Convert string to an array of integers
    digits = list(map(int, input))
    
    # Calculate checksum
    chksm = 0
    for i in range(len(digits)):
        chksm += digits[i] * (10 - i)
    
    # Verify checksum
    return (chksm % 11) == 0