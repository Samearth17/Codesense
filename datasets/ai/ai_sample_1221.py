import wave
import pandas as pd
import numpy as np
from scipy.io import wavfile
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the data
data = pd.read_csv("dataset.csv")

# Extract the audio samples and labels as numpy arrays
samples = np.array([wavfile.read(f)[1] for f in data["Audio Sample"]])
labels = np.array(data["Label"])

# Split datasets into training and test
X_train, X_test, y_train, y_test = train_test_split(samples, labels, test_size=0.2)

# Create and train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Measure accuracy
accuracy = clf.score(X_test, y_test)
print('Model accuracy:', accuracy)