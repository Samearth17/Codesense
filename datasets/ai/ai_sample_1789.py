def is_anagram(string1, string2): 
  
    # Create two lists from input strings 
    list_string1 = list(string1) 
    list_string2 = list(string2) 
  
    # If both strings are of different length then they  
    # cannot be anagram 
    if len(list_string1) != len(list_string2): 
        return False 
  
    # Sort both strings 
    list_string1.sort() 
    list_string2.sort() 
    
    # Compare sorted strings 
    if list_string1 == list_string2: 
        return True
    else: 
        return False