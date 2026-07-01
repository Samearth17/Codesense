import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# list of features and labels
features = np.array([[110000, 'Petrol', 'Manual', 1990, 30, 3000]])
labels = np.array([[1]])

# perform data preprocessing
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# create the model
model = KNeighborsClassifier()
model.fit(X_train_scaled, y_train)

# predict sales price
predicted_price = model.predict([X_test_scaled[0]])

print("Predicted sale price:", predicted_price[0])