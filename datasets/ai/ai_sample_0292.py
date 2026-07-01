class Node:
 def __init__(self, data):
  self.data = data
  self.next = None

class LinkedList:
 def __init__(self):
  self.head = None
  
 # Recursive function to insert a node at the beginning of the linked list 
 def insert_at_head(self, new_node): 
  current_head = self.head 
  new_node.next = current_head
  self.head = new_node

list = LinkedList()
list.insert_at_head(Node(1))