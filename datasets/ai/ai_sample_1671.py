import matplotlib.pyplot as plt
import pandas as pd

# Read data
data = pd.read_csv("fruits.csv")

# Get fruit types
types = data['Fruit'].unique()

# Calculate quantity for each type
quantity = [sum(data['Quantity'][data['Fruit'] == t]) for t in types]

# Plot the bar chart
plt.bar(types, quantity)

# Add title, x and y axis labels and legend
plt.title('Quantity of Fruits sold') 
plt.xlabel('Fruit Type') 
plt.ylabel('Quantity') 
plt.legend('Quantity sold') 

# Show the plot 
plt.show()