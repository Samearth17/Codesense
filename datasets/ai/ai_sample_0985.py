import matplotlib.pyplot as plt

# arbitrary data
data = [1, 4, 6, 3, 8, 3, 7, 9, 1]

# create bins of values
bins = [0, 2, 4, 6, 8, 10]

# create the histogram
plt.hist(data, bins, histtype='bar', rwidth=0.8)

# label the axes
plt.xlabel('Data Values')
plt.ylabel('Number of Occurrences')

# add title
plt.title('Histogram of Data')

# display the histogram
plt.show()