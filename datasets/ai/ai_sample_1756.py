# Bubble Sort Algorithm
def bubbleSort(lst):
    n = len(lst) 
   
    # Traverse through all array elements 
	for i in range(n): 
 
		# Last i elements are already in place 
		for j in range(0, n-i-1): 
 
			# traverse the array from 0 to n-i-1 
			# Swap if the element found is greater 
			# than the next element
			if lst[j] > lst[j+1] : 
				lst[j], lst[j+1] = lst[j+1], lst[j]
 
# Driver code to test above
lst = [2, 4, 9, 5, 1]
bubbleSort(lst)

print ("Sorted array is:")
for i in range(len(lst)):
	print ("%d" %lst[i])