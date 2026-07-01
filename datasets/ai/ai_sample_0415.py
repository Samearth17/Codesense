def sort(array):
  # base case: if array is empty or has only one element, it is already sorted
  if len(array) <= 1:
    return array

  # divide array into two halves
  midpoint = len(array) // 2
  left = array[:midpoint]
  right = array[midpoint:]

  # recursively sort left and right subarrays
  left = sort(left)
  right = sort(right)

  # merge two sorted halfs
  return merge(left, right)

def merge(left, right):
  result = []
  left_index = 0 # index of the left subarray
  right_index = 0 # index of the right subarray

  # keep going until one of the two subarrays is depleted
  while left_index < len(left) and right_index < len(right):
    if left[left_index] <= right[right_index]:
      # add the smallest element and increment its index
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1
  
  # we must have reached the end of the left or right subarray
  # append all remaining elements
  for i in range(left_index, len(left)):
    result.append(left[i])
  for i in range(right_index, len(right)):
    result.append(right[i])
  
  return result

# Test code
array = [4, 2, 9, 7, 3]
sorted_array = sort(array)
print(sorted_array)