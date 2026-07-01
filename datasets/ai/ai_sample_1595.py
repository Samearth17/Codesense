import keras 
from keras.datasets import mnist 
from keras.models import Model 
from keras.layers import Input, Dense, Dropout, Flatten 
from keras.layers import Conv2D, MaxPooling2D 

def create_model():
    # Define the input layer
    inputs = Input(shape=(28, 28, 1))
    
    # 1st convolutional layer
    conv = Conv2D(64, kernel_size=3, activation='relu')(inputs) 
    # 2nd convolutional layer 
    conv = Conv2D(32, kernel_size=3, activation='relu')(conv) 
    # Max pooling layer 
    pool = MaxPooling2D(pool_size=(2, 2))(conv) 
    # Dropout layer 
    drop = Dropout(0.25)(pool) 
    # Flatten layer 
    flatten = Flatten()(drop) 
    # Dense layer 
    dense = Dense(128, activation='relu')(flatten) 
    # Output layer 
    outputs = Dense(10, activation='softmax')(dense) 
    
    # Create a model and compile it 
    model = Model(inputs, outputs) 
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
    
    return model