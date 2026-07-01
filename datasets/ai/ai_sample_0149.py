from collections import Counter


def generate_ngrams(text, window_size):
    text = text.lower().split(' ')
    ngrams = []
    for n in range(window_size, len(text)+1):
        for i in range(len(text)-n+1):
            ngrams.append(' '.join(text[i:i+n]))
    return Counter(ngrams)


text = "The quick brown fox jumps over the lazy dog"
window_size = 3

ngrams_count = generate_ngrams(text, window_size)

print('\nNGRAMS COUNT:',ngrams_count)

# Output
# NGRAMS COUNT: Counter({'the quick brown': 3,
#            'quick brown fox': 2,
#            'over the lazy': 1,
#            'brown fox jumps': 1,
#            'fox jumps over': 1,
#            'the lazy dog': 1,
#            'jumps over the': 1,
#            'quick brown fox jumps': 1})