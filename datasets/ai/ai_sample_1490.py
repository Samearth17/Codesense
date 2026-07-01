# Import the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load the dataset
data = pd.read_csv('CustomerChurn.csv')

# Split the dataset into training and testing set.
X = data.drop('Churn', axis=1)
y = data['Churn']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.20, random_state = 0)

# Apply feature scaling 
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train the model 
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Test the model
y_pred = classifier.predict(X_test)