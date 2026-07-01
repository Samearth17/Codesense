import pandas as pd

# Create Series
data = [1, 2, 2, 3, 3, 3, 4, 5]
series = pd.Series(data)

# Calculate mean
mean = series.mean()

# Calculate median
median = series.median()

# Calculate mode
mode = series.mode()

# Print results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)