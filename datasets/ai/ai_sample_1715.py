import nltk
import pandas as pd
import numpy as np
import re
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm

# import data
data = pd.read_csv('data.csv', sep='\t')

# clean data
corpus = [re.sub(r'[^\w\s]','',text.lower()) for text in data['text']]

# tokenize data
tokenizer = nltk.tokenize.WordPunctTokenizer()
tokenized_corpus = [tokenizer.tokenize(sent) for sent in corpus]

# create features
vectorizer = TfidfVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(corpus)

# split data into training and test sets
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train model
clf = svm.SVC()
clf.fit(X_train,y_train)

# test model
y_pred = clf.predict(X_test)

# print results
print(f'Model accuracy: {np.mean(y_test == y_pred)}')