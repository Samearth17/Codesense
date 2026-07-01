import numpy as np

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Embedding
from keras.layers import GlobalAveragePooling1D

max_words = 1000

# load dataset 
(x_train, y_train), (x_test, y_test) = 
    keras.datasets.imdb.load_data(num_words=max_words)

# convert to one-hot
x_train = sequence.pad_sequences(x_train, maxlen=max_words)
x_test = sequence.pad_sequences(x_test, maxlen=max_words)

# define the model
model = Sequential()
model.add(Embedding(max_words, 32))
model.add(GlobalAveragePooling1D())
model.add(Dense(1, activation = 'sigmoid'))

# compile the model
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# fit the model
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=128)