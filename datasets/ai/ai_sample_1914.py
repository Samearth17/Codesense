import pandas as pd

# Load dataset
speech_data = pd.read_csv("speech_data.csv")

# Preprocessing
X_features = speech_data["speech_text"]
Y_target = speech_data["student_id"]

# Split into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X_features, Y_target, test_size = 0.2, random_state = 0)

# Generate Model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, Y_train)

# Evaluate Model
accuracy = classifier.score(X_test, Y_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(accuracy))