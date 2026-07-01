import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Read data
data = pd.read_csv('arrhythmaiadata.csv')

# Select features and targets
X = data.drop('arrhythmia', axis=1)
y = data.arrhythmia

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy: %.2f' % (accuracy))