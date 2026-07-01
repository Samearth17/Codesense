# Function to count number of words
def count_words(text):
 words = text.split()

 return len(words)


# Function to count number of characters
def count_characters(text):
 return len(text)


# Function to count number of sentences
def count_sentences(text):
 sentences = text.split('.')
 
 return len(sentences)

 
text = "The quick brown fox jumps over the lazy dog."

num_words = count_words(text)
print(f"Number of words: {num_words}")

num_characters = count_characters(text)
print(f"Number of characters: {num_characters}")

num_sentences = count_sentences(text)
print(f"Number of sentences: {num_sentences}")