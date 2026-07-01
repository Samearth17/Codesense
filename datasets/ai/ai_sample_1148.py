def quick_sort(arr):
    """Sort an array using the quick sort algorithm."""
    # Base case: array of length 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot element
    pivot = arr[0]
    
    # Create two lists to hold elements greater or less than the pivot
    less_than_pivot = []
    greater_than_pivot = []
    
    # Compare each element in the array to the pivot
    for elem in arr:
        if elem < pivot:
            less_than_pivot.append(elem)
        elif elem > pivot:
            greater_than_pivot.append(elem)
            
    # Recursively sort the two lists
    less_than_pivot = quick_sort(less_than_pivot)
    greater_than_pivot = quick_sort(greater_than_pivot)
    
    # Combine the two lists with the pivot in the middle
    sorted_arr = less_than_pivot + [pivot] + greater_than_pivot
    return sorted_arr