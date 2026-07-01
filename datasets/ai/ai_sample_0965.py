import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Input data
data = np.array([
[0, 'State-gov', 77516, 'Bachelors', 13, 'Never-married', 'Adm-clerical', 'Not-in-family', 'White', 'Male', 2174, 0, 40, 'United-States', '<=50K'],
[1, 'Private', 83311, 'Bachelors', 13, 'Married-civ-spouse', 'Exec-managerial', 'Husband', 'White', 'Male', 0, 0, 13, 'United-States', '<=50K'],
[2, 'Private', 215646, 'HS-grad', 9, 'Divorced', 'Handlers-cleaners', 'Not-in-family', 'White', 'Male', 0, 0, 40, 'United-States', '<=50K']
])

# Features
X = data[:, :14]
y = data[:, 14]

# Fit decision tree
clf = DecisionTreeClassifier(random_state=0, max_depth=2)
clf = clf.fit(X, y)