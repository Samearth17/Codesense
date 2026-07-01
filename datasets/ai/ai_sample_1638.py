def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2 # floor division
    guess = arr[mid]

    if guess == target:
      return mid
    elif guess > target:
      high = mid - 1
    else:
      low = mid + 1
  return None