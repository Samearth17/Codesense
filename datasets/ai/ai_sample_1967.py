import tensorflow as tf
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, Dropout, LSTM

# Step 1: Preprocess the data
input_data = [
  {'message': 'This is an important offer - act now!', 'label': 'spam'},
  {'message': 'You have been chosen to win a prize', 'label': 'spam'},
  {'message': 'To complete your order, please follow the link below', 'label': 'spam'},
  {'message': 'See the attached report for details', 'label': 'not_spam'},
  {'message': 'I will be away for the next few days', 'label': 'not_spam'}
]

# one-hot encoding
labels = [data['label'] for data in input_data]
labels_one_hot_encoded = [one_hot(label, 2) for label in labels]

# text encoding
messages = [data['message'] for data in input_data]
messages_encoded = [one_hot(message, 100) for message in messages]

# padding
messages_padded = pad_sequences(messages_encoded, maxlen=128, padding='pre')

labels_encoded = pad_sequences(labels_one_hot_encoded, maxlen=2, padding='post')

# creating the model
model = Sequential()
model.add(Embedding(input_dim=100, output_dim=128, input_length=messages_padded.shape[1]))

model.add(LSTM(128))
model.add(Dense(2, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x=messages_padded, y=labels_encoded, epochs=10, batch_size=32)