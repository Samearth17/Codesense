import pandas as pd

# Read the input data
df = pd.read_csv('company_data.csv')

# Select the top 5 companies by total revenue
top_5 = df.sort_values(by='revenue', ascending=False).head(5)

# Generate the report
print("Top 5 Companies by Total Revenue")
print("-------------------------------")
for index, row in top_5.iterrows():
 print("Company name: {}, Total Revenue: {:.2f}, Total Profit: {:.2f}".format(
 row['name'], row['revenue'], row['profit']
 ))