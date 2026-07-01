# Sum of a list of numbers

# Defining the function
def sum_list(input_list): 
  
    # initializing sum to 0 
    total = 0
  
    # Iterating over the list 
    for num in input_list: 
        total += num 
  
    # Returning the total value 
    return total 
  
# Driver code 
list_of_numbers = [1,2,3,4,5]
result = sum_list(list_of_numbers)

print("Sum of the list =", result)