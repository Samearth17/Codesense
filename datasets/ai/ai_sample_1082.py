import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble  import RandomForestClassifier

# read in the data
df = pd.read_csv('loan_data.csv')

# split features and target
X = df.drop(columns='default').values
y = df['default'].values

# split dataset into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# build the model
model = RandomForestClassifier(n_estimators=500)
model.fit(X_train, y_train)

# predict
y_pred = model.predict(X_test)

# calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print('Model accuracy is: ', accuracy)