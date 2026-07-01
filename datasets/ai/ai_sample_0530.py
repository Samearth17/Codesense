import matplotlib.pyplot as plt 
 
# Data to plot
data = [1, 2, 3, 6, 5, 4, 7]
 
# Create the graph object
plt.bar(range(len(data)), data, align='center')
 
# Label the graph
plt.xticks(range(len(data)), range(1, len(data)+1))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bar Graph')
 
# Display the graph
plt.show()