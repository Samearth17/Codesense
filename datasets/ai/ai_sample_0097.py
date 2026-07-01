"""
Generate a code in Python to convert a number into binary format
"""
def convert_to_binary(num):
    # check if the number is 0, if so return 0
    if num == 0:
        return 0
    
    # initialize an empty binary string
    binary = ''
    
    # loop through the number and get the remainder 
    # which is the bits of the binary
    while num != 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    
    return binary

# test the function 
print(convert_to_binary(10)) # 1010