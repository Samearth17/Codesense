from tensorflow.keras.layers import Input, Dense, Embedding, GRU
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model

# Create inputs
inputs1 = Input(shape=(20,))
x1 = Embedding(1000, 64)(inputs1)
x1 = GRU(128)(x1)

# Create outputs
y1 = Dense(1000, activation='softmax')(x1)

# Create model
model = Model(inputs=[inputs1], outputs=[y1])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit([inputs], [outputs],  epochs=10, batch_size=32)

# Generate the response to the sample utterance
query = "What time is it?"
prediction = model.predict(query)

print(prediction)