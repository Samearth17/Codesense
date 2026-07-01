class Node: 
 def __init__(self, data): 
 self.data = data
 self.left = None
 self.right = None

# Function to insert a node 
def insert(node, data): 
 if node is None: 
 node = Node(data) 
 elif data < node.data: 
 node.left = insert(node.left, data) 
 else: 
 node.right = insert(node.right, data) 

return node 

if __name__ == '__main__':
 root = None 
 root = insert(root, 8) 
 root = insert(root, 3) 
 root = insert(root, 10) 
 root = insert(root, 1) 
 root = insert(root, 6)
 root = insert(root, 4) 
 root = insert(root, 7) 
 root = insert(root, 14)
 root = insert(root, 13)