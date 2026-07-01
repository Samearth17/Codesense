import torch

# Load the pre-trained model
model = torch.load('model.pt')

# Get the input data
input_data = "This movie was amazing!"

# Convert the input data into a tensor
input_tensor = torch.tensor([input_data])

# Make a prediction with the pre-trained model
prediction = model(input_tensor)

# Get the results
if prediction[0][0].item() > 0.5:
  print('Positive sentiment')
else:
  print('Negative sentiment')