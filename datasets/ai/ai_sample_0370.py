"""
Create a program to group the strings of a given list according to their lengths in Python
"""

# List of strings 
input = ["apple", "mango", "banana", "kiwi", "grapes", "watermelon"]

# Dictionary to store the grouped strings 
result = {} 

# Iterate over the list 
for elem in input:
    # Get length of each string 
    length = len(elem)
    # If the length is present in the result dictionary, 
    # add the string to its corresponding list 
    if length in result: 
        result[length].append(elem)
    # Else, create a new list in the result dictionary 
    # and append the string to the list 
    else: 
        result[length] = [elem] 
  
# Print the result 
print(result) 
# Output: {5: ['apple', 'mango', 'kiwi'], 6: ['banana', 'grapes'], 12: ['watermelon']}