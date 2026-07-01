# imports 
import re
import string
from collections import Counter

# read the html file
html text = ""
with open('example.html', 'r') as f:
 html_text = f.read()

# remove punctuation from the html file
for char in string.punctuation:
 html_text = html_text.replace(char, "")

# split file into words
words = html_text.split()

# count the occurrence of each word
word_counts = Counter(words)

# print the most frequent word
print("Most frequent words: ")
for word in word_counts.most_common():
 print(word[0])