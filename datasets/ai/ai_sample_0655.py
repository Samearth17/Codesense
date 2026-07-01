# Python code

# input text
text = "the quick brown fox jumps over the lazy dog"

# store words in list
words = text.split()

# empty dictionary to store word frequencies
word_freq = {}

# loop through list of words
for word in words:
  # check if word is already in the dictionary
  if word in word_freq:
    # if so, increase count by 1
    word_freq[word] += 1
  else:
    # if not, add it to the dictionary with count = 1
    word_freq[word] = 1

# print the output
print("Word Frequency Histogram")
for word, freq in word_freq.items():
 print(word + ' |' + '*' * freq)