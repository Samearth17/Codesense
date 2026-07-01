class TreeNode:
 
 def __init__(self, val):
  self.val = val
  self.left = None
  self.right = None

class BST:
 
 def __init__(self):
  self.root = None
 
 def insert(self, val):
  node = TreeNode(val)
  if self.root is None:
   self.root = node
  else:
   self.__insert_helper(self.root, node)
 
 def __insert_helper(self, root, node):
  if node.val < root.val:
   if root.left is None:
    root.left = node
   else:
    self.__insert_helper(root.left, node)
  else:
   if root.right is None:
    root.right = node
   else:
    self.__insert_helper(root.right, node)
    
def search(self, val):
 node = self.__search_helper(self.root, val)
 return node is not None

def __search_helper(self, root, val):
 if root is None:
  return None
 if root.val == val:
  return root
 if val < root.val:
  return self.__search_helper(root.left, val)
 else:
  return self.__search_helper(root.right, val)