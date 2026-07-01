def quick_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    
    pivot = array[0]
    left = []
    right = []
    
    for i in range(1, len(array)):
        if array[i] <= pivot:
            left.append(array[i])
        else:
            right.append(array[i])
    
    left = quick_sort(left)
    right = quick_sort(right)
    
    return left + [pivot] + right