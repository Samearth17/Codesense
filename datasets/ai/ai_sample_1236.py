# Function to count words
def word_count(string):
 
 # Create a dictionary to store results
 words = {}
 
 # Split the string into words
 for word in string.split():
 
  # Check if the word is in the dictionary
  if word in words:
   # Increment the count
   words[word] += 1
  else:
   # Add the word to the dictionary
   words[word] = 1
 
 return words

# Test
string = 'This is a test string to count the words in the string.'
print(word_count(string)) # Output: {'This': 1, 'is': 1, 'a': 1, 'test': 1, 'string': 2, 'to': 1, 'count': 1, 'the': 1, 'words': 1, 'in': 1}