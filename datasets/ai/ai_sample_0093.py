import matplotlib.pyplot as plt

data = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]

# plotting the histogram 
plt.hist(data, bins = [0, 20, 40, 60, 80, 100, 120, 140, 160], edgecolor = 'black') 
  
# x-axis label 
plt.xlabel('Range of values') 
# y-axis label 
plt.ylabel('Number of Occurrences') 
# plot title 
plt.title('Histogram of data') 
  
# function to show the plot 
plt.show()