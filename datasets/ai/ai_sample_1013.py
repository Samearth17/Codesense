import cv2
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
 
#Creating the model
model = Sequential()
 
#Adding the first layer
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
 
#Adding the second layer
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
 
#Adding the third layer
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
 
#Flattening Layer
model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
 
#Output Layer
model.add(Dense(1))
model.add(Activation('sigmoid'))
 
#Compiling the model
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
#Train the model
model.fit_generator(training_set,
                         steps_per_epoch=1000,
                         epochs=25,
                         validation_data=test_set,
                         validation_steps=200)
 
#Prediction
def predict(path):
 img_array = cv2.imread(path)
 img_array = cv2.resize(img_array, (64, 64))
 img_array = np.array(img_array).reshape(-1, 64, 64, 3)
 predicted_array = model.predict(img_array)
 if predicted_array[0][0] == 1:
  print('Face Detected')
 else:
  print('Face not detected')