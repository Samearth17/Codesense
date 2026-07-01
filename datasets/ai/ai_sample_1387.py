import tensorflow as tf
from tensorflow.keras import layers

# Create the model
model = tf.keras.Sequential()
model.add(layers.Dense(50, activation='relu', input_dim=2))
model.add(layers.Dense(20, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
 
# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
 
# Fit the model
model.fit(X_train, y_train, epochs=20)

# Evaluate the model
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])