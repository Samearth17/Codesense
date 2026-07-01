def linearSearch(arr, value):
  for i in range(len(arr)):
    if arr[i] == value:
      return i  # value found, return index
  return -1  # value not found

arr = [5, 3, 7, 2]
searchValue = 7

result = linearSearch(arr, searchValue)

if result == -1:
  print("Element not found")
else:
  print("Element present at index", result)