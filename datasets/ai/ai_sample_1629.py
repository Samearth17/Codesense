import nltk
import numpy as np
import random
import string # to process standard python strings

# Read in the data
f = open('student_questions.txt','r',errors = 'ignore')
data = f.read()

conversationsPoints = data.lower().split("

")

# Create a dictionary that maps each word to its occurrence
word2count = {}
for conversation in conversationsPoints:
 for word in conversation.split():
 if word not in word2count.keys():
 word2count[word] = 1
 else:
 word2count[word] += 1

# Tokenize the words
words = sorted(list(word2count.keys()))

# Create the token_to_int dictionary
token2int = {}
int2token = {}

for i, word in enumerate(words):
 token2int[word] = i
 int2token[i] = word

# Create input and output datasets
X = []
Y = []

for conversation in conversationsPoints:
 sentence = conversation.lower().split()
 for i in range(1,len(sentence)):
 x = token2int[sentence[i-1]]
 y = token2int[sentence[i]]
 X.append(x)
 Y.append(y)

# One hot encode our input and output data
X_one_hot = np.zeros((len(X), len(words)), dtype=np.int32)
Y_one_hot = np.zeros((len(Y), len(words)), dtype=np.int32)

for i, x in enumerate(X):
X_one_hot[i][x] = 1

for i, y in enumerate(Y):
Y_one_hot[i][y] = 1


# Create and train the chatbot model
model = MyChatbot()
model.fit(X_one_hot, Y_one_hot, epochs=500, batch_size=32)

# Define bot response function
def bot_response(s):
 sentence = [word.lower() for word in s.split()]
 sentence = [token2int[word] for word in sentence]
 prediction = model.predict_single(sentence)
 int2word[prediction]
 return int2word[prediction]

# Run the app
while True:
 print('User: ', end='')
 s = input()
 response = bot_response(s)
 print('Chatbot: ' + response)