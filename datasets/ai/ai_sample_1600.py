class Node:
 def __init__(self, val):
 self.val = val
 self.left = None
 self.right = None

def findMaxValue(root):
 if root is None:
 return None
 
 if root.right is None:
 return root.val
 
 return findMaxValue(root.right)

# Usage example
root = Node(3)
root.left = Node(2)
root.right = Node(5)

maxValue = findMaxValue(root)
print('Max Value:', maxValue)