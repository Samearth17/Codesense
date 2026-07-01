import pandas as pd

# Create a dataframe from the input data
df = pd.DataFrame([
    {"customer_id": 1, "month": 1, "amount": 40000},
    {"customer_id": 2, "month": 1, "amount": 10000},
    {"customer_id": 3, "month": 1, "amount": 20000},
    {"customer_id": 1, "month": 2, "amount": 30000},
    {"customer_id": 2, "month": 2, "amount": 15000},
    {"customer_id": 3, "month": 2, "amount": 50000},
])

# Group by customer and get the average purchase amount in each month
result = df.groupby('customer_id')['amount'].mean().sort_values(ascending=False).head(5)

# Print the result
print(result)