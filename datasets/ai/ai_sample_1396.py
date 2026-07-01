# Imports
import torch.nn as nn
import torch

# CNN Model
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # Convolutional blocks
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 6, 3, 1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2))
        self.conv2 = nn.Sequential(
            nn.Conv2d(6, 16, 3, 1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2))
        # Fully connected layers
        self.fc1 = nn.Linear(5 * 5 * 16, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
 
    def forward(self, x):
        # Forward pass through convolutional blocks
        out = self.conv1(x)
        out = self.conv2(out)
        # Flatten the tensor for use in fully connected layers
        out = out.view(-1, 5 * 5 * 16)
        # Forward pass through fully connected layers
        out = self.fc1(out)
        out = self.fc2(out)
        out = self.fc3(out)
        return out

# Create an instance of the model 
model = CNN()
# Move model to GPU if available
if torch.cuda.is_available():
  model.cuda()