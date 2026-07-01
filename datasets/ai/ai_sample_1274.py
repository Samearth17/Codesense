class KeyValuePairs:
    def __init__(self):
        self.data = dict()
    
    def set(self, key, value):
        self.data[key] = value
    
    def get(self, key):
        return self.data[key]
    
    def containsKey(self, key):
        return key in self.data
    
    def containsValue(self, value):
        for v in self.data.values():
            if v == value:
                return True
        return False