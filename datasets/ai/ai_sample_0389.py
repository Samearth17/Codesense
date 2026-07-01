class Queue:
 def __init__(self):
 self.queue = []

 def push(self, item):
 self.queue.append(item)

 def pop(self):
 return self.queue.pop(0)

 def peek(self):
 return self.queue[0]

# Usage example
q = Queue()
q.push(1)
q.push(2)
q.push(3)

print(q.pop()) # 1 
print(q.peek()) # 2