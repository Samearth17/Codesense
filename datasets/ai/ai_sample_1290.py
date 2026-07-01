class HashTable:
    def __init__(self):
        self.table = {}

    def put(self, key, value):
        # Get the hash for the given key
        hash_value = self._hash(key)
        # If the hash value is not in the table, create an empty list
        if hash_value not in self.table:
            self.table[hash_value] = []
        # Append the value to the list
        self.table[hash_value].append((key, value))

    def get(self, key):
        # Get the hash for the given key
        hash_value = self._hash(key)
        # If the hash is not in the table, return None
        if hash_value not in self.table:
            return None
        # Search the list of (key, value) pairs for a matching key
        for k, v in self.table[hash_value]:
            if key == k:
                return v
        # If no matching key is found, return None
        return None

    def _hash(self, key):
        # Generate a simple hash of the given key
        return hash(key) % 1000