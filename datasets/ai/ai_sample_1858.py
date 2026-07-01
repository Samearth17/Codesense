def min_sum_array(arr):
 minimum = arr[0]
 total = 0

 for i in range (0, len(arr)):
  element = arr[i]
  if element < minimum:
   minimum = element
   total += element
 
 return total

arr = [13, -2, 7, -6, 5]
min_sum = min_sum_array(arr)
print(min_sum) # Output: -11