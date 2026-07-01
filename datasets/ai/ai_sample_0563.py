import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load the dataset
reviews = pd.read_csv('reviews.csv')

# Create the feature matrix
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews.text)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, reviews.sentiment, test_size=0.25, random_state=1)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))