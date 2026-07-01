import tensorflow as tf
from tensorflow import keras

# Split data into train and test sets
train_X, train_y, test_X, test_y = [], [], [], []
for x, y in data:
 train_X.append(x)
 train_y.append(y)

# Create tokenizer
tokenizer = keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(train_X)

# Create model
model = keras.models.Sequential([
keras.layers.Dense(64, input_shape=[None,]),
 keras.layers.Dense(64, activation='relu'),
 keras.layers.Dense(1, activation='sigmoid')
])

# Compile model
model.compile(
 optimizer='adam',
 loss='binary_crossentropy',
 metrics=['accuracy']
)

# Train
train_X_vector = tokenizer.texts_to_matrix(train_X)
model.fit(train_X_vector, train_y, epochs=10, validation_split=0.2)