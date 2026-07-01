import tensorflow as tf

# Create an input layer with two input features
inputs = tf.keras.Input(shape=(2,))

# Add a dense layer with three neurons
x = tf.keras.layers.Dense(3, activation='sigmoid')(inputs)

# Add a dense layer with three neurons
outputs = tf.keras.layers.Dense(3, activation='softmax')(x)

# Create the model
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Compile
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])