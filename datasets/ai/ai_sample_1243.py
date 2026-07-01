def max_product_of_two(arr):
    n = len(arr)
    if n == 0:
        return None

    max_val1 = arr[0]
    for i in range(1, n):
        if arr[i] > max_val1:
            max_val1 = arr[i]

    max_val2 = arr[0]
    for i in range(1, n):
        if arr[i] > max_val2 and arr[i] != max_val1:
            max_val2 = arr[i]

    return max_val1 * max_val2