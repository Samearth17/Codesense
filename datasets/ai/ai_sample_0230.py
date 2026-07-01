import numpy as np
import pandas as pd

def bitcoinPricePrediction(data):
# convert data to numpy array
data = np.array(data)

# define the model
model = keras.Sequential([
keras.layers.Dense(64, activation='relu'),
keras.layers.Dense(64, activation='relu'),
keras.layers.Dense(64, activation='relu'),
keras.layers.Dense(1)])

# compile and train the model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(data, epochs=50, verbose=1)

# predict the tomorrow's bitcoin price
prediction = model.predict(data)[0][0]

return prediction