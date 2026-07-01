def search(query):
 results = []
 for product in products:
 if query in product.name:
 results.append({
 'name': product.name,
 'price': product.price,
 'description': product.description,
 'image': product.image
 })
 return results
 
products = [
 {'name': 'white shoes', 'price': 19.99, 'description': 'Nice shoes for the summer', 'image': 'image.jpg'}, 
 {'name': 'black shoes', 'price': 32.00, 'description': 'Stylish shoes for a night out', 'image': 'image2.jpg'}
]

query = "shoes"
results = search(query)
print(results)