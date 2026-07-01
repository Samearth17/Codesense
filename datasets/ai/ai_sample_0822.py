#import packages
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the data from the 'spam' emails dataset
emails_data = pd.read_csv("emails.csv")

# Split the data into features and labels
X = emails_data.drop("label", axis=1)
y = emails_data["label"]

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Create the Multinomial Naive Bayes model
mnb = MultinomialNB()

# Train the model
mnb.fit(X_train, y_train)

# Make predictions
predictions = mnb.predict(X_test)

# Evaluate the accuracy of the model
print("Accuracy:", accuracy_score(y_test, predictions))