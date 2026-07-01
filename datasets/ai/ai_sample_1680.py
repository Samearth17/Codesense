from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

category = ['rec.sport.hockey', 'talk.politics.mideast']

newsgroups_train = fetch_20newsgroups(subset='train', categories=category)

# Transform the training data using TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(newsgroups_train.data)
y_train = newsgroups_train.target

# Create multinomial Naive Bayes classifier
clf = MultinomialNB(alpha=.01)
clf.fit(X_train, y_train)

# Define a function that takes an article and predicts its class
def predictClass(article):
    X_test = vectorizer.transform([article])
    y_test = clf.predict(X_test)
    if y_test[0] == 0:
        return 'Sports'
    else:
        return 'Politics'