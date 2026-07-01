def find_words(text):
    """Find all the words in the given text."""
    return text.split()

def find_word_count(text):
    """Find the number of words in the given text."""
    words = find_words(text)
    return len(words)

def find_average_word_length(text):
    """Find the average word length in the given text."""
    words = find_words(text)
    total_len = 0
    for word in words:
        total_len += len(word)
        
    return total_len/len(words)