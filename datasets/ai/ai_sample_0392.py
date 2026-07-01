# Load the required libraries
import numpy as np
import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# Load the training dataset
sentences = ['This is a good sentiment', 'This is a bad sentiment']
labels = [1, 0]

# Create the tokenizer
tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(sentences)

# Encode  the sentences
encoded_sentences = tokenizer.texts_to_sequences(sentences)
padded_sentences = pad_sequences(encoded_sentences, maxlen=10)

# Build the model
model = Sequential()
model.add(Embedding(input_dim=1000, output_dim=32, input_length=10))
model.add(LSTM(32))
model.add(Dense(1, activation='sigmoid'))

# Compile and fit the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(padded_sentences, labels, epochs=10) 

# Evaluate the model
scores = model.evaluate(padded_sentences, labels) 
print("Accuracy: %.2f%%" % (scores[1]*100))