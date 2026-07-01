def binary_search(arr, item):
 first = 0
 last = len(arr) - 1
 found = False
 
 while(first <= last and not found):
 mid = (first + last) // 2
 if arr[mid] == item:
 found = True
 else:
 if item < arr[mid]:
 last = mid - 1
 else:
 first = mid + 1
 
 return found
 
array = [1, 3, 5, 7, 9, 11, 13, 15, 17]
item = 9

result = binary_search(array, item)
if result:
 print('Element present in the array') 
else:
 print('No such element')