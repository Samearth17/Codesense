# A simple Tree class 
class Tree(object): 
    def __init__(self, data): 
        self.data = data  # root node 
        self.children = []  # empty list to store the children 
  
# Function to print the tree pre-order 
def traverse(tree): 
    print(tree.data) 
  
    # recursively traverse the Tree
    for value in tree.children: 
        traverse(value) 
  
# Create Tree 
tree = Tree('A') 
tree.children.append(Tree('B')) 
tree.children.append(Tree('C')) 
tree.children[0].children.append(Tree('D')) 
tree.children[0].children.append(Tree('E')) 

# Traverse the Tree 
traverse(tree)