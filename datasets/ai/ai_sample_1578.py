import keras

# Load the FOML-200 dataset
data = keras.datasets.imdb

# Create training and test data
(X_train, y_train), (X_test, y_test) = data.load_data(num_words=88000)

# Create word to index lookup
word_index = data.get_word_index()
word_index = {k:(v+3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

# Convert review to sequence
X_train = keras.preprocessing.sequence.pad_sequences(X_train, value=word_index['<PAD>'], padding='post', maxlen=250)
X_test = keras.preprocessing.sequence.pad_sequences(X_test, value=word_index['<PAD>'], padding='post', maxlen=250)

# Create embedding layer from pre-trained Glove embeddings
embedding_matrix = np.zeros((88000, 100))
for word, i in word_index.items():
    if i >= 88000:
        continue
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector

# Create the model
model = keras.Sequential()
model.add(keras.layers.Embedding(88000, 100, weights=[embedding_matrix], input_length=250, trainable=False))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.GlobalMaxPooling1D())
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X_train, y_train, epochs=25, batch_size=128, validation_data=(X_test, y_test))