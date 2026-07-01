class Node:
 def __init__(self, data, left=None, right=None):
  self.data = data
  self.left = left
  self.right = right

class BinaryTree:
 def __init__(self):
  self.root = None

 def search(self, char):
  current = self.root
  while current:
   if char == current.data:
    return True
   elif char < current.data:
    current = current.left
   else:
    current = current.right
  return False

tree = BinaryTree()
tree.root = Node('F')
tree.root.left = Node('D')
tree.root.right = Node('J')
tree.root.left.left = Node('B')
tree.root.left.right = Node('E')
tree.root.right.left = Node('G')
tree.root.right.right = Node('K')

print(tree.search('G')) # Output: True