class Node:
 def __init__(self, data):
 self.data = data
 self.next = None

class LinkedList:
 def __init__(self):
 self.head = None

 def add_node(self, data):
 new_node = Node(data)
 new_node.next = self.head
 self.head = new_node

 def delete_node(self, data):
 curr_node = self.head
 prev_node = None
 while curr_node:
 if curr_node.data == data:
 if prev_node:
 prev_node.next = curr_node.next
 else:
 self.head = curr_node.next
 return
 prev_node = curr_node
 curr_node = curr_node.next

 def search_node(self, data):
 curr_node = self.head
 while curr_node:
 if curr_node.data == data:
 return curr_node
 curr_node = curr_node.next
 return None