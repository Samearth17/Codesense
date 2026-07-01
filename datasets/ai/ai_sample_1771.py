import tensorflow as tf

# Create example deep learning model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv2D(32, (3,3), input_shape=(300, 300, 3)))
model.add(tf.keras.layers.MaxPool2D(2, 2))
model.add(tf.keras.layers.Conv2D(64, (3,3), input_shape=(150, 150, 3)))
model.add(tf.keras.layers.MaxPool2D(2, 2))

# Optimize model for size
model.add(tf.keras.layers.Conv2D(32, (3,3), input_shape=(50, 50, 3), activation='relu'))
model.add(tf.keras.layers.MaxPool2D(2, 2))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Conv2D(64, (3,3), input_shape=(25, 25, 3),activation="relu"))
model.add(tf.keras.layers.MaxPool2D(2, 2))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Flatten())