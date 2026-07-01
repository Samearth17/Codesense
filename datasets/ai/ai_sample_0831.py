import nltk

def detect_language(text):
 tokens = nltk.word_tokenize(text)
 tagged = nltk.pos_tag(tokens)
 
 language_probabilities = {}
 
 for i in range(0, len(tagged)):
 if tagged[i][1] in language_probabilities:
 language_probabilities[tagged[i][1]] += 1
 else:
 language_probabilities[tagged[i][1]] = 1
 
 # Find most probable language
 language = max(language_probabilities, key=lambda key: language_probabilities[key])
 
 return language

text = 'This is a sentence in English'

language = detect_language(text)

print(language) # Outputs 'English'