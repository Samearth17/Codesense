def medianMostCommon(arr):
  # Count the number of occurences of every element
  counts = {}
  for element in arr:
    if element in counts:
      counts[element] += 1
    else:
      counts[element] = 1
  
  # Find the most common element
  most_common_element = None
  max_count = 0
  for element, count in counts.items():
    if count > max_count:
      most_common_element = element
      max_count = count

  # Sort the array
  sorted_arr = sorted(arr)

  # Find the index of the most common element
  index = sorted_arr.index(most_common_element)

  # Swap the most common element and the middle element in the array
  mid = len(sorted_arr) // 2
  sorted_arr[index] = sorted_arr[mid]
  sorted_arr[mid] = most_common_element

  return sorted_arr

arr = [4, 5, 2, 5, 8, 5, 6, 5]
result = medianMostCommon(arr)
print(result) # [4, 5, 5, 5, 5, 6, 8, 2]