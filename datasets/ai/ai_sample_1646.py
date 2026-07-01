temperatures = {
 'January': [10, 11, 12],
 'February': [15, 13, 16]
}

# Calculate average temperature
avgTemperatures = {}
for month in temperatures:
 avgTemperatures[month] = sum(temperatures[month])/len(temperatures[month])

# Calculate maximum temperature
maxTemperatures = {}
for month in temperatures:
 maxTemperatures[month] = max(temperatures[month])

print('Average Temperatures:', avgTemperatures)
print('Max Temperatures:', maxTemperatures)