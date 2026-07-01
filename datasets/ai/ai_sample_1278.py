sentence = 'The quick brown fox jumps over the lazy dog'

# Split the sentence into individual words
words = sentence.split(' ')

# Create an empty dictionary
word_count = {}

# Count the number of times each word appears
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the results
for word in word_count:
    print("{}: {}".format(word, word_count[word]))