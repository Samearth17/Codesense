import nltk

def synonyms_words(text):
    text_tokens = nltk.word_tokenize(text)
    replacement_words = []
    
    for token in text_tokens:
        synonyms = nltk.wordnet.synsets(token)
        if synonyms:
            replacement_words.append(synonyms[0].name().split('.')[0])
        else:
            replacement_words.append(token)

    return ' '.join(replacement_words)

text = "this is an example sentence"
print(synonyms_words(text))