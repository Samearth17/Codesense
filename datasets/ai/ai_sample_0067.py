import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

# Load data
data = pd.read_csv('data.csv')

# Select features
features = data[['home_team_goals', 'away_team_goals', 'home_team_possession', 'away_team_possession',
                 'home_team_shots', 'away_team_shots', 'home_team_yellow_cards', 'away_team_yellow_cards',
                 'home_team_red_cards', 'away_team_red_cards']]

# Select target
target = data['winner']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the model
gbm = GradientBoostingClassifier()
gbm.fit(X_train, y_train)

# Make predictions
y_pred = gbm.predict(X_test)

# Evaluate the model
score = gbm.score(X_test, y_test)
print(f'Model score: {score}')