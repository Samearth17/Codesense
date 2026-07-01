import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the dataset
dataset = pd.read_csv('stock_data.csv')

# Exploratory data analysis
dataset.describe()

sns.heatmap(dataset.corr(), annot=True)

# Create feature and target variables
X = dataset.iloc[:, 1:-1]
y = dataset.iloc[:, -1]

# Split the data into train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=0)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Test the model
y_pred = regressor.predict(X_test)

# Evaluate the model
from sklearn.metrics import r2_score
r2_score(y_test, y_pred)