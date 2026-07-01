# Load libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load dataset
data = pd.read_csv('basketball_players.csv')

# Split into features and target
X = data.drop(columns=['position'])
y = data['position'] 

# Split into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Fit Naive Bayes classifier
model = GaussianNB()
model.fit(X_train, y_train)