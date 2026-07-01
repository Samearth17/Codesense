# Python program to implement a binary tree

# A class that represents an individual node in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A class to represent the Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, curr_node, key):
        if key < curr_node.val:
            if curr_node.left is None:
                curr_node.left = Node(key)
            else:
                self._insert(curr_node.left, key)
        elif key > curr_node.val:
            if curr_node.right is None:
                curr_node.right = Node(key)
            else:
                self._insert(curr_node.right, key)

    def inOrder(self):
        res = []
        self._inOrder(self.root, res)
        return res

    def _inOrder(self, curr_node, res):
        if curr_node:
            self._inOrder(curr_node.left, res)
            res.append(curr_node.val)
            self._inOrder(curr_node.right, res)

    def preOrder(self):
        res = []
        self._preOrder(self.root, res)
        return res

    def _preOrder(self, curr_node, res):
        if curr_node:
            res.append(curr_node.val)
            self._preOrder(curr_node.left, res)
            self._preOrder(curr_node.right, res)

    def postOrder(self):
        res = []
        self._postOrder(self.root, res)
        return res

    def _postOrder(self, curr_node, res):
        if curr_node:
            self._preOrder(curr_node.left, res)
            self._preOrder(curr_node.right, res)
            res.append(curr_node.val)