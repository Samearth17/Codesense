import collections
import string

# define punctuation
punctuations = string.punctuation

# open the file and read lines
with open('words.txt', 'r') as f:
    words = f.readlines()

# remove punctuation and make all words lowercase
words = [word.strip(punctuations).lower() for word in words]

# count the words and store the word count in dictionary
word_count = collections.Counter(words)

# sort the data and get the top ten words
top_ten_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]

# print the results
print("Result:")
for word in top_ten_words:
    print(f"{word[0]} {word[1]}")