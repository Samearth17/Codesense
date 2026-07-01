# Python program to print reverse level 
# order traversal
  
# Binary Tree Node
class Node: 
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
  
#reverse Level Order Traversal 
def reverseLevelOrder(root): 
    # Base Case 
    if root is None: 
        return
  
    # Create an empty queue for level order  
    # traversal 
    q = []
  
    # Enqueue Root and initialize height 
    q.append(root) 
      
    # Loop while there is at least one  
    # discovered node 
    while(len(q) > 0): 
        # Print front of queue and remove it from queue 
        print(q[len(q)-1].data) 
        node = q.pop(len(q)-1) 
          
        # Insert right child first 
        if node.right is not None: 
            q.append(node.right) 
          
        # Insert left child 
        if node.left is not None: 
            q.append(node.left)  
  
#Driver Program
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
  
# Function Call 
reverseLevelOrder(root)