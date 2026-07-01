import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective(allocation):
    # Calculate portfolio return on investment
    portfolio_return = np.sum(allocation * stock_return)
    return -portfolio_return

# Set the bounds and constraints
bounds = [(0, n) for n in available_stocks]
constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x)-1}]

# Initialize the starting allocations
starting_allocations = np.array([1/len(available_stocks)]*len(available_stocks))

# Optimize
result = minimize(objective, starting_allocations, bounds=bounds, constraints=constraints)
allocation = result.x

# Print the optimal portfolio allocation
print(allocation)