def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = []
    right = []

    for element in array[1:]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)