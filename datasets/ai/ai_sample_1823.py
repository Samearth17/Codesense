import keras
from keras.datasets import mnist
from keras.layers import Dense, Activation
from keras.models import Sequential

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# Initializing the model
model = Sequential()

# Input and hidden Layer
model.add(Dense(units=32, input_shape=(784, )))
model.add(Activation('relu'))

# Output Layer
model.add(Dense(units=10))
model.add(Activation('softmax'))

# Compiling the model
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

# Train the model
history = model.fit(x_train, 
                    y_train, 
                    epochs=25, 
                    batch_size=200, 
                    validation_data=(x_test ,y_test ))

# Evaluate the model
scores = model.evaluate(x_test, y_test)