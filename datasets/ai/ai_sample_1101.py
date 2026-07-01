# import libraries
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 

# read dataset
cancer_data = pd.read_csv("cancer_data.csv")

# split into train and test sets
x_train, x_test, y_train, y_test = train_test_split(cancer_data.iloc[:,:-1], cancer_data.iloc[:,-1], test_size=0.25, random_state=0)

# create the model 
lr_model = LogisticRegression() 
lr_model.fit(x_train,y_train)

# accuracy
accuracy = lr_model.score(x_test,y_test)
print(accuracy)