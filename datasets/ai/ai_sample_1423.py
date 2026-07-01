class CacheStorage:
    def __init__(self, ttl):
        self.ttl = ttl
        self.cache = {}
    
    def store(self, key, value):
        self.cache[key] = {"value": value,
                           "expire_at": time.time() + self.ttl}
    
    def fetch(self, key):
        # Check if key is expired
        if self.cache[key]["expire_at"] > time.time():
            return self.cache[key]["value"]
        else:
            # If expired, remove the key and return None
            self.cache.pop(key)
            return None