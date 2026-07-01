from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Read in sample data
df = pd.read_csv('sample_dataset.csv')

# Split the data into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(df[['input']], df[['output']], test_size=0.2)

# Create the model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Use the model to predict output for the test data
y_pred = model.predict(X_test)

# Evaluate the model
score = model.score(X_test, y_test)
print("Model accuracy:",score)