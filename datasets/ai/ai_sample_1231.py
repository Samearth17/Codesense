def is_anagram(string1, string2): 
    # Remove white spaces from strings 
    string1 = string1.replace(" ", "") 
    string2 = string2.replace(" ", "") 
  
    # If strings have different length, 
    # then they are not anagrams 
    if len(string1) != len(string2): 
        return False
  
    # Sort both strings 
    string1 = sorted(string1) 
    string2 = sorted(string2) 
  
    # Compare sorted strings 
    for i in range(0, len(string1)): 
        if string1[i] != string2[i]: 
            return False 
  
    return True