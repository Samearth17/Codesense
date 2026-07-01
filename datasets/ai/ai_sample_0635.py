# Feature selection
from sklearn.feature_selection import RFE

# Use recursive feature elimination to select the most 
# important features
rfe = RFE(estimator = model, step = 1)
fit = rfe.fit(X, y)

# Parameter tuning using grid search
from sklearn.model_selection import GridSearchCV

# Create grid search object
parms = {'C': [0.1, 1, 10, 100, 1000],  
         'gamma': [1, 0.1, 0.01, 0.001, 0.0001], 
         'kernel': ['rbf']} 
grid = GridSearchCV(estimator = model, param_grid = parms, scoring = 'accuracy', cv = 5)

# Fit grid search to the data
grid.fit(X, y)

# Regularization and model selection
from sklearn.linear_model import Ridge, Lasso

# Ridge regression with parameter alpha = 0.01
model = Ridge(alpha = 0.01)
model.fit(X, y)