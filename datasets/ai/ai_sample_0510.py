def intersection_arr(arr1, arr2):
    # create an empty list for storing the elements
    result = []
    
    for element in arr1:
        if element in arr2: 
            result.append(element)
    
    return result

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

intersect = intersection_arr(a, b)
print(intersect)