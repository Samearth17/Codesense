# Read the file
with open('text.txt') as f:
    # Get all the words from the file
    words = f.read().split()

# Count the frequency of each word
word_frequencies = {}
for word in words:
    if word not in word_frequencies:
        word_frequencies[word] = 1
    else:
        word_frequencies[word] += 1

# Sort the words based on their frequencies
sorted_words = sorted(word_frequencies.items(), key = lambda wf: wf[1], reverse=True)

# Print the 10 most frequently used words
print('10 most frequent words: ', end = '')
for i in range(10):
    print(sorted_words[i][0] + ("," if i != 9 else "."))