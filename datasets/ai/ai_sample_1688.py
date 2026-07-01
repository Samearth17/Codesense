import torch
import torch.nn as nn
import torch.optim as optim

class SentimentClassifier(nn.Module):
 def __init__(self):
  super().__init__()
  self.embedding = nn.EmbeddingBag(1000, 16, sparse=True)
  self.fc = nn.Linear(16, 3)
 
 def forward(self, x):
  x = self.embedding(x)
  x = self.fc(x)
  return x

# instantiate the model
model = SentimentClassifier()

# define the loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# train the model
model.train()
for i in range(num_epochs):
 # iterate over the data
 for x,y in train_iter:
  # predict
  y_pred = model(x)
 
  # calculate the loss
  loss = criterion(y_pred, y)
 
  # backpropagate the loss
  loss.backward()
 
  # update weights
  optimizer.step()
 
  # zero grad
  optimizer.zero_grad()

# Test the model
model.eval()
with torch.no_grad():
 for x,y in test_iter:
  y_pred = model(x)
 
  # calculate the accuracy
  correct = (y == y_pred.argmax(dim=1)).float().sum()
  acc = correct/len(y)