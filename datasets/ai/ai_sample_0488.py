#import necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.svm import SVC

#load the dataset
dataset = datasets.load_iris()

#split the data into train and test datasets
x_train, x_test, y_train, y_test = train_test_split(dataset.data, dataset.target, 
                                                    test_size=0.2, random_state=42)

#build the model
svc = SVC()
svc.fit(x_train, y_train)

#predict for test data
y_pred = svc.predict(x_test)

#evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print('accuracy: ', accuracy)

print(classification_report(y_test, y_pred))