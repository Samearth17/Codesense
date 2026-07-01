# Imports 
import numpy as np 
import pandas as pd 
import tensorflow as tf

# Data 
data = pd.DataFrame(columns=['string'])
data = data.append({'string':'3aF5yD'}, ignore_index=True)

# Neural Network Architecture 
model = tf.keras.models.Sequential([
 tf.keras.layers.Embedding(input_dim=len(data.columns), output_dim=1, input_length=len(data.columns)),
 tf.keras.layers.LSTM(256, return_sequences=True),
 tf.keras.layers.Dense(32),
 tf.keras.layers.Dense(len(data), activation='softmax')
])

# Optimizer
model.compile(optimizer='adam', loss='mse')

# Train 
model.fit(data.values, epochs=10)

# Prediction
predictions = model.predict(data.values)
print(predictions)