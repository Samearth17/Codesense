import pandas as pd
import matplotlib.pyplot as plt

# Read the sales data
data = pd.read_csv('sales_data.csv')

# Create a figure
fig = plt.figure()

# Create a bar chart
ax = fig.add_subplot()
ax.bar(data['date'], data['sales'], color='orange')

# Set the x-axis and y-axis limits
ax.set_xlim([min(data['date']), max(data['date'])])
ax.set_ylim([0, max(data['sales']) + 10])

# Set the title of the chart
ax.set_title('Sales of a Product')

# Display the chart
plt.show()