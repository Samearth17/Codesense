def merge_sorted_lists(list1, list2):
    # Create a new list for the result
    result = [] 
    # Make iterators for both lists
    iter1 = iter(list1)  
    iter2 = iter(list2) 
    # Initialize the elements to compare
    elem1 = next(iter1, None) 
    elem2 = next(iter2, None)  
  
    # Compare the elements of both lists 
    while elem1 is not None and elem2 is not None: 
        # Pick the smaller element 
        if elem1 <= elem2: 
           result.append(elem1) 
           elem1 = next(iter1, None)  
        else: 
           result.append(elem2) 
           elem2 = next(iter2, None) 
  
    # Append the remaining elements of list1  
    if elem1 is not None: 
        result.append(elem1) 
        for elem1 in iter1: result.append(elem1) 
  
    # Append the remaining elements of the list2  
    if elem2 is not None: 
        result.append(elem2) 
        for elem2 in iter2: 
            result.append(elem2) 
  
    return result