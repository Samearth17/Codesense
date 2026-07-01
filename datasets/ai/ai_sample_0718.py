import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5, 6]
y1 = [50, 60, 70, 80, 70, 60]
x2 = [1, 2, 3, 4, 5, 6]
y2 = [40, 50, 70, 80, 90, 100]

# set figure size
plt.figure(figsize=(8, 5))

# plot data
plt.plot(x1, y1, label='Product A')
plt.plot(x2, y2, label='Product B')

# beautify the graph
plt.xlabel('Months')
plt.xticks([1, 2, 3, 4, 5, 6])
plt.ylabel('Sales (in Units)')
plt.title('Comparing Sales of Two Products')
plt.legend()
plt.grid(True)

# show the chart
plt.show()