def most_frequent_words(text):
    # Split the text into words
    words = text.split() 
    # Create an empty dictionary
    word_counter = {}
    
    # Iterate through each word in the list of words
    for word in words:
        # If the word is already in the dictionary
        if word in word_counter:
            # Add 1 to the count of the word
            word_counter[word] += 1 
        else:
            # Else, set the count of the word to 1
            word_counter[word] = 1
            
    # Sort the dictionary by value
    word_sorted = sorted(word_counter.items(), 
                         key=lambda count: count[1], 
                         reverse=True)
    
    # Return the words with highest frequency
    return [word_sorted[0][0], word_sorted[1][0], 
            word_sorted[2][0]]