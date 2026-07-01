# import libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

# read data
df = pd.read_csv('data.csv')

# set up dependent and independent variables
X = df['text']
y = df['sentiment']

# creating document term matrix
vectorizer = CountVectorizer() 
X_dtm = vectorizer.fit_transform(X).toarray() 

# split data into train and test set
X_train, X_test, y_train, y_test = train_test_split(X_dtm, y, test_size = 0.2, random_state = 0)

# train model
nb = BernoulliNB() 
nb.fit(X_train, y_train) 

# evaluate model
accuracy = nb.score(X_test, y_test) 

# predicting sentiment
text = 'I love it when the weather is good.'
data = vectorizer.transform([text]).toarray()
prediction = nb.predict(data)
print(prediction)
# Output: ['positive']