import keras
from keras.models import Sequential
from keras.layers import Dense

#define the model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=50))
model.add(Dense(units=10, activation='softmax'))

#compile the model
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

#train the model
model.fit(x_train, y_train, epochs=5, batch_size=32)

#evaluate the model
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)