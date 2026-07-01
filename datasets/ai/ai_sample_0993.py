import numpy as np

from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM

corpus = ["It is a wonderful day today",
"the weather is extremely bad today"]
labels = np.array([1, 0])

# tokenize corpus
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
X = tokenizer.texts_to_sequences(corpus)
X = sequence.pad_sequences(X, maxlen=10)

# build model
model = Sequential()
model.add(Embedding(len(tokenizer.word_index)+1, 100, input_length=10))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# train the model
model.fit(X, labels, batch_size=1, epochs=20)

# test the model
test_sentence = "today the weather is horrible"
test_tokenized = tokenizer.texts_to_sequences([test_sentence])
test_tokenized = sequence.pad_sequences(test_tokenized, maxlen=10)
predict = model.predict(test_tokenized)
print(predict[0])