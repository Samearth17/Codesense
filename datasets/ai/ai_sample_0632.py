import torch.nn as nn

class ANN(nn.Module):
    def __init__(self):
        super().__init__()
        # Input layer
        self.fc1 = nn.Linear(50, 64) # 50 input units, 64 neurons in the hidden layer
        self.relu1 = nn.ReLU()
        # Hidden layer 1
        self.fc2 = nn.Linear(64, 32)
        self.relu2 = nn.ReLU()
        # Hidden layer 2
        self.fc3 = nn.Linear(32, 16)
        self.relu3 = nn.ReLU()
        # Output layer
        self.fc4 = nn.Linear(16, 3)
        self.sigmoid = nn.Sigmoid()
 
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.fc2(x)
        x = self.relu2(x)
        x = self.fc3(x)
        x = self.relu3(x)
        x = self.fc4(x)
        x = self.sigmoid(x)
        return x