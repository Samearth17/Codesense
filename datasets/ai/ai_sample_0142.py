class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(256)]
 
    def insert(self, key, value):
        h = hash(key) % 256
        for i, kv in enumerate(self.table[h]):
            if kv[0] == key:
                self.table[h][i] = (key, value)
                return
        self.table[h].append((key, value))
 
    def retrieve(self, key):
        h = hash(key) % 256
        for kv in self.table[h]:
            if kv[0] == key:
                return kv[1]
 
    def delete(self, key):
        h = hash(key) % 256
        for i, kv in enumerate(self.table[h]):
            if kv[0] == key:
                del self.table[h][i]