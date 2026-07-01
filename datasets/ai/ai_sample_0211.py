# import libraries 
from keras.models import Sequential 
from keras.layers import Dense, Dropout 
import numpy 

# load the dataset 
dataset = numpy.loadtxt("mnist.csv", delimiter=",") 

# split into input (X) and output (Y) variables 
X = dataset[:,0:784] 
Y = dataset[:,784] 

# Create model
model = Sequential() 
model.add(Dense(784, input_dim=784, activation='relu'))
model.add(Dense(256, activation='relu')) 
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile model 
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 

# Fit the model 
model.fit(X, Y, epochs=10, batch_size=128, verbose=2)

# Evaluate the model 
scores = model.evaluate(X, Y) 
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))