import pandas as pd
from sklearn.model_selection import train_test_split

# Read the dataset
df = pd.read_csv('data.csv')

# Define the features and labels
X = df[['Gender', 'Age', 'Married', 'Salary']]
y = df['Outcome']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create the logistic regression model
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Make predictions
y_pred = logreg.predict(X_test)