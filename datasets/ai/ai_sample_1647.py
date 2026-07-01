# import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the dataset
data = pd.read_csv('TimeSeriesData.csv')

# check for missing values 
data.isnull().sum()

# check the data types 
data.dtypes

# check the descriptive statistics
data.describe()

# visualize the data
data.hist(bins = 50)
plt.show()

# check for outliers
for column in data:
 data.boxplot(column, vert = False)
 plt.show()