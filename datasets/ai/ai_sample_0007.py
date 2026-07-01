import keras

# Input layer
input_layer = keras.layers.Input(shape=(784,))

# Hidden layer
hidden_layer = keras.layers.Dense(128, 
                activation='relu')(input_layer)

# Output layer
output_layer = keras.layers.Dense(10, 
                activation='softmax')(hidden_layer)

# Model
model = keras.Model(inputs=input_layer, outputs=output_layer)

# Compile model
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])