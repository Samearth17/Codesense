import tensorflow as tf
import pandas as pd
from tensorflow.keras.layers import Input, Embedding, Dense, Flatten
from tensorflow.keras.models import Model

# Preprocess data
customers = pd.read_csv('customers.csv', usecols=['customer_id', 'name', 'purchase_history'])
customers['purchase_history'] = customers['purchase_history'].str.split(';')

# Create model
inputs = Input(shape=(1,))
emb_layer = Embedding(input_dim=customers.shape[0], output_dim=5)(inputs)
flatten = Flatten()(emb_layer)
dense_1 = Dense(10, activation='relu')(flatten)
outputs = Dense(1, activation='sigmoid')(dense_1)

model = Model(inputs=inputs, outputs=outputs)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(x_train, y_train, 
          epochs=50,
          batch_size=32, 
          validation_data=(x_test, y_test))

# Deploy model in web service
api = tf.keras.models.load_model('purchase_prediction.h5')