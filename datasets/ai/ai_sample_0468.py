def same_case(string1, string2): 

    # Take the lengths of two strings into consideration 
    if len(string1) != len(string2): 
        return False
        
    # Compare character by character 
    # If any one of the characters are not of same case 
    # return false 
    for x, y in zip(string1, string2): 
        if x.islower() != y.islower(): 
            return False

    # If execution reaches this point 
    # it means that all characters of both strings 
    # are having same case 
    return True