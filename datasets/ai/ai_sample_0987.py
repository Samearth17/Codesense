class CountUniqueWords:

    def __init__(self, sentence):
        self.sentence = sentence
        self.unique_words = []
    
    def count_unique_words(self):
        words = self.sentence.split()
        for word in words:
            if word not in self.unique_words:
                self.unique_words.append(word)
        return len(self.unique_words)

sentence = "Hello world. This is a sample sentence."
c = CountUniqueWords(sentence)
print(c.count_unique_words())