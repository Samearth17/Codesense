import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
data=pd.read_csv("data.csv")

# Extract the features and labels
features = data.iloc[:, :-1].values
labels = data.iloc[:, -1].values

# splitting of training and testing data
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Feature extraction
vect = CountVectorizer()
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)

# Building and training the model
model = LogisticRegression()
model.fit(X_train_dtm,y_train)

# Predictions
predictions = model.predict(X_test_dtm)

# Evaluating the model
print('accuracy score:', accuracy_score(y_test, predictions)*100)