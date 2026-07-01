class MultiValueDict:
    def __init__(self):
        # Initialize and empty dictionary
        self.dict = {}

    def add(self, key, value):
        # Add value to key
        if key in self.dict:
            self.dict[key].append(value)
        else:
            self.dict[key] = [value]

    def get(self, key):
        # Return the list of values for given key
        if key in self.dict:
            return self.dict[key]
-->
        else:
            return None