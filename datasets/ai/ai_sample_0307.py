def compute_readability(text):
    """Compute the readability score of a given text"""
    words = 0
    sentences = 0
    syllables = 0
    for word in text.split():
        words += 1
        syllables += count_syllables(word)

    for sentence in text.split("."):
        sentences += 1

    score = 206.835 - (1.015 * (words / sentences)) - (84.6 * (syllables / words))
    return score

def count_syllables(word):
    """Count the number of syllables in a given word"""
    vowels = "aeiouAEIOU"
    syllables = 0
    for letter in word:
        if letter in vowels:
            syllables += 1
    if len(word) >= 3 and word[-3:] == "ely" or word[-2:] == "es":
        syllables -= 1
    return syllables