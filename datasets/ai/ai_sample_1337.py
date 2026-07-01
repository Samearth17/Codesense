def binary_search(arr, x):
 n = len(arr)
 
 # Sort the given array in ascending order
 arr.sort()
 
 # print all elements
 for i in range(n):
 print(arr[i], end = " ")
 
 #binary search
 start = 0
 end = n-1
 
 while start <= end:
    mid = (start + end) // 2
    if x == arr[mid]:
 return mid 
 elif x > arr[mid]:
 start = mid + 1
 else:
 end = mid - 1
 
 return -1