import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout

def create_spam_classifier():
 model = Sequential()
 model.add(Dense(128, activation='relu', input_shape=(20,)))
 model.add(Dropout(0.5))
 model.add(Dense(1, activation='sigmoid'))
 
 model.compile(
 optimizer='adam',
 loss='binary_crossentropy',
 metrics=['accuracy']
 )

 return model

if __name__ == "__main__":
 model = create_spam_classifier()