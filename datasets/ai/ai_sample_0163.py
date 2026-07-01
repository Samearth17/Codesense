# Function to filter an array by a given criteria
def filter_array(array, criteria):
 # Create an empty list
 filtered_array = []
 # Iterate through the array
 for value in array:
  # Check if it matches the criteria
  if criteria(value):
   # If it matches, add it to the list
   filtered_array.append(value)

 # Return the filtered array
 return filtered_array

# Input criteria
def criteria(x):
 return x % 5 == 0

result = filter_array(array, criteria)
print(result) # Outputs [5, 10, 15, 20, 25, 30]