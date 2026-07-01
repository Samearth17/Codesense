import tensorflow as tf
from tensorflow.keras.datasets import mnist

# Get train and test data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape data
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normalize data
x_train /= 255
x_test /= 255

# Build model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
 metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10)

# Evaluate model
accuracy = model.evaluate(x_test, y_test)[1]
print('Accuracy of model:', accuracy)