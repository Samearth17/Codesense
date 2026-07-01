def merge_arrays(arr1, arr2):
    merged_arr = []
    # Make copies of arrays
    arr1_copy = arr1[:]
    arr2_copy = arr2[:]
    
    # add elements from both array in sorted order
    while arr1_copy and arr2_copy:
        if arr1_copy[0] <= arr2_copy[0]:
            merged_arr.append(arr1_copy.pop(0))
        else:
            merged_arr.append(arr2_copy.pop(0))
            
    # add remaining elements of array
    if arr1_copy:
        merged_arr.extend(arr1_copy)
    else:
        merged_arr.extend(arr2_copy)
    
    # return merged array
    return merged_arr

arr1 = [3, 8, 11]
arr2 = [1, 4, 9]

print(merge_arrays(arr1, arr2))