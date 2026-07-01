# Import the necessary packages
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split

# Create the neural network
def build_model(input_dim):
    model = Sequential()
    model.add(Dense(64,input_dim=input_dim, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(2, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.001),
    metrics=['accuracy'])
    return model

# Load and prepare the data
X = np.load("x_data.npy")
y = np.load("y_data.npy")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the model and train it
input_dim = X_train.shape[1]
model = KerasClassifier(build_fn=lambda: build_model(input_dim))
model.fit(X_train, y_train, epochs=22, batch_size=32, verbose=1)

# Evaluate the model accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy: ", accuracy)
##

6. Instruction: Create a react app for a small business website. The app should include an About Us page, a Contact Us page, and pages for each of the services offered by the business.

6. Input:
Not applicable

6. Output:
import React from 'react';
import {
  Route,
  Link,
  Switch
} from 'react-router-dom';

import './App.css';
import './AboutUs.css';
import './ContactUs.css';
import './Services.css';

import AboutUs from './AboutUs.js';
import ContactUs from './ContactUs.js';
import Services from './Services.js';

function App() {
  return (
    <div className="App">
      <header>
        <h1>Business Name</h1>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/about-us">About Us</Link>
          <Link to="/contact-us">Contact Us</Link>
        </nav>
      </header>
      <Switch>
        <Route path="/" exact>
          <Services />
        </Route>
        <Route path="/about-us">
          <AboutUs />
        </Route>
        <Route path="/contact-us">
          <ContactUs />
        </Route>
      </Switch>
    </div>
  );
}

export default App;