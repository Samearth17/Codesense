import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

# define training data
x = np.array([i for i in range(len(stock_prices))]).reshape(-1,1)
y = np.array(stock_prices)

# create and train model 
model = LinearRegression()
model.fit(x, y)

# make predictions 
y_pred = model.predict(x)

# plot results
plt.plot(x, y, 'o-')
plt.plot(x, y_pred, 'x-')
plt.title('Stock Prices with Linear Regression Model')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()