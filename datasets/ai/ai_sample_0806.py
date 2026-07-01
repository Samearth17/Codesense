class Stack:
 def __init__(self):
  self.stack = []

 def push(self, item):
  self.stack.append(item)

 def pop(self):
  if self.stack:
   return self.stack.pop()
  else: 
   return None

 def is_empty(self):
  return len(self.stack) == 0