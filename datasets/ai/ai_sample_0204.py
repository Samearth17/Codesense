class WordCounter:
    def __init__(self, filename):
        self.word_counts = {}
        self.filename = filename
        self.process_file()

    def process_file(self):
        with open(self.filename) as f:
            for line in f:
                words = line.split()
                for word in words:
                    if word in self.word_counts:
                        self.word_counts[word] += 1
                    else:
                        self.word_counts[word] = 1

    def get_word_counts(self):
        return self.word_counts