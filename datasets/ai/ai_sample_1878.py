class TextProcessor:
  def __init__(self):
    self.frequency_map = {}

  def process_text(self, text):
    clean_text = self._preprocess_text(text)
    word_list = clean_text.split()
    self._count_frequencies(word_list)

  def _preprocess_text(self, text):
    # Strip punctuation, convert to lower case, etc.
    return text.strip().lower()

  def _count_frequencies(self, word_list):
    for word in word_list:
      if word in self.frequency_map:
        self.frequency_map[word] += 1
      else:
        self.frequency_map[word] = 1