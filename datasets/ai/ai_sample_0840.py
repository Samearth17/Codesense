def is_isogram(string):
    # empty strings are isograms
    if len(string) == 0:
        return True

    # convert string to lowercase 
    string = string.lower()

    # create a set to store seen letters 
    seen_letters = set()

    for char in string:
        # if char is not seen, add it to set 
        if char not in seen_letters:  
            seen_letters.add(char) 
        
        # if char is already seen, it is not an isogram  
        else: 
            return False

    # all letters are unique, it is an isogram
    return True