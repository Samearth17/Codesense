import pandas as pd
import numpy as np

# Create spreadsheet
df = pd.DataFrame()

# Add column of x-values
x_values = np.arange(start=0,stop=2*np.pi,step=0.1)
df['x'] = x_values

# Add column of y-values
y_values = np.sin(x_values)
df['y'] = y_values

# Save spreadsheet
df.to_csv('sine-wave.csv', index=False)