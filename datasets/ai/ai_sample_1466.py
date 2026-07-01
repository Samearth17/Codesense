def most_frequent_words(text):
    # convert the text into a list of words
    words = text.split()

    # create an empty dictionary
    word_count = {}

    # count each word and store it in the dictionary
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # sort the dictionary by frequency
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # return the most frequently used words
    most_frequent_words = [word[0] for word in sorted_word_count[:10]]
    return most_frequent_words