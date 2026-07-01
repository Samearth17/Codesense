def nth_largest(root, n):
 if root is None or n <= 0:
 return -1
 
 stack = []
 while root or stack:
 while root:
 stack.append(root)
 root = root.right
 node = stack.pop()
 n -= 1
 
 if n == 0:
 break
 root = node.left
 
 return node.data