import pandas as pd 
from sklearn import tree 
data = pd.read_csv('customer_data.csv') 
feature_names = ['Age','Gender','Occupation','Type','City','Member since','Months on Site'] 
target_names = ['No','Yes'] 
X = data[feature_names].values 
y = data['Purchase'].values 

# Create decision tree classifier 
clf = tree.DecisionTreeClassifier() 

# Train the decision tree classifier 
clf = clf.fit(X, y) 

# Visualize the decision tree 
dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=feature_names,  
                     class_names=target_names,  
                     filled=True, rounded=True,  
                     special_characters=True)  
import graphviz 
graph = graphviz.Source(dot_data)  
graph