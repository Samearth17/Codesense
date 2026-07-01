def binary_search(arr,target):
  low = 0
  high = len(arr) - 1
  while low <= high: 
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target: 
      low = mid + 1
    else: 
      high = mid - 1
  return -1

arr = [2, 3, 4, 10, 40]
target = 10
index = binary_search(arr, target)
if index != -1: 
    print("Element is present at index", index)
else: 
    print("Element is not present in the array")