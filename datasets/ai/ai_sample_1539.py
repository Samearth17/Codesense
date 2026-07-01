import pandas as pd

# a data frame with the customer's purchase history
purchases = pd.DataFrame({
    'item' : ["Lipstick", "Wine Glasses", "Cap"],
    'price': [10, 20, 15],
    'gender': [0, 1, 0]
})

# number of customers who bought each item
item_counts = purchases.groupby('item').count()

# probability of each item being bought by a customer
prob_items = item_counts / len(purchases)

# probability of the customer being either male or female
prob_gender = purchases.groupby('gender').count() / len(purchases)

# probability of the customer being male given they bought the items
prob_gender_given_items = (purchases.groupby(['item','gender']).count() / len(purchases)).divide(prob_items, axis=0)

# gender of the customer based on their purchase history
customer_gender = prob_gender_given_items['price']['Lipstick', 'Wine Glasses', 'Cap'].multiply(prob_gender['price']).idxmax()

print("The customer is classified as: " + str(customer_gender)) # Output: The customer is classified as: 0