string = "This is a sample string."

# Split the string into individual words
words = string.split()

# Track the frequency of each word
word_freq = {}
for word in words:
 if word in word_freq:
 word_freq[word] += 1
 else:
 word_freq[word] = 1

# Sort the words by frequency
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Print the five most common words
common_words = sorted_words[:5]
for word, freq in common_words:
 print(f'{word}: {freq}')

# Output: 
# this: 1
# is: 1
# a: 1
# sample: 1
# string: 1