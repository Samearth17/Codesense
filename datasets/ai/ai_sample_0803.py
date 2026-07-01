# Define function to compute the gradient, given a set of weights
def compute_gradient(weights):
    
    # Compute the gradient with respect to each weight in the weight vector
    gradients = []
    for w in weights:
        gradients.append(2 * w)
    
    # Return the gradient vector
    return gradients

# Define a function to compute the cost, given a set of weights
def compute_cost(weights):
    
    # Compute the cost with given weights
    cost = 0
    for w in weights:
        cost += w**2
    
    # Return the cost
    return cost

# Gradient descent loop
weights = np.array([1, 2, 3]) # Initialize weights
learning_rate = 0.01 # Set learning rate

for i in range(1000): # Iterate for 1000 steps
    gradients = compute_gradient(weights) # Compute gradients
    weights -= learning_rate * np.array(gradients) # Do gradient descent step
    cost = compute_cost(weights) # Compute cost
    # Print cost every 100 steps 
    if i % 100 == 0:
        print("Cost at iteration %d: %f" % (i, cost))

# Print the final weights
print(weights)