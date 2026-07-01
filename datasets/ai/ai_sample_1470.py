#importing the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

#loading the dataset
df = pd.read_csv('wine_data.csv')

#defining independent and dependent variables
X = df.iloc[:,:11]
y = df.iloc[:,11]

#splitting the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#scaling the data
scaler = StandardScaler()
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.fit_transform(X_test)

#creating and fitting the model
model = LogisticRegression().fit(scaled_X_train, y_train)

#prediciting the test data
y_pred = model.predict(scaled_X_test)

#calculating the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)