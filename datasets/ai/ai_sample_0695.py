def optimize_shipping_cost(items):
 # sort items by cost
 items_by_cost = sorted(items, key=lambda x: x['cost'])
 
 # traverse the sorted list from the lowest to highest cost
 total_cost = 0 # total cost of the cart 
 weight = 0 # total weight of the cart
 for item in items_by_cost:
 weight += item['weight']
 
 # select the least expensive shipping option
 if weight <= 5:
 total_cost = 2 
 elif 6 < weight < 12:
 total_cost = 3 + (weight - 6) * 0.2
 else:
 total_cost = 2 + (weight - 5) * 0.5
 
 return total_cost