class DecisionTreeClassifier:
    def __init__(self):
        self.tree = None
    
    def fit(self, X, y):
        # Create empty Decision Tree
        self.tree = {'feats': [], 'thresholds': [], 'left': None, 'right': None}

        # Find the best feature to split data
        bestFeature, bestThreshold = self.findBestSplit(X, y)

        # Split data into two subsets
        leftMask = X[:, bestFeature] < bestThreshold
        rightMask = ~leftMask

        # Add the feature and threshold to the tree
        self.tree['feats'].append(bestFeature)
        self.tree['thresholds'].append(bestThreshold)

        # Split data into subsets
        XLeft, yLeft = X[leftMask], y[leftMask]
        XRight, yRight = X[rightMask], y[rightMask]
        
        # Recursively build decision tree
        self.tree['left'] = self.fit(XLeft, yLeft)
        self.tree['right'] = self.fit(XRight, yRight)
        
        return self.tree
      
    def predict(self, X):
        pass