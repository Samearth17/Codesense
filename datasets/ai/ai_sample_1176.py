from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

# Import the dataset
from keras.datasets import mnist
# Load the dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Reshaping the data
X_train = X_train.reshape(-1, 784)
X_test = X_test.reshape(-1, 784)
# Normalizing the data
X_train = X_train/255
X_test = X_test/255
# Converting the target variables into binary categories
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Building the model
model = Sequential([
 Dense(64, activation='relu', input_shape=(784,)),
 Dense(64, activation='relu'),
 Dense(10, activation='softmax')
])

# Compiling the model
model.compile(
 optimizer='adam',
 loss='categorical_crossentropy',
 metrics=['accuracy']
)

# Training the model
model.fit(
 X_train, y_train,
 batch_size=128,
 epochs=5,
 validation_data=(X_test, y_test)
)