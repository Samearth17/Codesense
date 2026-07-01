def extract_unique_words(text): 
    # split the string into words 
    words = text.split() 
  
    # loop for each word in words 
    for i in range(0, len(words)): 
  
        # compare words 
        for j in range(i+1, len(words)): 
  
            # if a match is found 
            if (words[i] == words[j]): 
  
                # delete the word found at jth index 
                words.pop(j) 
  
    # return the unique words list  
    return words

unique_words = extract_unique_words(text)
print(unique_words)