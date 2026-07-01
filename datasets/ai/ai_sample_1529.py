import tensorflow as tf
import pandas as pd

# Read the data
df = pd.read_csv('data.csv', index_col=False)

# Prepare the input data
X = df[['height', 'weight']]
y = df['label'].astype('int32')

# Build the model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(2, input_shape=(2,), activation='softmax'))
model.compile(optimizer=tf.keras.optimizers.Adam(0.05),
 loss=tf.keras.losses.SparseCategoricalCrossentropy(),
 metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=100, batch_size=32)