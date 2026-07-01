#import libraries 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
  
#import dataset 
data = load_iris() 
  
#divide the data into independent and dependent variables 
X = data.data 
y = data.target 
  
# Split the data into training and test set 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 
  
#Define the model 
model = RandomForestClassifier(n_estimators=100) 
  
#Train the model 
model.fit(X_train, y_train) 
  
# Test the model 
model.score(X_test, y_test)