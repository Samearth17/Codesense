# Bubble sort algorithm
def bubble_sort(unsortedList):
 n = len(unsortedList) 
   
 # Traverse through all array elements 
for i in range(n): 
    # Last i elements are already in place 
    for j in range(0, n-i-1): 
  
        # traverse the array from 0 to n-i-1 
        # Swap if the element found is greater 
        # than the next element 
        if unsortedList[j] > unsortedList[j+1] : 
            unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j] 
  
# Driver code to test above 
unsortedList = [14, 2, 27, 10, 5] 
bubble_sort(unsortedList) 
  
print ("Sorted array is:") 
for i in range(len(unsortedList)): 
    print ("%d" %unsortedList[i]),