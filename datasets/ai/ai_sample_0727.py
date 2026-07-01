"""
Create a program to sort the elements of an unsorted array using the bubble sort technique in Python
"""
def bubbleSort(arr):
	length = len(arr)
	for i in range(length):
		for j in range(length-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr
 
# Driver Code
arr = [4, 5, 7, 3, 8, 1, 9]
 
result = bubbleSort(arr)
 
print(result)