class Stack:
  
    # empty list to store stack elements
    def __init__(self):
        self.stack = []
  
    # push element to the stack
    def push(self, data):
        self.stack.append(data)
  
    # pop element from the stack
    def pop(self):
        self.stack.pop() 
  
    # peek element from the stack
    def peek(self):
        return self.stack[-1]