# Establish an SQL connection 
import sqlite3
conn = sqlite3.connect("mydatabase.db")

# Create a cursor object 
c = conn.cursor()

# Execute SQL Query 
c.execute("SELECT * FROM TABLE")

# Store the result in a dataframe 
import pandas as pd
df = pd.DataFrame(c.fetchall()) 

# Perform some manipulation on the data 
# E.g. Add a new column 
df['new_col'] = df['old_col1'] + df['old_col2']

# Update the table 
df.to_sql("TABLE", conn, if_exists='replace', index=False)

# Close connection 
conn.close()