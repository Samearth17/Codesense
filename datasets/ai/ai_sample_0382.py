"""
Classify a text into either spam or ham 
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def classify_spam(text):
    # Create a vectorizer object
    vec = CountVectorizer()
    
    # Tokenize the text
    X = vec.fit_transform([text])
    
    # Create a Multinomial NB model 
    model = MultinomialNB()
    model.fit(X, y)
    
    # Make predictions
    prediction = model.predict(X)
    
    if prediction[0] == 0:
        return 'ham'
    else:
        return 'spam'

if __name__ == '__main__':
    text = 'This is an example of a spam message.'
    print(classify_spam(text))