from sklearn.tree import DecisionTreeClassifier

# Load the dataset
X, y = dataset

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# Train Decision Tree classifier
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# Make predictions 
pred = clf.predict(X_test)

# Evaluate accuracy 
acc = accuracy_score(y_test, pred)
print('Accuracy: {:.2f}%'.format(acc*100))