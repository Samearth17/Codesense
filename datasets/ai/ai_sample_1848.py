def binarySearch(arr, x): 
	start = 0
	end = len(arr) - 1
	
	while start <= end: 
	
		mid = start + (end - start) // 2
	
		if arr[mid] == x: 
			return mid 
	
		elif arr[mid] < x: 
			start = mid + 1
	
		else: 
			end = mid - 1
	
	return -1

arr = [ 1, 3, 5, 7, 9 ]
result = binarySearch(arr, 3) 

if result != -1: 
	print("Element is present at index", str(result)) 
else: 
	print("Element is not present in array")