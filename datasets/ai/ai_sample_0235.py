import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# loading dataset
df = pd.read_csv("spam_classification.csv")

# splitting dataset
X = df["Message"]
y = df["Label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# creating a model
model = MultinomialNB()
model.fit(X_train, y_train)

# evaluating the model
score = model.score(X_test, y_test)
print("Model score: {}".format(score))