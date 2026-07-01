import spacy
import nltk
from nltk.corpus import opinion_lexicon
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC

# Download and create a spaCy model
nlp = spacy.load('en_core_web_sm')

# Create a list of positive, negative and neutral words
positive_words = opinion_lexicon.positive()
negative_words = opinion_lexicon.negative()
neutral_words = list(set(nlp.vocab.words) - set(positive_words) - set(negative_words))

# Create a Bag of Words Vectorizer
vectorizer = CountVectorizer(vocabulary=list(positive_words + neutral_words + negative_words))

def create_examples(words, sentiment):
    examples = []
    # Create BOW for each example
    for w in words:
        bow = vectorizer.transform([w])
        examples.append((bow, sentiment))
    return examples

# Create training examples
positive_examples = create_examples(positive_words, 'POSITIVE')
negative_examples = create_examples(negative_words, 'NEGATIVE')
neutral_examples = create_examples(neutral_words, 'NEUTRAL')

# Create training data
train_data = positive_examples + negative_examples + neutral_examples

# Train a classifier
classifier = LinearSVC()
classifier.fit([x[0] for x in train_data], [x[1] for x in train_data])

def predict_sentiment(sentence):
    # Create BOW of sentence
    bow = vectorizer.transform([sentence])
    # Get sentiment
    sentiment = classifier.predict(bow)[0]
    return sentiment

sentence = 'I had a great time today!'
sentiment = predict_sentiment(sentence)
print('The sentiment of the sentence is:', sentiment)