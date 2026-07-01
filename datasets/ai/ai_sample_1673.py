import numpy as np
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense

# Data
x_data = np.array([1,2,3,4,5,6,7,8,9,10])
labels = ['apple', 'apple', 'orange', 'orange', 'pear', 'pear', 'apple', 'orange', 'pear', 'apple']

# One-hot encoding
y_data = to_categorical([labels.index(label) for label in labels])

# Model building
model = Sequential()
model.add(Dense(units=3, activation='softmax', input_dim=1))
model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
model.fit(x_data, y_data, batch_size=10, epochs=100, verbose=2)

# Predictions
predictions = model.predict(x_data)

# Print predictions
for (x, prediction) in zip(x_data, predictions):
 print('x={0} -- Predicted class={1}'.format(x, np.argmax(prediction)))