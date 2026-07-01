class Stack:
    def __init__(self):
        self.items = []

    def push(self, x): 
        self.items.append(x) 

    def pop(self): 
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def is_empty(self): 
        return len(self.items) == 0