import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier 

# Define the hyperparameters to optimize
param_grid={
 'n_estimators': np.arange(2, 30, 2),  
 'max_depth': np.arange(2, 12, 2),  
 'min_samples_leaf': np.arange(1, 10, 2)
}

# Create GridSearchCV model object with the hyperparameters
model = GridSearchCV(RandomForestClassifier(), param_grid, verbose=2, cv=3) 

# Fit the model to the data
model.fit(X, y) 

# Print out the best estimator
print(model.best_estimator_)