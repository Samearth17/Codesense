import matplotlib.pyplot as plt
 
# Create lists of data to plot
# Current year's temperatures
temperatures = [10, 12, 14, 13, 14, 14, 15]
 
# Create a chart of average temperatures
plt.plot(temperatures)
 
# Label the chart
plt.title('Average Temperatures in Celcius')
plt.xlabel('Month')
plt.ylabel('Temperature (Celsius)')
 
# Show the chart
plt.show()