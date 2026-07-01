#import necessary packages
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

# define the word embedding layer
class WordEmbeddingLayer(nn.Module):
	def __init__(self, vocab_size, embedding_dim):
		super().__init__()
		# define the embedding layer
		self.embedding = nn.Embedding(vocab_size, embedding_dim)

	def forward(self, x):
		# lookup the embeddings for the input
		return self.embedding(x)

# define the recurrent neural network
class SentimentRNN(nn.Module):
	def __init__(self, embedding_dim, hidden_dim, output_dim, n_layers, dropout, bidirectional, pad_idx):
		super().__init__()
		# define the embedding layer
		self.embedding = WordEmbeddingLayer(vocab_size, embedding_dim)
		# define the recurrent neural network
		self.rnn = nn.LSTM(embedding_dim, hidden_dim, num_layers=n_layers, bidirectional=bidirectional, dropout=dropout)
		# define the output layer
		self.fc = nn.Linear(hidden_dim * 2, output_dim)
		# define the dropout layer
		self.dropout = nn.Dropout(dropout)
		# define the padding id
		self.pad_idx = pad_idx

	def forward(self, text):
		# look up the embeddings
		embedded = self.embedding(text)
		# perform the recurrent neural network
		outputs, (hidden, cell) = self.rnn(embedded)
		# perform dropout
		outputs = self.dropout(outputs)
		# get the last output
		out = outputs[-1, :, :]
		# apply the output layer
		out = self.fc(out)
		return out

# define the model
model = SentimentRNN(embedding_dim=100, hidden_dim=256, output_dim=1, n_layers=2, bidirectional=True, dropout=0.5, pad_idx=1)

# define the optimizer	
optimizer = torch.optim.Adam(model.parameters())

# define the test sentence
test_sentence = "I am so happy right now!"

# predict the sentiment of the sentence
pred = model(test_sentence)

# print the prediction
print(pred)