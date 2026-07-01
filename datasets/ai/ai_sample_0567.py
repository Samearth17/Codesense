def most_frequent_words(s):
    # Split string into list of words
    words = s.split(' ')
    # Create empty dictionary to store word frequencies
    word_frequencies = {}
    # Iterate through words in list
    for word in words:
        # If word is already in the dictionary, increment its frequency
        if word in word_frequencies:
            word_frequencies[word] += 1
        # Otherwise, set frequency to 1
        else:
            word_frequencies[word] = 1
    # Sort words by frequency
    sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
    # Return a list of the most frequent words
    return [item[0] for item in sorted_words]