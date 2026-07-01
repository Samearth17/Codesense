import re

text = "The quick brown fox jumped over the lazy dog"

# Extract words from the document
words = re.findall(r'\w+', text)

# Get the frequency of each word
word_freq = {} 
for word in words: 
    if word not in word_freq: 
        word_freq[word] = 0
    word_freq[word] += 1

# Sort words in descending order by frequency
sorted_word_freq = sorted(word_freq.items(), key = lambda x: x[1], reverse = True) 
  
# Print the top 10 most frequent words
print("Top 10 most frequent words:") 
for word, freq in sorted_word_freq[:10]: 
    print(word, ' :', freq)