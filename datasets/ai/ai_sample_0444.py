import nltk
from nltk.classify import maxent
from nltk.tokenize import word_tokenize

# define the categories
CATEGORIES = ['noun', 'verb', 'adjective', 'adverb', 'other']

# generate training data
training_data = [
    ("That's an interesting book.", {'category': 'noun'}),
    ("Can I borrow it?", {'category': 'verb'}),
    ("It's really amazing.", {'category': 'adjective'}),
    ("I'm learning a lot.", {'category': 'adverb'}),
    ("It's blue.", {'category': 'other'})
]

# create a feature extractor
def extract_features(sentence):
 words = word_tokenize(sentence)
 features = {}
 for w in words:
 features[w.lower()] = True
 return features

# train the classifier
classifier = maxent.MaxentClassifier.train(
training_data, 'GIS', trace=0, encoding=None, labels=CATEGORIES
)

# classify a sentence
sentence = "It's yellow."
features = extract_features(sentence)
label = classifier.classify(features)

# print the result
print(label) # other