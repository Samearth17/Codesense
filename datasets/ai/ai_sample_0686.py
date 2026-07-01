import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import precision_recall_curve

# Array of classification labels
y = np.array([1, 0, 1, 0, 1, 0, 0, 0, 1, 1]) 

# Array of classification scores
scores = np.array([0.8, 0.6, 0.75, 0.9, 0.7, 0.3, 0.2, 0.1, 0.85, 0.5])

# Get precision and recall value
precision, recall, _ = precision_recall_curve(y, scores)

# plot precision and recall curve
plt.plot(recall, precision)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.show()