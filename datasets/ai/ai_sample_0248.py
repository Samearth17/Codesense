from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Read the data into a dataframe
df = pd.read_csv('spam.csv', header=None)

#Split data into features and target
X = df[df.columns[:-1]]
y = df[df.columns[-1]]

# Create a multinomial naive bayes classifier
model = MultinomialNB()

#Train the model
model.fit(X,y)

# Use the trained model to predict the class for the new data
predicted_classes = model.predict(X)

# Calculate the accuracy of the model
print("Accuracy:", model.score(X,y))