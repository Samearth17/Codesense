class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct_tree(vals):
    root = Node(vals[0])
    for val in vals[1:]:
        node = Node(val)
        tmp_node = root
        while True:
            if node.val > tmp_node.val:
                if tmp_node.right is None:
                    tmp_node.right = node
                    break
                else:
                    tmp_node = tmp_node.right
            else:
                if tmp_node.left is None:
                    tmp_node.left = node
                    break
                else:
                    tmp_node = tmp_node.left
    return root