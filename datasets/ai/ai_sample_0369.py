def getStringLengths(words):
    # Create an empty dictionary 
    lengths = {} 

    # For each word in the list of words
    for word in words:
        # find the length of the word
        length = len(word)
        # add the length of the word to the dictionary
        lengths[word] = length 

    # return the dictionary
    return lengths

print(getStringLengths(["apple", "mango", "banana"]))