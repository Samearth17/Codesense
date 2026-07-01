def find_max_value(lst):
    max_value = lst[0]
    for item in lst:
        # loop through list and compare each item with max_value 
        if item > max_value:
            max_value = item
    return max_value
 
lst = [1, -5, 8, 10, -2] 
  
# call the function
maximum_value = find_max_value(lst)
  
print("The maximum value in the list is", maximum_value)
# Output: The maximum value in the list is 10