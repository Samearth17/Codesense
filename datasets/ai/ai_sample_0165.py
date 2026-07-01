class Node:
    """Node class to represent the node in a linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList class to represent the entire linked list"""
    def __init__(self):
        self.head = None
    
    def print_list(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next

# Creating a linked list 
linked_list = LinkedList()

# Creating the nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Linking the nodes
linked_list.head = node1
node1.next = node2
node2.next = node3

# Printing the linked list
linked_list.print_list()