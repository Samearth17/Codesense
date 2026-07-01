class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def are_similar(root1, root2):
    if root1 is None and root2 is None:
        return True
    if (root1 and root2) is None or (root1 or root2) is None:
        return False
    if root1.val != root2.val:
        return False
    else:
        return are_similar(root1.left, root2.left) and are_similar(root1.right, root2.right)