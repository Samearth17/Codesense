def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
    arr = quicksort(left) + [pivot] + quicksort(right)
    return arr

arr = [1, 5, 8, 7, 2]
sorted_arr = quicksort(arr)
print(sorted_arr)