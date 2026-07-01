items = [
 {"name": "widget", "price": 10, "quantity": 5 },
 {"name": "thingy", "price": 7, "quantity": 3 },
 {"name": "doodad", "price": 5, "quantity": 2 },
]

taxRate = 0.095
shippingCost = 7.50

totalCost = 0

for item in items:
 totalCost += item['price'] * item['quantity']

totalCost += totalCost * taxRate
totalCost += shippingCost

print('Total cost:', totalCost)