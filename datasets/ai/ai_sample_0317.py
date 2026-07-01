# Merge Sort Algorithm

def merge(left, right):
  sortedList = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      sortedList.append(left[i])
      i += 1
    else:
      sortedList.append(right[j])
      j += 1
  # Check if anything remains
  sortedList += left[i:]
  sortedList += right[j:]
  return sortedList

def mergeSort(arr):
  # Base case, already sorted
  if len(arr) <= 1:
    return arr

  # Split in half
  mid  = len(arr)/2
  left = arr[:mid]
  right = arr[mid:]
  
  # Sort each half and merge
  left  = mergeSort(left)
  right = mergeSort(right)
  return merge(left, right)

# Driver Code
arr = [6,2,5,1,8,9,0]

sortedArr = mergeSort(arr)
print(sortedArr)

# Output: [0, 1, 2, 5, 6, 8, 9]