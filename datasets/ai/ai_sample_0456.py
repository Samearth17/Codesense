import numpy as np
from tensorflow.keras.callbacks import TensorBoard

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Reshape and normalize the data
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the model
model = tf.keras.Sequential([
 tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
 tf.keras.layers.MaxPooling2D(),
 tf.keras.layers.Flatten(),
 tf.keras.layers.Dense(128, activation='relu'),
 tf.keras.layers.Dense(10, activation='softmax')
])

# Compile and train the model
model.compile(
 optimizer='adam', 
 loss='sparse_categorical_crossentropy',
 metrics=['accuracy']
)

model.fit(x_train, y_train, epochs=5, callbacks=[TensorBoard('logs')])

# Evaluate the model
model.evaluate(x_test, y_test)