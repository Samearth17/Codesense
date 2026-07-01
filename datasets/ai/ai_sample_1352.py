import nltk
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier

# Create a function to classify the sentence
def classify_sentence(sentence):
    # Create a list of words derived from the sentence
    words = word_tokenize(sentence)

    # Collect words and their corresponding part of speech tags
    words_tags = nltk.pos_tag(words)
    
    # Create lists to contain nouns, verbs, adjectives and adverbs
    nouns = []
    verbs = []
    adjectives = []
    adverbs = []

    # Iterate through each word and tag in the sentence
    for word, tag in words_tags:
        if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
            nouns.append(word)
        elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            verbs.append(word)
        elif tag in ['JJ', 'JJR', 'JJS']:
            adjectives.append(word)
        elif tag in ['RB', 'RBR', 'RBS']:
            adverbs.append(word)

    # Return a dictionary containing the detected words
    return {
        'nouns': nouns,
        'verbs': verbs,
        'adjectives': adjectives,
        'adverbs': adverbs
    }

sentence = 'The dog barked at the cat.'

# Classify the sentence
classified_sentence = classify_sentence(sentence)

# Print the results
print(classified_sentence)

# Output:
# {'nouns': ['dog', 'cat'], 'verbs': ['barked'], 'adjectives': [], 'adverbs': []}