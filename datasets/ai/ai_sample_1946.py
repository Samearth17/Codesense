def has_duplicates(arr): 
    # Create an empty set 
    s = set() 
  
    # Traverse through the list 
    for item in arr:
        # If the element is present 
        # in the set then it is a duplicate 
        if item in s:
            return True 
        else:
            s.add(item) 

    # No duplicate element found 
    return False