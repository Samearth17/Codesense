class Node: 
	
    def __init__(self, data): 
        self.data = data 
        self.children = [] 
  
    def add_child(self, node): 
        self.children.append(node) 
  
    def get_child(self, index): 
        return self.children[index] 
  
    def get_data(self): 
        return self.data 
  
    def get_children(self): 
        return self.children

root = Node(data=0) 
node1 = Node(data=1) 
node2 = Node(data=2) 
  
root.add_child(node1) 
root.add_child(node2) 
  
node3 = Node(data=3) 
node4 = Node(data=4) 
  
node1.add_child(node3) 
node1.add_child(node4) 
  
node5 = Node(data=5) 
node2.add_child(node5)