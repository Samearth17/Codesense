#import libraries
import keras
from keras import models
from keras.layers import Dense, Dropout, Embedding, Conv1D, GlobalMaxPooling1D, Flatten
import numpy as np

#Specify parameters
vocab_size = 50000
embedding_dim = 200
maxlen = 500
batch_size = 64

#define model
model = models.Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=maxlen))
model.add(Conv1D(256, 3, activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

#Fit model
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=5,
          validation_data=(x_val, y_val))