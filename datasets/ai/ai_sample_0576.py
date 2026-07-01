class Node:
    def __init__(self, val):
      self.right = None
      self.data = val
      self.left = None

def insert(node, data): 
  if node is None:
    return Node(data)
  else:
    if data <= node.data:
      node.left = insert(node.left, data)
    else:
      node.right = insert(node.right, data)
  return node