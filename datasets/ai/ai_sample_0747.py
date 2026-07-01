def remove_overlap(string1, string2): 
    #split string1 into a list of words
    words1 = string1.split()
    #split string2 into a list of words
    words2 = string2.split()
    #initialize an empty list
    result = []
    #compare between the two words list 
    for word in words1:
        if word not in words2:
            result.append(word)
    #join string2 into the result list
    result = result + words2
    # join the result list into a single string
    new_string = ' '.join(result)
  
    return new_string

#call the remove_overlap()function
result = remove_overlap(string1, string2)
print(result)