import numpy as np #importing the libraries 
from sklearn.neural_network import MLPClassifier #importing the neural network classifier

#defining the input values
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

#Creating the model
model = MLPClassifier(hidden_layer_sizes = (2,2)) #creating the neural network with two hidden layers.
model.fit(X,y)

#Testing the model with a new input
test_data = np.array([[1,1]])
prediction = model.predict(test_data) 
print("The model predicts the output as:",prediction[0])