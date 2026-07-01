class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Insert nodes to the binary search tree.
    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left == None:
                        current_node.left = new_node
                        return
                    current_node = current_node.left
                else:
                    if current_node.right == None: 
                        current_node.right = new_node
                        return
                    current_node = current_node.right
                
    def printTree(self, node): 
        if node != None: 
            self.printTree(node.right)
            print(node.value)
            self.printTree(node.left)

# Test code
bst = BinarySearchTree()
nums = [10,4,2,15,14,16]
for num in nums:
    bst.insert(num)
bst.printTree(bst.root)