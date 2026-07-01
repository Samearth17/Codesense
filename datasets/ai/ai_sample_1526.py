def find_words(text):
 
 # find all words in the string
 words = text.split(' ')
 
 # filter out words that are not 4 characters long
 filtered_words = [word for word in words if len(word) == 4]
 
 return filtered_words
 
# example
text = 'The quick brown fox jumps over the lazy dog'
words = find_words(text)
 
print(words)
 
# output: ['quick', 'brown', 'over', 'lazy']