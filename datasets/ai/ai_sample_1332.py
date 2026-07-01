def classify_words(words):
    """Classify a list of words into two categories depending on length"""
    # Initialize empty lists
    short_words = []
    long_words = []
    # Loop through the words
    for word in words:
        # Add the word to the short list if it is less
        # than 7 characters, otherwise add it to the long list
        if len(word) < 7:
            short_words.append(word)
        else:
            long_words.append(word)

    return short_words, long_words

# Output
print(classify_words(words))