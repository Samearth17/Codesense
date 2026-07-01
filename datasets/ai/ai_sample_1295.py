import os
from collections import Counter
from nltk import word_tokenize

# Specify the directory containing the files
directory = 'articles_folder'

# Initialize a Counter object
word_counts = Counter()

# Iterate through all the files in the directory
for filename in os.listdir(directory):
  if filename.endswith('.txt'):
    with open(os.path.join(directory, filename)) as f:
      for line in f:
        tokens = word_tokenize(line)
        word_counts.update(tokens)

# Print the most common words
for word, count in word_counts.most_common(20):
  print(f'{word}: {count}')