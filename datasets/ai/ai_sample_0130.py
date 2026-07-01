import numpy as np
import keras 
from keras.layers import Dense
from keras.models import Sequential

# Build model
model = Sequential()
model.add(Dense(64, input_dim = 2, activation = 'relu'))
model.add(Dense( 1))

# Compile the model
model.compile(loss = 'mean_squared_error',
              optimizer = 'adam')

# Obtain some data - age (years), education level (high school, college, university)
x_train = np.array([[25, 0], [30, 0], [35, 0], 
		    [40, 0], [45, 1], [45, 2],
		    [50, 1], [50, 2], [55, 1],
		    [55, 2], [50, 3], [60, 3]])

# Labels - annual income
y_train = [15000, 20000, 25000, 30000,
           40000, 45000, 50000, 60000, 
	   65000, 70000, 80000, 90000]

# Fit the model
model.fit(x_train, y_train, epochs = 150, batch_size = 2)

# Calculate the predicted annual income
age = 50
education = 3
annualIncome = model.predict(np.array([[age, education]]))
print(annualIncome)
# output: [[80000]]