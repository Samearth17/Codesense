class WordCounter:
    def __init__(self):
        self.count = 0
    
    def countWords(self, text):
        words = text.split() # Splits the sentence into a list of words
        self.count = len(words) # Counts the number of words
        return self.count

# Creating an instance of the WordCounter class
wordCounter = WordCounter()

# Counting the words in the text
wordCount = wordCounter.countWords("Hello world, this is a test")

print(wordCount) # Outputs 4