import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

# Convert text into numerical features
def get_features(text):
 feature_vector = []
 words = text.split(' ')
 for word in words:
 if word == 'happy':
 feature_vector.append(1)
 else:
 feature_vector.append(0)
 return np.array(feature_vector)
 
# Define model
model = Sequential([
 Dense(3, input_shape=(1,), activation='relu'),
 Dense(1, activation='sigmoid')
])

# Train model
X = get_features("I'm feeling very happy today!")
y = np.array([1])

model.compile(loss='binary_crossentropy', optimizer='adam',
 metrics=['accuracy'])
model.fit(X, y, epochs=100, batch_size=1)

# Save model
model.save('sentiment_detection.h5')