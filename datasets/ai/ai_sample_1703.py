import numpy as np
from sklearn.neural_network import MLPClassifier

# define model
model = MLPClassifier(hidden_layer_sizes=(6, 6), activation='relu')

# prune redundant neurons
pruned_model = MLPClassifier(hidden_layer_sizes=(4, 4), activation='relu')

# define data
x = np.random.rand(1000, 9)
y = np.random.randint(2, size=(1000,2))

# train pruned model
pruned_model.fit(x, y)

# evaluate pruned model
score = pruned_model.score(x, y)

print("Pruned model performance:", score)

# train original model
model.fit(x, y)

# evaluate original model
score = model.score(x, y)

print("Original model performance:", score)