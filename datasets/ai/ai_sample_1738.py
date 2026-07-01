def display_min_max(arr):
    # initializing max and min element
    max_element = arr[0]
    min_element = arr[0]

    # traverse through the array elements
    for x in arr:
        if (x > max_element):
            max_element = x
        if (x < min_element):
            min_element = x

    # display max and min element
    print("The largest element is", max_element)
    print("The smallest element is", min_element)

# Driver code
arr = [2, 3, 8, 5, 10, 6]
display_min_max(arr)