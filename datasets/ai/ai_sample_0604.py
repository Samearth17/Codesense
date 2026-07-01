def bin_to_dec(binary_str):
 # Initialize the result
 result = 0
 
 # Iterate through the string and add each digit to the result
 for d in binary_str:
  # Multiply the result by 2 for each digit of the string
  result = result * 2
  # Add the current digit to the result
  result += int(d)
 
 # Return the result
 return result

binary_str = '10101'
print(bin_to_dec(binary_str))
# Output: 21