def get_unique_words(word_string):
    word_string = word_string.lower() # Convert the string to lower case
    words = word_string.split() # Split the string into a list of words
    unique_words = [] # Create an empty list to store unique words
    
    # Iterate over the list of words and check if the word is already 
    # present in the list of unique words.
    # If not, then append the word to the list of unique words.
    for word in words:
        if word not in unique_words: 
            unique_words.append(word) 
  
    # Return the list of unique words
    return unique_words

print(get_unique_words("This is a test"))