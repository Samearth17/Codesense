import pandas as pd

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from keras.models import Sequential

from keras.layers import Dense, GRU, Embedding

# Load the dataset
df = pd.read_csv("reviews.csv")

# Select labels and text
data = df[["review", "sentiment"]]

# Split data into training and test set
train_data, test_data = train_test_split(data, random_state=42)

# Tokenize the text
tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_data['review'])

# Pad and encode the sequences
# This pad the article to a length of 120
X_train = tokenizer.texts_to_sequences(train_data['review'])
X_test = tokenizer.texts_to_sequences(test_data['review'])

X_train = pad_sequences(X_train, maxlen=120)
X_test = pad_sequences(X_test, maxlen=120)

# Prepare labels
y_train = train_data['sentiment']
y_test = test_data['sentiment']

# Create a model
model = Sequential()
model.add(Embedding(1000, 128, input_length=120))
model.add(GRU(256))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X_train, y_train, batch_size=128, epochs=20)