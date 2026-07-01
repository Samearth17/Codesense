def find_binary_representation(num):
    # base case 
    if num == 0: 
        return 0
  
    # stores the binary representation
    bin_rep = ""  
  
    # to store the remainder 
    rem = 0
  
    while (num != 0): 
        # calculate remainder
        rem = num % 2
        bin_rep += str(rem)
        num //= 2
  
    # reverse the string and return it
    bin_rep = bin_rep[::-1]
    return bin_rep


# Main program
num = 42
binary_rep = find_binary_representation(num)
print(binary_rep)