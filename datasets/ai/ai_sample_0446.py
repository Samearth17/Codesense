def binary_search(array, target):
  left = 0
  right = len(array) - 1
  while left <= right:
      middle = (left + right)//2
      if array[middle] < target:    
          left = middle + 1
      elif array[middle] > target:  
          right = middle - 1
      else:                         
          return middle             
  return -1                        

position = binary_search(array, number) 
if position == -1:
  print("Number not found in array.")
else:
  print(f"{number} found at position {position}")