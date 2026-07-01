import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import precision_score

# Load the dataset
df = pd.read_csv("spam.csv", encoding='iso-8859-1')
# Load label and data
X = df['EmailText']
y = df['Label']

# Split data into train-test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Create bag of words model
count_vectorizer = CountVectorizer()
X_train_counts = count_vectorizer.fit_transform(X_train)

# Train the model
clf = svm.SVC(kernel='linear')
clf.fit(X_train_counts, y_train)

# Test the model
X_test_counts = count_vectorizer.transform(X_test)
predictions = clf.predict(X_test_counts)
score = precision_score(y_test, predictions, average='binary')

print('Precision score of the model:', score)