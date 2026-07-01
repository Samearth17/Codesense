# Importing necessary libraries 
import numpy as np 
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

# Defining the function which takes the classifier object and optimizes it
def optimize_model(classifier, parameters):
    # Create a GridSearchCV object, which will use 5-fold cross validation 
    clf = GridSearchCV(classifier, parameters, scoring = 'accuracy', cv = 5)

    # Fit the model on the training data 
    clf.fit(X_train, y_train)

    # Predict the values on the test dataset
    y_pred = clf.predict(X_test)

    # Calculate the accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    
    # Print the accuracy
    print('Accuracy: {:.2f}%'.format(accuracy*100)) 

    # Return the best parameters and the classifier
    return clf.best_params_, clf