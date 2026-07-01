class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
  

class LinkedList: 
    def __init__(self):
        self.head = None
  
    # Function to insert a new node at the beginning
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  

# Example 
llist = LinkedList() 
node_values = [1, 2, 3, 4, 5]
for node in node_values:
    llist.push(node)