import tensorflow as tf 
from tensorflow import keras 

# create a Neural Network
model = keras.Sequential([ 
    keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(6,)), 
    keras.layers.Dense(64, activation=tf.nn.relu), 
    keras.layers.Dense(1) 
]) 
  
# compile the model 
model.compile(optimizer = 'rmsprop', 
              loss = keras.losses.MeanSquaredError(), 
              metrics=['accuracy']) 
              
# train the model
model.fit(X_train, y_train, epochs=40) 

# test the model 
test_loss, test_acc = model.evaluate(X_test, y_test) 

print('Test accuracy:', test_acc)