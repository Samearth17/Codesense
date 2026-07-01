# function to perform bubble sort
def bubble_sort(arr): 
    # iterate over a range of the length of the array
    for i in range(len(arr)): 
  
        # iterate over the array until the index is equal to the current 
        # iteration of the first loop
        for j in range(0, len(arr)-i-1): 
  
            # compare two adjacent elements
            # if the one on the left is greater than the one on the right, 
            # swap them
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# driver code to test the above code 
arr = [3, 5, 1, 9, 6] 
bubble_sort(arr)
  
# print the sorted array 
print ("Sorted array is:") 
for i in range(len(arr)):
    print ("%d" %arr[i], end=' ')