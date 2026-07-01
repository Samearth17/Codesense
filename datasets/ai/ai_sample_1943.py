class Node:
 def __init__(self, data):
  self.data = data
  self.next = None

class SinglyLinkedList:
 def __init__(self):
  self.head = None
  self.tail = None
  self.middle = None

 def addNode(self, node):
  if self.head is None:
   self.head = node
   self.tail = node
   self.middle = node
  else:
   self.tail.next = node
   self.tail = node
   # To mark the middle node
   if self.head.next is self.middle:
    self.middle = node

 def mark_middle(self):
  if self.middle is None:
   return
  self.middle.data = 'Middle Node'