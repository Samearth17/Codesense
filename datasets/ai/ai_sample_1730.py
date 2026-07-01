import flask
from geopy.distance import geodesic


app = flask.Flask('__name__')

stores = [
    {
        'store_id': 1,
        'name': 'Store A',
        'address': '2 Main Street, Anytown, US'
    },
    {
        'store_id': 2,
        'name': 'Store B',
        'address': '3 Main Street, Anytown, US'
    },
    {
        'store_id': 3,
        'name': 'Store C',
        'address': '4 Main Street, Anytown, US'
    },
]

@app.route('/nearest-store', methods=['POST'])
def find_nearest_store():
    request_data = flask.request.get_json()
    address = request_data.get('address')

    nearest_store = None
    min_distance = None

    for store in stores:
        store_distance = geodesic(address, store['address']).kilometers
        if not min_distance or store_distance < min_distance:
            nearest_store = store
            min_distance = store_distance

    return flask.jsonify({
        'store': nearest_store
    })

if __name__ == '__main__':
    app.run()