class Stack:
 
 def __init__(self):
 self.head = None

 def is_empty(self):
 return self.head is None

 def push(self, data):
 node = Node(data)
 node.next = self.head
 self.head = node

 def pop(self):
 if self.head is None:
 return None
 data = self.head.data
 self.head = self.head.next
 return data

class Node:
 
 def __init__(self, data):
 self.data = data
 self.next = None