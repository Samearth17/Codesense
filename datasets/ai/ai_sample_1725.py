import nltk
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#Data processing
data = pd.read_csv('dataset.csv')
train, test = train_test_split(data,test_size=0.2,random_state=1)
X_train = train['Sentence'].values
y_train = train['Sentiment'].values
X_test = test['Sentence'].values
y_test = test['Sentiment'].values

#Create a CountVectorizer
count_vectorizer = CountVectorizer(stop_words='english')
count_train = count_vectorizer.fit_transform(X_train)
count_test = count_vectorizer.transform(X_test)

#Train the model
nb_classifier = MultinomialNB()
nb_classifier.fit(count_train,y_train)

#Evaluate the model
predictions = nb_classifier.predict(count_test)
print('Accuracy score: ', format(np.mean(predictions==y_test)))