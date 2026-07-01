class StoreItem:
    def __init__(self, item_id, name, price, description):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f'{self.name}, ${self.price}'

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }