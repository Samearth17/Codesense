import re
import matplotlib.pyplot as plt

# Get the sentence
sentence = "This is a sentence with a lot of different words."

# Get all the words
words = re.findall(r'\w+', sentence)

# Count the frequency of each word
frequency = {}
for word in words:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

# Create the labels and counts for the histogram
labels, counts = list(frequency.keys()), list(frequency.values())

# Plot the histogram using matplotlib
plt.bar(labels, counts, width=0.8, align='center')
plt.title('Frequency of Words')
plt.show()