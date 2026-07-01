class PriorityQueue:

    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def insert(self, key):
        self.queue.append(key)
        self.queue.sort(reverse=True)
    
    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None