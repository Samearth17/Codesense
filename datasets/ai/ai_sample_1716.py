class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
        
    def insert_left(self, node):
        if self.left is None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t
        
    def insert_right(self, node):
        if self.right is None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t