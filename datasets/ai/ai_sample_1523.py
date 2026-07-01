import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

# Load data
data = pd.read_csv('student_data.csv')
X = data.iloc[:,0:-1]
y = data.iloc[:, -1]

# Preprocssing
X = StandardScaler().fit_transform(X)

# Split train, test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train machine learning model 
knn_classifier = KNeighborsClassifier(n_neighbors=6)
knn_classifier.fit(X_train, y_train)

# Make predictions
y_pred = knn_classifier.predict(X_test)

# Evaluate performance
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))