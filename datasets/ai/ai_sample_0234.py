from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample dataset
docs = [
 "The sky is blue.",
 "Violets are red.",
 "I love programming.",
 "JavaScript is fun."
 "Python is great!"
]

labels = [0, 0, 1, 1, 1]

# Create the vectorizer
vectorizer = CountVectorizer()

# Vectorize the documents
X = vectorizer.fit_transform(docs).toarray()

# Create a Naive Bayes model
model = MultinomialNB()

# Fit the model to the dataset
model.fit(X, labels)

# Make a prediction
prediction = model.predict([X[3]])

# Print the prediction
print(prediction) # prints [1]