# Naive Bayes Classifier

import numpy as np
from sklearn.naive_bayes import MultinomialNB

# Sample data
# Each item is a string of text
X = ["I am spam", "Help me now", "You won the lottery", "Buy this product now", 
    "Don't miss this great offer", "Open an account with us", "Get rich quick",
    "This is not a scam", "Don't believe this offer", "Invest with us now"]

# Labels for the example data
# 1: Spam, 0: Ham
y = np.array([1,0,1,1,1,0,1,0,1,0])

# Create the classifier
clf = MultinomialNB()

# Train the classifier
clf.fit(X, y)

# Test the classifier
test_example = "Claim your prize now"
test_example_label = clf.predict([test_example])
print("Test example classified as:", test_example_label[0])