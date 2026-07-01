import numpy as np
import tensorflow as tf

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(7, )),
        tf.keras.layers.Dense(1)
    ])

    model.compile(loss='mean_squared_error', 
                  optimizer='adam',
                  metrics=['accuracy'])

    return model
    
if __name__ == "__main__":
    model = create_model()

    input_data = np.array([[10, 10.4, 10.5, 10.6, 10.7, 10.9, 11]])
    predictions = model.predict(input_data)

    print(f"Predicted stock price for the next day is: {predictions[0][0]}")