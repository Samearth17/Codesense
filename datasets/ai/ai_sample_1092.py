import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training and testing data
X_train = np.array(["This is a sample sentence.",
                    "Another sample sentence.",
                    "Yet another sentence for classification."])
y_train = np.array([0, 0, 1])
X_test = np.array(["Classify this sentence.",
                   "Two sentences in one."])

# Create a vectorizer and fit it to the training data
vectorizer = CountVectorizer()
vectorizer.fit(X_train)

# Transform the training data and test data into a vector
X_train_vec = vectorizer.transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Create a MultinomialNB model and fit it to the vectorized data
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Make predictions with the model
predictions = model.predict(X_test_vec)
print(predictions)  # Output: [1 0]