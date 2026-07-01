import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Load the data
data = pd.read_csv("data.csv")

# Vectorize the text
cv = CountVectorizer()
X = cv.fit_transform(data["text"])

# Convert target labels to numerical values
y = np.array([1 if label == "category1" else 2 if label == "category2" else 3 for label in data["category"]])

# Split into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Train the model
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Test the model
y_pred = nb.predict(X_test)

# Print out the results
print(classification_report(y_test, y_pred))