# Array to search
sortedArray = [1, 2, 3, 4, 5, 6, 7]

# Target value
value = 5

# Binary search function
def binarySearch(array, target):
 # Find the middle of the array
 mid = len(array) // 2
 
 # Check if the target is equal to the middle value 
 if array[mid] == target:
  return True
 
 # If the target is less than the middle value, search the left half
 elif target < array[mid]:
  return binarySearch(array[:mid], target)
  
 # If the target is greater than the middle value, search the right half
 elif target > array[mid]:
  return binarySearch(array[mid+1:], target)
 
 # If the target is not found
 else:
  return False
  
# Check if the value is in the array
if binarySearch(sortedArray, value):
 print('Value found!')
else:
 print('Value not found!')