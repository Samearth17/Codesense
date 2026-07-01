class BinarySearchTree:

 def __init__(self):
  self.root = None

 def add_node(self, value):
  if not self.root:
   self.root = Node(value)
  else: 
   self._add_node(self.root, value)

 def _add_node(self, node, value):
  if value <= node.value:
   if node.left:
    self._add_node(node.left, value)
   else:
    node.left = Node(value)
  else:
   if node.right:
    self._add_node(node.right, value)
   else:
    node.right = Node(value)

 def search(self, value):
  return self._search(self.root, value)

 def _search(self, node, value):
  if node is None:
   return False
  if node.value == value:
   return True
  else:
   if value <= node.value:
    return self._search(node.left, value)
   else: 
    return self._search(node.right, value)

 def get_size(self):
  return self._get_size(self.root)

 def _get_size(self, node):
  if not node:
   return 0
  return self._get_size(node.left) + 1 + self._get_size(node.right)