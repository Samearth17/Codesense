#importing necessary packages
import tensorflow as tf
import pandas as pd
import numpy as np

#loading and pre-processing the data
data = pd.read_csv(data.csv)
data = np.array(data)

#building the model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(1000, 64))
model.add(tf.keras.layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

#compiling the model
model.compile(loss='binary_crossentropy',
 optimizer=tf.keras.optimizers.Adam(),
 metrics=['accuracy'])

#training the model
model.fit(data[:,1], data[:,0], batch_size=128, epochs=10, validation_split=0.1)

#testing the model
text = input("User: ") 
prediction = model.predict(np.array([text]))

#responding to the user
if prediction > 0.5:
 print("Chatbot: The temperature outside is " + prediction + " degrees")
else:
 print("Chatbot: Sorry, I don't know.")