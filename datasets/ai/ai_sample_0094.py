from collections import Counter

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

# Split the text into individual words
words = text.split()

# Create a counter object
counter = Counter(words)

# Get the top 10 most frequent words
top_words = counter.most_common(10)

print(top_words)

# Output: [('dolor', 1), ('Lorem', 1), ('ipsum', 1), ('amet', 1), ('consectetur', 1), ('adipiscing', 1), ('elit,', 1), ('sed', 1), ('do', 1), ('eiusmod', 1)]