import tensorflow as tf
import  nltk
from tensorflow.keras.layers import Dense, Input, Embedding, LSTM
from tensorflow.keras.models import Model

inputs = Input(shape=(None,)) # shape is the length of the sentences
embedding = Embedding(input_dim=1000, output_dim=32)(inputs)

lstm_1 = LSTM(50, return_state=True,name="LSTM_1")
outputs, h, c = lstm_1(embedding) # h and c are hidden states

dense_1 = Dense(15, activation='relu')(outputs)

dense_2 = Dense(1)(dense_1)

model = Model(inputs=inputs, outputs=dense_2)

model.summary()

nltk.download('punkt')

sentences = [['Hi', 'How are you?'], ['I am good', 'That is awesome'], ['Thank you']]

# Tokenize Sentences
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

# Generate Vocabulary and Embedding
vocab = set([word for sentence in sentences for word in sentence])

word_2_idx = {word: idx for idx, word in enumerate(vocab)}

train_data = [[word_2_idx[word] for word in sentence] for sentence in tokenized_sentences]

model.compile(optimizer='adam', loss='binary_crossentropy', 
              metrics=['accuracy'])

model.fit(train_data, labels,
         epochs=50,
         batch_size=32)