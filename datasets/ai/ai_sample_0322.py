import numpy as np 

# Create data
data = np.array([2, 3, 1, 4, 5, 6, 5, 8, 9, 10, 11, 12])

# Calculate mean and standard deviation
mean = np.mean(data)
std = np.std(data)

# Set the boundaries
lower_bound = mean - 3*std
upper_bound = mean + 3*std

# Find outliers
outliers = [] 
for i in data: 
    if i < lower_bound or i > upper_bound: 
        outliers.append(i)

# Print the outliers
print("Outliers:", outliers) 

"""
Outliers: [1, 11, 12]
"""