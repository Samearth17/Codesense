def merge_arrays(arr1, arr2):
    len1, len2 = len(arr1), len(arr2)
    
    # initialize empty result list and pointers to traverse the both array
    arr_merged, i, j = [], 0, 0
    
    # traverse both array and compare the element
    # append the lesser one to result
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            arr_merged.append(arr1[i])
            i += 1
        else:
            arr_merged.append(arr2[j])
            j += 1
    
    # append remaining elements(if any) of faster completed array to result
    while i < len1:
        arr_merged.append(arr1[i])
        i += 1
    while j < len2:
        arr_merged.append(arr2[j])
        j += 1
    return arr_merged