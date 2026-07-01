import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# create the dataset
x_train = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y_train = np.array([[3], [5], [7], [9], [11], [14], [17], [22], [25], [27]])

# create and fit the polynomial regression model
pr = LinearRegression()
quadratic = PolynomialFeatures(degree=2)
x_train_quad = quadratic.fit_transform(x_train)

# fit the model
pr.fit(x_train_quad, y_train)

# predict the output for the values in x
y_pred = pr.predict(x_train_quad)

# visualize the input and output
plt.scatter(x_train, y_train, label='Training Data')
plt.plot(x_train, y_pred, label='Polynomial Regression', color='red')
plt.legend()
plt.show()