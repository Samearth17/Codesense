# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Construct feature and label data
# Feature (independent variable): days of the week
features = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
# Label (dependent vaiable): number of riders
labels = [[10, 15, 20, 25, 35, 50], [12, 18, 15, 24, 40, 57]]
# Reformat data as arrays
X = np.array(features)
y = np.array(labels)
# Split train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create model
model = LinearRegression()
# Train model
model.fit(X_train, y_train)
# Make predictions
y_pred = model.predict(X_test)
# Evaluate model
score = model.score(X_test, y_test)
print(f'Model score: {score}')