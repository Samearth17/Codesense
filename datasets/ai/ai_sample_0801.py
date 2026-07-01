def search_array(array, element):
    # loop through array
    for i in range(len(array)):
        # compare array element and search element
        if array[i] == element:
            # return index if elements are equal
            return i
    # return -1 if search element is not found
    return -1

array = [3, 5, 7, 8, 9]
element = 5

index = search_array(array, element)
if index != -1:
    print("Element {} found at index {}".format(element, index))
else:
    print("Element not found.")