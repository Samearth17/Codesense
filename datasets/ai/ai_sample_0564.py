# Import Libraries
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load data
X_train, X_test, y_train, y_test = load_data()

# Create a Machine Learning Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(solver='lbfgs', random_state=42))
])

# Fit the pipeline to the training data
pipeline.fit(X_train, y_train)

# Evaluate the pipeline on the test data
predicted = pipeline.predict(X_test)
print('Test Accuracy:', accuracy_score(predicted, y_test))