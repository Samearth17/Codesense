# Import Django
import django
from django.conf import settings
from django.urls import path

# Setup Django app
settings.configure()

# Create Django application
app = django.apps.registry.AppRegistry()

# Create URL path
@app.route('/compare')

# Define response
def compare_prices(): 
  # Get product and store information 
  product1 = request.args.get('product1') 
  store1 = request.args.get('store1') 
  product2 = request.args.get('product2)
  store2 = request.args.get('store2')

  # Make the API call to the stores' API 
  store1_data = requests.get(url1+product1+'&store='+store1).json()
  store2_data = requests.get(url2+product2+'&store='+store2).json()

  # Compare the prices 
  price1 = float(store1_data['price'])
  price2 = float(store2_data['price'])
  difference = price2 - price1

  # Return response
  return jsonify(
    store1=store1,
    store2=store2,
    product1=product1,
    product2=product2,
    price1=price1,
    price2=price2,
    difference=difference
  )

# Run the server
if __name__ == "__main__": 
  app.run()