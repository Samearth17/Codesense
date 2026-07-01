import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

# Data Preprocessing
# Read dataset into pandas dataframe
df = pd.read_csv("data.csv")

# Extract relevant features
features = df.iloc[:, :-1].values
labels = df.iloc[: , -1].values

# Split dataset into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state= 0)

# Train and Test data feature engineering
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
X_test = cv.transform(X_test)

# Train the Naive Bayes Classifier Model
classifier = BernoulliNB()
classifier.fit(X_train, y_train)

# Test the accuracy of the model
y_pred = classifier.predict(X_test)
accuracy = np.mean(y_pred == y_test)

# Print the accuracy of the model
print("Accuracy: ", accuracy * 100, "%")