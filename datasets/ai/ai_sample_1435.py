def selection_sort(arr):
    # traverse through all array elements
    for i in range(len(arr)):
        # find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # swap the found minimum element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [5, 8, 10, 15, 2] 
selection_sort(arr)
print("Sorted array: ", arr)

Output: Sorted array:  [2, 5, 8, 10, 15]