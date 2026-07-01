def freq_word(sentence):
    words = sentence.split()
    # make a dictionary to count the occurrance of each word
    d = {}
    for word in words:
        # if the word is already in the dictionary, increment its count
        if word in d.keys():
            d[word] += 1
        # else add the word in the dictionary
        else:
            d[word] = 1
    # set the first most_freq to the first word in the sentence
    most_freq = words[0]
    # loop trough the words
    for word in words:
        # if we find a word with higher frequency, set most_freq to that word
        if d[word] > d[most_freq]:
            most_freq = word
    return most_freq