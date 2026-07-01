import pandas as pd

#importing the dataset 
dataset = pd.read_csv('data.csv')

#splitting the dataset into features and labels 
X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, 3].values

#importing DecisionTreeClassifier 
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion = 'entropy')

#fitting the classifier to the dataset
classifier.fit(X,y)