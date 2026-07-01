import pandas as pd

# load the dataset
data = pd.read_csv('data.csv')

# display information about the dataset
data.info()

# observe the first five rows
data.head()

# list all columns
data.columns 

# display summary statistics
data.describe()