import pandas as pd

# Load the data
data = pd.read_csv('./dataset.csv')

# Get the text and the labels
texts = data['text'].values
labels = data['label'].values

# Generate a dictionary of all the words in the dataset
words = set()
for text in texts:
 for word in text.split():
 words.add(word)

# Create a dictionary of word counts
word_counts = {}
for word in words:
 word_counts[word] = 0

# Count the number of times each word appears in each sentiment label
for i in range(len(texts)):
 for word in texts[i].split():
 if labels[i] == 0:
 word_counts[word] -= 1
 else:
 word_counts[word] += 1

# Print out the words with the highest sentiment polarity
sorted_words = sorted(word_counts.items(), key=lambda x: x[1])

for word, count in sorted_words[:10]:
 print(f'{word}: {count}')