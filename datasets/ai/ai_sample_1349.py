def sort_array(arr):
 n = len(arr)
 
 # Iterate through the array
 for i in range(n):
 
 # Find the minimum element 
 min_ind = i
 for j in range(i + 1, n):
 if arr[min_ind] > arr[j]:
 min_ind = j
 
 # Swap the found minimum element with the first element 
 arr[i], arr[min_ind] = arr[min_ind], arr[i]

# Driver code to test above 
arr = [6,5,3,1,8,7,2,4]
sort_array(arr)

print ("Sorted array is:")
for i in range(n):
 print ("%d" %arr[i]),