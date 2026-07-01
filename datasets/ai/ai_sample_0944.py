arr = [[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9]] 

# Initialize result 
result = 0

# Iterate every element in the array 
for row in arr: 
  for col in row:
    # Adding elements of each row 
    result = result + col  

# Displaying sum 
print(result)

# Output: 45