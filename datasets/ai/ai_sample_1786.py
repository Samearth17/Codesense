import numpy as np

# Define the function to be optimized
def f(x, y):
    return np.square(x) + 2 * np.square(y)

# Initialize the parameters
x = 0
y = 0
learning_rate = 10

# Gradient Descent Algorithm
for i in range(1000):
    # Calculate the derivatives
    grad_x = 2 * x
    grad_y = 4 * y

    # Calculate the new values
    x -= learning_rate * grad_x
    y -= learning_rate * grad_y

# Print the minimum
print("The minimum is: {:.4f}".format(f(x, y)))