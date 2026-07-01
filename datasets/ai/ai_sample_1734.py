from sklearn import linear_model
from sklearn.model_selection import train_test_split

#load the data
X = height
y = age

#split it into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#train a linear regression model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)

#predict the age based on height
y_pred = model.predict(X_test)