import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential 
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D 
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint

# Specify image dimensions 
img_width, img_height = 150, 150

# # Create the model 
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(img_width, img_height, 3))) 
model.add(MaxPooling2D(pool_size=(2,2))) 
model.add(Conv2D(64, kernel_size=(3, 3)))
model.add(MaxPooling2D(pool_size=(2,2))) 
model.add(Flatten())
model.add(Dense(128, activation='relu')) 
model.add(Dense(7, activation='softmax'))

# Compile the model 
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(), metrics=['accuracy'])

# Prepare the data
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255) 

train_generator = train_datagen.flow_from_directory('train', target_size=(img_width, img_height), batch_size=16, class_mode='categorical')
validation_generator = test_datagen.flow_from_directory('test',target_size=(img_width, img_height), batch_size=16,class_mode='categorical')

# Train the model 
checkpoint = ModelCheckpoint(filepath='best-model.h5',save_best_only=True,verbose=1)
model.fit_generator(train_generator,steps_per_epoch=2000//16,epochs=50,validation_data=validation_generator,validation_steps=1000//16,callbacks=[checkpoint])

# Evaluate the model
scores = model.evaluate_generator(validation_generator, steps=1000//16)
print("Accuracy = ", scores[1])

# Make predictions
y_pred = model.predict_generator(validation_generator, steps=1000//16)

# Print predictions
for i in range(len(y_pred)): 
 print("Prediction: ", np.argmax(y_pred[i]), "Actual: ", validation_generator.labels[i])
print("Done!")