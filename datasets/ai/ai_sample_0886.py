# function to perform quick sort
def QuickSort(arr):
    # base case 
    if len(arr) <= 1:
        return arr
    
    # Select pivot
    pivot = arr[len(arr) // 2]
    # partition the array
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # recursive call
    return QuickSort(left) + middle + QuickSort(right)

# unsorted list
arr = [10, 7, 8, 9, 1, 5]
# Print the sorted array
print("Sorted array is: ", QuickSort(arr))