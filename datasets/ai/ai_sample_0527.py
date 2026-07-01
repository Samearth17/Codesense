import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Create a data frame from the input data
df = pd.read_csv("emails.csv")
# Extract features and outputs
X = df['content'].values
y = df['label'].values
# Split the dataset into train & test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
# Count vectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)
# Create & fit the model
model = MultinomialNB()
model.fit(X_train, y_train)
# Test the model
score = model.score(X_test, y_test)
print(score)