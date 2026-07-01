import matplotlib
import matplotlib.pyplot as plt

# Generate the data for the dashboard
x = [1,2,3,4,5]
y = [10,25,30,50,80]

# Create the figure and set the size
fig = plt.figure(figsize=(10,6))

# Configure the plot
plt.plot(x, y, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.title("My Data Visualization Dashboard")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()