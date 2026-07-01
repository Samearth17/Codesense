# Create a dictionary to record the frequency of words in a given string

# Split the string into words
words = "this is a test string".strip().split()

# We use a dictionary to store the frequency of the words
freq = {}

# Iterate through the words and count their frequency
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)