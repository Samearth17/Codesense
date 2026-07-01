# Python 
class Node: 
  def __init__(self, data): 
    self.data = data 
    self.children = [] 
  
def buildTree(relationships): 
  tree = {} 
  for parent, child in relationships: 
    if parent not in tree: 
      tree[parent] = Node(parent) 
    parent_node = tree[parent] 
    if child not in tree: 
      tree[child] = Node(child) 
    child_node = tree[child] 
    parent_node.children.append(child_node) 
  return tree[1]