import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.naive_bayes import MultinomialNB

# Load the data
data = pd.read_csv('movie_reviews.csv')

# Extract the reviews and the labels
reviews = data.text.tolist()
labels = data.label.tolist()

# Transform the reviews to a numerical feature vector
cv = CountVectorizer(binary=True)
X = cv.fit_transform(reviews)

# Initialize the classifier
mnb = MultinomialNB()

# Train the classifier
mnb.fit(X, labels)

# Make predictions
preds = mnb.predict(X)

# Print the accuracy
print('Accuracy:', mnb.score(X, labels))