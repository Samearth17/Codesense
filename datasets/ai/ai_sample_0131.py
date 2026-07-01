import nltk
from nltk.classify import NaiveBayesClassifier 
  
def label_words(words): 
    return dict([(word, True) for word in words]) 

positive_tokens = nltk.word_tokenize(positiveText) 
negative_tokens = nltk.word_tokenize(negativeText)

positive_data = [(label_words(positive_tokens), 'positive')] 
negative_data = [(label_words(negative_tokens), 'negative')]
 
train_data = positive_data + negative_data 
classifier = NaiveBayesClassifier.train(train_data) 
  
# classify 
classifier.classify( 
	label_words(nltk.word_tokenize("This movie was ok")))